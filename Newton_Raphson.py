#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym
from derivate import *

def main():

    x = sym.Symbol('x')
    f_x = -x**2+ 1
    print (f_x)
    x_k = 3
    h = 1

    dx_dy = d_central(f_x, x_k, h)
    x_k_p1 = x_k - ( f_x.subs(x,x_k) / dx_dy )
    x_k = x_k_p1
    print (x_k.evalf())

    dx_dy = d_central(f_x, x_k, h)
    x_k_p1 = x_k - ( f_x.subs(x,x_k) / dx_dy )
    x_k = x_k_p1
    print (x_k.evalf())

    dx_dy = d_central(f_x, x_k, h)
    x_k_p1 = x_k - ( f_x.subs(x,x_k) / dx_dy )
    x_k = x_k_p1
    print (x_k.evalf())

    dx_dy = d_central(f_x, x_k, h)
    x_k_p1 = x_k - ( f_x.subs(x,x_k) / dx_dy )
    x_k = x_k_p1
    print (x_k.evalf())

    dx_dy = d_central(f_x, x_k, h)
    x_k_p1 = x_k - ( f_x.subs(x,x_k) / dx_dy )
    x_k = x_k_p1
    print (x_k.evalf())

    graf_start = -10
    graf_finish = 10
    incre = 0.1
    x_y = np.zeros(( int((graf_finish-graf_start)/incre+1), 3))
    i = 0
    for j in np.arange(graf_start, graf_finish+incre, incre):
        x_y[i,0] = j
        x_y[i,1] = f_x.subs(x, j)
        x_y[i,2] = dx_dy * j + f_x.subs(x, x_k) - dx_dy * x_k
        i += 1

    plt.plot(x_y[:,0],x_y[:,1])
    plt.plot(x_y[:,0],x_y[:,2])
    plt.grid()
    plt.show()
'''
if __name__ == "__main__":
    print("Diferenciation --- Starting...\n\n")
    try:
        main()
    except ValueError:
        print (ValueError)
    pass
'''
