#!/usr/bin/env python3
import numpy as np
from pylab import *
import matplotlib as plt
import math
import sympy as sym


def IrapezoidalIntegral(f_x,less_limit,high_limit,divitions):
    f_x=f_x
    a = less_limit
    b = high_limit
    m = divitions
    h = (b-a)
    h2 = h/m
    valueIntegral = 0
    x = sym.Symbol('x')
    for i in range(1,m):
        valueX = h2*i + a
        valueIntegral += 2*f_x.subs(x,valueX)
        print (f_x.subs(x,valueX))
    valueIntegral +=  f_x.subs(x,a) + f_x.subs(x,b)
    valueIntegral = h2 / 2 *valueIntegral
    return valueIntegral

def main():
	#----------------------

    x = sym.Symbol('x')
    f_x = 15*x**2
    less_limit = 1
    high_limit = 2
    divitions = 10
	#----------------------
    valueIntegral = IrapezoidalIntegral(f_x,less_limit,high_limit,divitions)
    print (valueIntegral)

    values=[]
    graphRange = arange(less_limit - less_limit * .1, high_limit + high_limit * .1, .1)

    for value in graphRange:
        values.append(f_x.subs(x,value))

    plot(values,graphRange)
    show()

if __name__ == "__main__":
	print("Intergal Trapezoid --- Starting...\n\n")
	try:
		main()
	except ValueError:
		print (ValueError)
	pass
