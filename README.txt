Stephan Bilyk
XR Trading 
Technical Operations Analyst
Python Development Challenge - SE

Create a Python application that will read from 3 input files and use the data within to produce 2 output 
files.

Bilyk_Stephan.zip contains:
report.py
Sales.csv
ProductMaster.csv
TeamMap.csv

report.py will run with this command:

python report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csv

Running this command will produce two files:

TeamReport.csv
ProductReport.csv

The Team Report file is a comma-separated text file where each line contains two values: the string 
name of the sales team and the total gross revenue of their team’s sales.  The file should contain a header with 
the field names, and teams should be in descending order by their gross revenue.

The Product Report file is a comma-separated text file where each line summarizes the sales of a single 
Product and contains four values as follows: 
Name – name of the Product 
GrossRevenue – gross revenue of sales of the Product 
TotalUnits – total number of units sold in the Product 
DiscountCost – total cost of all discounts provided on sales of the Product 
The file should contain a header with the field names, and the products should be provided in descending order 
of their gross revenue.

"Large Test" folder has personal input data that may be used but must be in same directory as report.py to run with the above command.