import csv

f = open("Employees.csv", 'r')

csv_reader=csv.reader(f)

next(csv_reader)


name=[]
for row in csv_reader:
    name.append(row[0])

print(name)

f.close()