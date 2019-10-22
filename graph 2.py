#!/usr/bin/env python

import sympy as sym
import numpy as np
import math
from pylab import *
import matplotlib as plt




def main():
    yAxis=[]
    graphRange = arange(0, 6, .1)

    for x in arange(0, 6, .1):
        #yAxis.append(2.7182**x)

        yAxis.append(-0.008819*x**5 + 0.1332*x**4 - 0.7052*x**3 + 1.525*x**2 - 1.107*x)
        '''
        for x in graphRange:
            #print x
            yAxis.append(neville(xdata, ydata ,x))

        '''

    print len(yAxis)

    plot(graphRange,yAxis)
    plot(graphRange,yAxis)
    show()


if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
