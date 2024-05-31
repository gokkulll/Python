import csv

f = open('Employees.csv', 'r')

csv_reader=csv.reader(f)


next(csv_reader)

slas=[]
for row in csv_reader:
    slas.append(row[2])

print(slas)
print("Max:", max(slas))
print("Min:", min(slas))