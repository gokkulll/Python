import csv

f = open("Employees.csv", "r")

cdr=csv.DictReader(f)



for row in cdr:
    print(row)

f.close()