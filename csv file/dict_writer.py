import csv

data=[
{'Country':'India','doses':'1.29Cr','status':"ok"},
{'Country':'Australia','doses':'1Cr','status':"not ok"}
]

f = open('dict_writer.csv', 'w',newline='')
fields=['Country','doses','status']
wrtr = csv.DictWriter(f,fields)

wrtr.writeheader()
for d in data:
    wrtr.writerow(d)

f.close()