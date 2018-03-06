from math import *
from tkinter import *
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
	
	
def err(x):
	if (sin(x) != 0):
		return abs((my_sin(x) - sin(x))/sin(x))
	else:
		return 0
		
		
root = Tk()
x_0 = 100
y_0 = 10**(12)
x_sc = 10**(10)
canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500, 1000, 500, 0, width = 2, arrow = LAST)
canv.create_line(0, 500, 1000, 500, width = 2, arrow = LAST)
canv.create_text(980, -20 +500, font = ("Purisa", 18), text = "x", fill
= "purple")
canv.create_text(-57 + 500, 25, font = ("Purisa", 15), text = "err*" +
str(x_sc), fill = "purple")
First_x = -500
for i in range(16000):
	if (i % 800 == 0):
		k = First_x + (1 / 16) * i
		canv.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width=0.5,ill='black')
		canv.create_line(k + 500, 0, k + 500, 1000, width=0.1, fill='grey', dash=(1, 1))
		canv.create_text(k + 515, 10 + 500, font = ("Purisa", 10), text=
			str(k/x_0), fill="purple")
		if (k != 0):
			canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width
				=0.5, fill='black')
			canv.create_line(0, k + 500, 1000, k + 500, width=0.1, fill='grey', dash=(1, 1))
			canv.create_text(25 + 500, k + 500 + 20, font = ("Purisa",	10), text=str(-k/y_0*x_sc), fill="purple")
	try:
		x = First_x + (1 / 16) * i
		y = -err(x/x_0)*y_0 + 499
		x += 499
		canv.create_oval(x, y, x + 1, y + 1, fill='black')
	except:
		First_x = -500


canv.pack()
root.mainloop()
