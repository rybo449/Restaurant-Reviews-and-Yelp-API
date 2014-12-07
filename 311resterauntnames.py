import sys
import csv
import operator

f = open(sys.argv[1])
reader = csv.reader(f)
line1 = next(reader)
f1 = open('names.csv','w')
name_write = csv.writer(f1,delimiter = ',')
name = {}
for i in reader:
	count = name.setdefault(i[1], 0)
	name[i[1]] = count + 1
for i in name.keys():
	name_write.writerow([i])

f.close()
f1.close()