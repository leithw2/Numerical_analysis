#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym
from mpmath import *
import matplotlib as plt
from pylab import *

yAxis = ([],[])

def IrapezoidalIntegral(f_x,less_limit,high_limit,divitions):
    f_x=f_x
    a = less_limit
    b = high_limit
    m = divitions
    h = (b-a)
    h2 = h/m
    valueIntegral = 0

    global yAxis

    x = sym.Symbol('x')

    yAxis[1].append(f_x.subs(x,a))
    yAxis[0].append(a)

    valueIntegral += f_x.subs(x,a)


    for i in range(1,m):
        valueX = h2*i + a

        yAxis[1].append(f_x.subs(x,valueX))
        valueIntegral += 2*f_x.subs(x,valueX)
        yAxis[0].append(h2*i+a)

        print (f_x.subs(x,valueX))#.subs(x,valueX))

    yAxis[1].append(f_x.subs(x,b))
    valueIntegral += f_x.subs(x,b)
    yAxis[0].append(b)

    valueIntegral = h2 / 2 *valueIntegral
    return valueIntegral

def main():
	#----------------------

    x = sym.Symbol('x')

    ex = sym.Symbol('e')
    #f_x = e**x**2
    f_x = (e**x)/x
    print(f_x)
    less_limit = 2
    high_limit = 4
    divitions = 50

	#----------------------
    valueIntegral = IrapezoidalIntegral(f_x,less_limit,high_limit,divitions)
    print (valueIntegral)
    print (yAxis)

    func=[]
    graphRange = arange(2, 4.01, .01)

    for k in arange(2, 4.01, .01):
        #yAxis.append(2.7182**x)

        func.append((exp(1)**k)/k)


        '''
        for x in graphRange:
            #print x
            yAxis.append(neville(xdata, ydata ,x))

        '''

    #yAxis.traspose()
    plot(graphRange, func)
    plot(yAxis[0], yAxis[1])

    show()



if __name__ == "__main__":
	print("Intergal Trapezoid --- Starting...\n\n")
	try:
		main()
	except ValueError:
		print (ValueError)
	pass
