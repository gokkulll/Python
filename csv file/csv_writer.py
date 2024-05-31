import csv


doses = [('Melissa Smith',8/14/2000,13.1,14.00),
('Melissa Smith',4/22/2024,9.00,5.00),		
('Melissa Smith',4/1/2024,9.00,4.30)]


f = open("Employ.csv", 'w',newline='')
csv_w=csv.writer(f)

for row in doses:
    csv_w.writerow(row)

f.close()

