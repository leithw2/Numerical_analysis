#!/usr/bin/env python

import sympy as sym
import numpy as np
import math
from pylab import *
import matplotlib as plt
#from mpmath import *

def main():
    yAxis=[]
    graphRange = arange(-10, 21, .1)

    for x in arange(-10, 21, .1):
        #yAxis.append(2.7182**x)

        #y = exp(1)**(x**2)
        y = x - sym.tan(x)
        #y = x**3 - 10*x**2 + 5

        yAxis.append(y)
        print (y)

        '''
        for x in graphRange:
            #print x
            yAxis.append(neville(xdata, ydata ,x))

        '''

    print len(yAxis)


    plot(graphRange,yAxis)
    plot(0.0, 0, color='red', marker='o',
            linestyle='None', markersize=6)
    grid()
    show()


if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
