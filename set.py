import csv
names = []
f = open('names.csv')
reader = csv.reader(f)
for row in reader:
	names.append(row[0])
names = list(set(names))
f.close()
f = open('names.csv', 'w')
writer = csv.writer(f)
for i in names:
	writer.writerow([i.lower()])
f.close()