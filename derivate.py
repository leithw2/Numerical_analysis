#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

def d_forward(f_x, x_1,h):
    x = sym.Symbol('x')
    f_x = f_x
    x_1 = x_1
    h = h
	#funcs = vars(math)

	#dx_dy =  ( eval(f_x, funcs, dict( x=x_1+h)) - eval(f_x, funcs, dict( x=x_1))) / h
    dx_dy = (f_x.subs(x, x_1 + h) - f_x.subs(x, x_1)) / h

    return dx_dy

def d_backward(f_x, x_1,h):
    x = sym.Symbol('x')
    f_x = f_x
    x_1 = x_1
    h = h

	#dx_dy =  ( eval(f_x, funcs, dict( x=x_1)) - eval(f_x, funcs, dict( x=x_1-h))) / h
    dx_dy = (f_x.subs(x, x_1) - f_x.subs(x, x_1 - h)) / h
    return dx_dy

def d_central(f_x, x_1,h):
    x = sym.Symbol('x')

    f_x = f_x
    x_1 = x_1
    h = h
    funcs = vars(math)

	#dx_dy =  ( eval(f_x, funcs, dict( x=x_1+h)) - eval(f_x, funcs, dict( x=x_1-h))) / (2*h)
    dx_dy = (f_x.subs(x, x_1 + h) - f_x.subs(x, x_1 - h)) / (2 * h)
    return dx_dy
'''
def main():

    x = sym.Symbol('x')

    f_x = x**2+2*x
    print (f_x)
    x_1 = 3
    h = 1
    dx_dy_forward	= 	d_forward(f_x, x_1, h)
    dx_dy_backward	=	d_backward(f_x, x_1, h)
    dx_dy_central 	=	d_central(f_x, x_1, h)

    print('Forward derivation:  ' , dx_dy_forward)
    print('Backward derivation: ' , dx_dy_backward)
    print('Central derivation:  ' , dx_dy_central)
	#----------------------
	# ~ valueIntegral = IrapezoidalIntegral(f_x,less_limit,high_limit,divitions)
	# ~ print (valueIntegral)

    graf_start = -10
    graf_finish = 10
    incre = 0.1
    x_y = np.zeros(( int((graf_finish-graf_start)/incre+1), 3))
    i = 0
    for j in np.arange(graf_start, graf_finish+incre, incre):
        x_y[i,0] = j
        x_y[i,1] = f_x.subs(x, j)
        x_y[i,2] = dx_dy_central * j + f_x.subs(x, x_1) - dx_dy_central * x_1
        i += 1

    plt.plot(x_y[:,0],x_y[:,1])
    plt.plot(x_y[:,0],x_y[:,2])
	# ~ plt.plot([0,1],[np.exp(0*2),np.exp(1*2)])
	# ~ plt.legend(['e^x^2','Recta del trapecio'])

    plt.show()


if __name__ == "__main__":
    print("Diferenciation --- Starting...\n\n")
    try:
        main()
    except ValueError:
        print (ValueError)
    pass
'''
