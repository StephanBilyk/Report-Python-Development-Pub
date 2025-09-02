#Generate reports from team, product, and sales data

import csv
import argparse
from collections import defaultdict

def read_team_map(file_path):
    team_map = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            team_map[int(row['TeamId'])] = row['Name']
    return team_map

def read_product_master(file_path):
    product_master = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            pid = int(row[0])
            name = row[1]
            price = float(row[2])
            lot_size = int(row[3])
            product_master[pid] = {'name': name, 'price': price, 'lot_size': lot_size}
    return product_master

def read_sales(file_path):
    sales = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append({
                'SaleId': int(row[0]),
                'ProductId': int(row[1]),
                'TeamId': int(row[2]),
                'Quantity': int(row[3]),
                'Discount': float(row[4])
            })
    return sales

def generate_reports(team_map, product_master, sales):
    team_revenue = defaultdict(float)
    product_data = defaultdict(lambda: {'revenue': 0.0, 'units': 0, 'discount_cost': 0.0})

    for sale in sales:
        pid = sale['ProductId']
        tid = sale['TeamId']
        quantity = sale['Quantity']
        discount = sale['Discount']

        product = product_master[pid]
        price = product['price']
        lot_size = product['lot_size']
        name = product['name']

        units = quantity * lot_size
        gross = units * price
        discount_cost = gross * (discount / 100.0)

        team_revenue[tid] += gross

        product_data[pid]['revenue'] += gross
        product_data[pid]['units'] += units
        product_data[pid]['discount_cost'] += discount_cost

    return team_revenue, product_data

def write_team_report(output_path, team_revenue, team_map):
    sorted_teams = sorted(team_revenue.items(), key=lambda x: x[1], reverse=True)
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Team', 'GrossRevenue'])
        for tid, revenue in sorted_teams:
            team_name = team_map.get(tid, f"Unknown Team {tid}")
            writer.writerow([team_name, round(revenue, 2)])

def write_product_report(output_path, product_data, product_master):
    sorted_products = sorted(product_data.items(), key=lambda x: x[1]['revenue'], reverse=True)
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'GrossRevenue', 'TotalUnits', 'DiscountCost'])
        for pid, data in sorted_products:
            name = product_master[pid]['name']
            writer.writerow([name, round(data['revenue'], 2), data['units'], round(data['discount_cost'], 2)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--team-map', required=True)
    parser.add_argument('-p', '--product-master', required=True)
    parser.add_argument('-s', '--sales', required=True)
    parser.add_argument('--team-report', required=True)
    parser.add_argument('--product-report', required=True)
    args = parser.parse_args()

    team_map = read_team_map(args.team_map)
    product_master = read_product_master(args.product_master)
    sales = read_sales(args.sales)

    team_revenue, product_data = generate_reports(team_map, product_master, sales)

    write_team_report(args.team_report, team_revenue, team_map)
    write_product_report(args.product_report, product_data, product_master)

if __name__ == '__main__':
    main()
