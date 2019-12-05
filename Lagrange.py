#!/usr/bin/env python
import numpy as np
import math
from pylab import *
import matplotlib as plt

def Interpolation(data, val):

    nData = len(data)
    xData =[]
    yData =[]
    for x in data:

        xData.append(x[0])
        yData.append(x[1])


    return combination(val, xData, yData)

def combination(val, xData, yData):
    #print xData
    com = 0

    for k in range(len(xData)):
        producto = 0
        lag = 1
        for x in range(len(xData)):

            if xData[k] != xData[x]:

                lag *= (val - xData[x])/(xData[k]-xData[x])
                #print "(", val, "-", xData[x],")/"
                #print "(", xData[k], "-", xData[x],")"

        #print "--------------------------------"
        #print "lagrange = ", lag
        #print "valor de y = ", yData[k]
        #print "sumatoria = ", lag*yData[k]
        com += lag*yData[k]
    #print "combination = ", com


    return com



def main():

    #sino = arange(-5, 5, .1)

    inData = np.array([[1548,4],
               [-216, -24]])
    '''
    inData = np.array([[0,0],
               [1,1],
               [2,4]])
    '''
    #inData = []


    #for z in sino:
        #print z
        #inData.append([z ,sin(z)])


    #print inData

    #val = 20
    yAxis = []
    graphRange2 = arange(-5, 5, .1)
    for x in graphRange2:
        yAxis.append(Interpolation(inData, x))

    x = graphRange2
    #print yAxis
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
