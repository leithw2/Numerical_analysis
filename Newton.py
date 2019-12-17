#!/usr/bin/env python

import sympy as sym
import numpy as np
import math
from pylab import *
import matplotlib as plt

xdata = []
ydata = []

def newtonInterpol(xdata, ydata,   x):

    n = len(xdata)
    p = np.zeros((n,n))
    i = 0
    j = n-1
    return recu(x ,i ,j ,p )

def recu(x ,i ,j ,p ):

    global xdata
    global ydata

    n=len(xdata)-1
    if j == i:
        p[i][j] = ydata[i]
        return ydata[i]

    else:

        first = recu(x, i+1, j, p)
        second = recu(x, i, j-1, p)
        down = (xdata[j]-xdata[i])
        res = (first - second) / down
        p[i][j] = res
    print (p)
    return res
'''
def main():
    global xdata
    global ydata

    data = np.array([ [1.0, 6],
		              [2.0, 9],
		              [3.0, 2],
		              [4.0, 5],
		                          ])
    data = data.transpose()
    xdata = data[0]
    ydata = data[1]
    print data
    x = sym.Symbol('x')
    newton(xdata, ydata ,x)
    return

if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
'''
