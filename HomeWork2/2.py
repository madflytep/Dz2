import math
under = -1
over = 1
N = 1000000000
for i in range (N):
	under = abs(under)*1000000
	over = over*1000000
	print ("Loop: ", i, " ", -math.log10(abs(under)), " ", math.log10(
	over))
