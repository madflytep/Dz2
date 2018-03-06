from math import *
def solve(a, b, c):
	if (b**2 >= 4*a*c) and (a != 0) and (c != 0):
		print ((-b + sqrt(b**2-4*a*c))/(2*a), (-b - sqrt(b**2-4*a*c))/(2*a))
		print ((2*c)/(-b - sqrt(b**2-4*a*c)), (2*c)/((-b + sqrt(b**2-4*a*c))))
		sum = 0
		x = -4*a*c/b**2
		f = 1
		term = 1
		sum = 1
		eps = 10 ** (-40)
		n = 0
		while (abs(term) > abs(sum * eps)):
			term = term * x * (1-2*n)/(2*(n+1))
			sum = sum + term
			n += 1
		print (b*(-1+b/abs(b)*sum)/(2*a), b*(-1-b/abs(b)*sum)/(2*a))
		print ((2*c)/(b*(-1-b/abs(b)*sum)), (2*c)/(b*(-1+b/abs(b)*sum)))
	else:
		if (a == 0) and ( b != 0):
			print ((-c/b), (-c/b))
		else:
			if (a == 0) and ( b == 0):
				if (c == 0):
					print ("x in (-inf, +inf)")
				else:
					if ( c != 0):
						print("NaN, NaN")
					else:
						print("Error: D < 0")
while (True):
	try:
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))
	except:
		print ("Exit")
		break
	solve(a, b, c)						
