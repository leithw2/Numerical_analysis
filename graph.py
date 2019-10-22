#!/usr/bin/env python

import sympy as sym
import numpy as np
import math
from pylab import *
import matplotlib as plt
#from mpmath import *

def main():
    yAxis=[]
    graphRange = arange(0, 1, .01)

    for x in arange(0, 1, .01):
        #yAxis.append(2.7182**x)

        y = exp(1)**(x**2)
        yAxis.append(y)
        print (y)

        '''
        for x in graphRange:
            #print x
            yAxis.append(neville(xdata, ydata ,x))

        '''

    print len(yAxis)


    plot(graphRange,yAxis)
    show()


if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
