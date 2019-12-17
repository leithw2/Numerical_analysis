#!/usr/bin/env python
import numpy as np
import math
from pylab import *
import matplotlib as plt

def InterLagrange(data, val):

    nData = len(data)
    xData =[]
    yData =[]
    for x in data:

        xData.append(x[0])
        yData.append(x[1])

    return combination(val, xData, yData)

def combination(val, xData, yData):
    com = 0

    for k in range(len(xData)):
        producto = 0
        lag = 1
        for x in range(len(xData)):

            if xData[k] != xData[x]:

                lag *= (val - xData[x])/(xData[k]-xData[x])

        com += lag*yData[k]

    return com

'''
def main():

    inData = np.array([[1548,4],
               [-216, -24]])

    yAxis = []
    graphRange2 = arange(-5, 5, .1)
    for x in graphRange2:
        yAxis.append(Interpolation(inData, x))

    x = graphRange2
    print len(x)

    plot(x, yAxis)
    show()

if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
'''
