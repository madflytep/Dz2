import math
def my_sin(x):
	term = x
	sum = x
	eps = 10**(-8)
	n = 1
	while (abs(term) > abs(sum * eps)):
		n += 1
		term = -term * x**2 /( (2*n-1) * (2*n-2) )
		sum = sum + term
	return sum
x = 0
while (True):
	x+= 0.25
	if (math.sin(x) != 0):
		print ("x = ", x, " ", abs ((my_sin(x) - math.sin(x))/(math.sin(x))), my_sin(x + 2*math.pi) - my_sin(x))
	else:
		print ("sin(x) = 0, my_sin(x) = ", my_sin(x))
