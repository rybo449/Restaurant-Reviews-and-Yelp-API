import sys

f = open(sys.argv[1])
for i in f:
	print i.strip()+ ",",