#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

def main():

    x = sym.Symbol('x')
    f_x = x - x**(1/3) -2
    print (f_x)
    root(f_x,3,4)
	#----------------------
def root(f_x ,a ,b):
    x = sym.Symbol('x')
    for k in range(200):

        xm = a + (b-a) / 2
        print (xm)

        if (abs(f_x.subs(x,a)) <= 0.000001):
            xm = a
            break

        if (abs(f_x.subs(x,a)) <= 0.000001):
            xm = b
            break

        if sign(f_x.subs(x,xm)) == sign(f_x.subs(x,a)):
            a = xm
        else:
            b = xm


    print ("la raiz es: " , xm, " con ",k, "iteraciones" )

def sign(f_x):

    if f_x < 0:
        return 1
    if f_x > 0:
        return -1

    if f_x == 0:
        return 0
if __name__ == "__main__":
	print("Intergal Trapezoid --- Starting...\n\n")
	try:
		main()
	except ValueError:
		print (ValueError)
	pass
