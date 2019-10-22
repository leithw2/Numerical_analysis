from scipy.interpolate import lagrange
import numpy as np

import numpy as np
import math
from pylab import *
import matplotlib as plt


#x = sym.Symbol('x')

#f_x = sym.sin(3*x)/(1+3*x)

#print (f_x.subs(x,1.2)).evalf()

ydata=[]

for i in arange(0 , 7.2, 1.2):

    ydata.append(np.sin(3*i)/(1+3*i))
    #print i

#print ydata

data = np.array([ [0.0, ydata[0]],
                  [1.2, ydata[1]],
                  [2.4, ydata[2]],
                  [3.6, ydata[3]],
                  [4.8, ydata[4]],
                  [6.0, ydata[5]],
                                ])
data = data.transpose()
print (data[0])
print (data[1])

poly = lagrange(data[0], data[1])

print poly
