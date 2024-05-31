import csv
import pprint

f = open("Employees.csv", "r")

cdr=csv.DictReader(f)


emp={}
for row in cdr:
    emp[row['Name']]=row

pprint.pprint(emp)

f.close()