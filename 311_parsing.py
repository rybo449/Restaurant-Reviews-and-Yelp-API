import csv
import sys

f = open(sys.argv[1])
reader = csv.reader(f)
data = []
for i in reader:
	data.append([i[1], i[5], i[7], i[8], i[10], i[12], i[13], i[17]])
f.close()
f = open(sys.argv[2], 'w')
writer = csv.writer(f, delimiter = ',')
for i in data:
	writer.writerow(i)
f.close()