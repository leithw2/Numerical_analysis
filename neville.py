#!/usr/bin/env python

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
        #print "termina recursividad"
        #print "fondo =" + str(ydata[j])
        p[i][j] = ydata[j]
        return ydata[j]

    else:
        first = (x - xdata[j]) * (recu(x, i, j-1, p))
        second = (x - xdata[i]) * (recu(x, i+1, j, p))
        down = (xdata[i]-xdata[j])

        #print ("valor primero =") + str(first)
        #print ("valor segundo =") + str(second)
        #print ("valor abajo =") + str(down)

        res = (first - second) / down
        #print res
        p[i][j] = res
    print p
    return res

def main():
    global xdata
    global ydata

    '''
    data = np.array([[1,2],
               [2,4],
               [3,2],
               [4,5],
               [5,6]])
    '''
    '''
    data = np.array([[1.0,0.7651977],
                     [1.3,0.6200960],
                     [1.6,0.4554022],
                     [1.9,0.2818186],
                     [2.2,0.1103623]])
    '''
    data = np.array([ [4.0,-0.06604],
		              [3.9,-0.02724],
		              [3.8, 0.01282],
		              [3.7, 0.05383],
		                          ])


    data = data.transpose()

    xdata = data[0]
    ydata = data[1]
    print data

    graphRange = arange(-10, 10, .1)

    yAxis = []
    #print graphRange

    '''
    for x in graphRange:
        #print x
        yAxis.append(neville(xdata, ydata ,x))


    print yAxis
    plot(graphRange,yAxis)
    show()

    '''
    neville(xdata, ydata ,1.5)

    return


if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except ValueError:
        print ValueError
    pass
