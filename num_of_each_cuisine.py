import sys
import csv
import operator

f = open(sys.argv[1])
reader = csv.reader(f)
line1 = next(reader)
f1 = open('dump.csv','w')
name_write = csv.writer(f1,delimiter = ',')
name = {}

for i in reader:
	if i[line1.index('CRITICAL FLAG')] == 'Critical':
		count = name.setdefault((i[1],i[line1.index('CUISINE DESCRIPTION')]), 0)
		name[(i[1],i[line1.index('CUISINE DESCRIPTION')])] = count + 1
name1 = {}
for i,j in name.iteritems():
	count = name1.setdefault(i[1], 0)
	name1[i[1]] = count + 1

name1 = sorted(name1.items(), key=operator.itemgetter(1), reverse = True)	
for i,j in name1:
	name_write.writerow([i,j])
f.close()
f1.close()