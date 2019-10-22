#!/usr/bin/env python

import sympy as sym
import numpy as np
import math
from pylab import *
import matplotlib as plt

xdata = []
ydata = []

def neville(xdata, ydata,   x):

    n = len(xdata)
    p = np.zeros((n,n))
    i=0
    j=n-1

    return recu(x ,i ,j ,p )

def recu(x ,i ,j ,p ):

    global xdata
    global ydata

    n=len(xdata)-1
    if i == j:

        print ("j = " + str(j)+ " " + "i = " + str(i))
        print ("" + str(ydata[j]))
        return ydata[j]

    else:
        first = (x - xdata[j]) * (recu(x, i, j-1, p))
        second = (x - xdata[i]) * (recu(x, i+1, j, p))
        down = (xdata[i]-xdata[j])

        res = (first - second) / down

        print ("j = " + str(j)+ " " + "i = " + str(i))
        print (sym.simplify(res))

    return res

def main():
    global xdata
    global ydata

    data = np.array([ [-1.0, e**(-1)],
		              [0.0, e**(0)],
		              [1.0, e**(1)],
		                          ])
    data = data.transpose()
    xdata = data[0]
    ydata = data[1]
    print data
    x = sym.Symbol('x')
    poli = sym.simplify(neville(xdata, ydata ,x))
    #print sym.solve(poli,x)

    return

if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
