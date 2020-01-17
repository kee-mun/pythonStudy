import csv

with open('test.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in reader:
        print(' '.join(row))