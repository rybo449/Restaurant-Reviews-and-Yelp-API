import csv

f = open('names.csv')
names = {}
reader = csv.reader(f)
for i in reader:
	count = names.setdefault(i[0], 0)
	names[i[0]] = count + 1
f.close()

f = open('data.csv')
reader = csv.reader(f)
f1 = open('parsed_data.csv', 'w')
writer = csv.writer(f1)
for i in reader:
	#print i[2]
	if i[2].strip() in names:
		writer.writerow(i)