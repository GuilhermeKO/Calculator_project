#---------------------Calculator---------------------#
#16/jan/21
#author: Guilherme K
#version 1.0.1

from tkinter import *
from math import * 

root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file='pixil-frame-0.png'))

e = Entry(root, borderwidth = 5, width = 26, font = ("arial", 18)) 
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

conta = 0
def button_click(num):
	global conta
	if conta == 1:
		e.delete(0, END)
		e.insert(0, str(num))
		conta = 0
	elif conta == 0:
		var = e.get()
		e.delete(0, END)
		e.insert(0, str(var) + str(num))

def button_operator(op):
	num1 = e.get()
	e.delete(0, END)

	global operator 
	global number 
	operator = str(op)
	number = float(num1) 

def button_equal():
	num2 = e.get()
	e.delete(0, END)
	global conta
	conta = 1
	if operator == "+":
		e.insert(0, number + float(num2))
	elif operator == "-":
		e.insert(0, number - float(num2))
	elif operator == "*":
		e.insert(0, number * float(num2))
	elif operator == "/":
		if int(num2) == 0:
			e.insert(0, "ERROR")
		else:	
			e.insert(0, number / float(num2))
	elif operator == "^":
		e.insert(0, number ** float(num2))
	else:
		e.insert(0, "Invalid operation")

def button_rad():
	global conta
	conta = 1
	num = e.get()
	e.delete(0, END)
	e.insert(0, sqrt(float(num)))

def button_fat():
	global conta
	conta = 1
	num = int(float(e.get()))

	num = int(num)

	if(num > 10000):
		e.delete(0, END)
		e.insert(0, "ERROR")
		return

	fat = 1
	e.delete(0, END)
	for x in range(1, num+1, 1):
		fat = fat*x
	
	e.insert(0, fat)

def button_signal():
	num = e.get()
	e.delete(0, END)
	e.insert(0, float(num) * -1)

def button_percent():
	global conta
	conta = 1
	num = e.get()
	e.delete(0, END)
	e.insert(0, float(num)/100)

def button_clear():
	e.delete(0, END)

Button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0), fg = "black", bg = "#cfcbcf")
Button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1), fg = "black", bg = "#cfcbcf")
Button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2), fg = "black", bg = "#cfcbcf")
Button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3), fg = "black", bg = "#cfcbcf")
Button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4), fg = "black", bg = "#cfcbcf")
Button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5), fg = "black", bg = "#cfcbcf")
Button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6), fg = "black", bg = "#cfcbcf")
Button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7), fg = "black", bg = "#cfcbcf")
Button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8), fg = "black", bg = "#cfcbcf")
Button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9), fg = "black", bg = "#cfcbcf")
Button_pi = Button(root, text = "π", padx = 40, pady = 20, command = lambda: button_click(pi), fg = "black", bg = "#cfcbcf")
Button_decimal = Button(root, text=".", padx = 42, pady = 20, command = lambda: button_click('.'), fg = "black", bg = "#cfcbcf")

Button_sum = Button(root, text = "+", padx = 37, pady = 20, command = lambda: button_operator("+"), fg = "black", bg = "#a1a3e6")
Button_sub = Button(root, text = "-", padx = 40, pady = 20, command = lambda: button_operator("-"), fg = "black", bg = "#a1a3e6")
Button_mul = Button(root, text = "*", padx = 39, pady = 20, command = lambda: button_operator("*"), fg = "black", bg = "#a1a3e6")
Button_div = Button(root, text = "/", padx = 40, pady = 20, command = lambda: button_operator("/"), fg = "black", bg = "#a1a3e6")
Button_exp = Button(root, text = "x^y", padx = 29, pady = 20, command = lambda: button_operator("^"), fg = "black", bg = "#e7ad6f")
Button_rad = Button(root, text = "√", padx = 40, pady = 20, command = button_rad, fg = "black", bg = "#e7ad6f")
Button_fat = Button(root, text = "x!", padx = 38, pady = 20, command = button_fat, fg = "black", bg = "#e7ad6f")
Button_percent = Button(root, text = "%", padx = 38, pady = 20, command = button_percent, fg = "black", bg = "#e7ad6f")
Button_signal = Button(root, text = "+/-", padx = 35, pady = 20, command = button_signal, fg = "black", bg = "#e7afdd")
Button_clear = Button(root, text = "C", padx = 40, pady = 20, command = button_clear, fg = "black", bg = "#f17564")
Button_equal = Button(root, text = "=", padx = 86, pady = 20, command = button_equal, fg = "black", bg = "#6deea0")

Button0.grid(row = 4, column = 0)
Button1.grid(row = 3, column = 0)
Button2.grid(row = 3, column = 1)
Button3.grid(row = 3, column = 2)
Button4.grid(row = 2, column = 0)
Button5.grid(row = 2, column = 1)
Button6.grid(row = 2, column = 2)
Button7.grid(row = 1, column = 0)
Button8.grid(row = 1, column = 1)
Button9.grid(row = 1, column = 2)
Button_decimal.grid(row = 4, column = 1)
Button_pi.grid(row = 4, column = 2)

Button_sum.grid(row = 4, column = 3)
Button_sub.grid(row = 3, column = 3)
Button_mul.grid(row = 2, column = 3)
Button_div.grid(row = 1, column = 3)
Button_rad.grid(row = 5, column = 2)
Button_exp.grid(row = 5, column = 3)
Button_fat.grid(row = 5, column = 0)
Button_percent.grid(row = 5, column = 1)
Button_signal.grid(row = 6, column = 0)
Button_clear.grid(row = 6, column = 1)
Button_equal.grid(row = 6, column = 2, columnspan = 2)

root.mainloop()
