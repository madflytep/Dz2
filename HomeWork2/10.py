from math import *
def s_1(N):
	n = 1
	sum = -0.5
	term = -0.5
	while (n < 2*N):
		term = term * (-1)*((n+1)**2)/(n*(n+2))
		sum += term
		n += 1
	return sum
def s_2(N):
	n = 1
	sum = 0
	while (n < N):
		sum += -(2*n-1)/(2*n) + (2*n)/(2*n+1)
		n += 1
	return sum
def s_3(N):
	n = 1
	sum = 1/6
	term = 1/6
	while (n < N):
		term = term * (2*n*(2*n+1))/((2*n+2)*(2*n+3))
		sum += term
		n += 1
	return sum
