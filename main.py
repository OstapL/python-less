import csv
File = 'Sacramentorealestatetransactions.csv'
exampleReader = csv.reader(open(File))
for row in exampleReader:
    if exampleReader.line_num <= 1:
        continue
    print(row)
