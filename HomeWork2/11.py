from math import *
from tkinter import *

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
	
def err(x):
	try:
		return abs((s_1(x)-s_3(x))/s_3(x))
	except:
		return 1
root = Tk()
x_0 = 10**(0)
y_0 = 10**(2)
x_sc = 10**(0)
canv = Canvas(root, width=1000, height=1000, bg="white")
canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)
canv.create_text(980, -20 + 500, font=("Purisa", 18), text="x", fill="purple")
canv.create_text(-57 + 500, 25, font = ("Purisa", 15), text="err*"+ str(
x_sc), fill="purple")
First_x = -500;
my_file = open("lg.dat", "w")
for i in range(18000):
	if (i % 1800 == 0):
		k = First_x + (1 / 18) * i
		canv.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width=0.5,fill='black')
		canv.create_line(k + 500, 0, k + 500, 1000, width=0.1, fill='grey', dash=(1, 1))
		canv.create_text(k + 515, 10 + 500, font = ("Purisa", 10), text=str(k/x_0), fill="purple")
		if (k != 0):
			canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width=0.5, fill='black')
			canv.create_line(0, k + 500, 1000, k + 500, width=0.1, fill='grey', dash=(1, 1))
			canv.create_text(25 + 500, k + 500 + 20, font = ("Purisa",10), text=str(-k/y_0*x_sc), fill="purple")
	try:
		x = First_x + (1 / 18) * i
		y = -err(x/x_0)*y_0 + 499
		x += 499
		canv.create_oval(x, y, x + 1, y + 1, fill='black')
		my_file.write(str(x - 499) + " " + str(499-y) + "\n")
	except:
		First_x = -500
my_file.close()
canv.pack()
root.mainloop()
