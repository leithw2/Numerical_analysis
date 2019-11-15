#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

roots = []

def main():

    x = sym.Symbol('x')
    f_x = -x**2 + 1
    #f_x = sym.sin(5*x)

    print (f_x)
    level = 1
    root(f_x,-3,5,level)
    print(roots)

def root(f_x ,a ,b,level):
    global roots
    x = sym.Symbol('x')
    xm = a + (b-a) / 2
    #print ("a = " + str(a) + " b = " + str(b))
    #print("f_x = " + str(f_x.subs(x,a)))

    if (level >= 4):
        #print ("No hay raiz at " + str(xm) )
        return
    res = root(f_x,a,xm,level+1)
    if(res != None):
        roots.append(res)

    res = root(f_x,xm,b,level+1)
    if(res != None):
        roots.append(res)

    if (abs(f_x.subs(x,a)) <= 0.01):
        roots.append(a)
        #print("a = " + str(a))

        return a

    if (abs(f_x.subs(x,b)) <= 0.01):
        roots.append(b)
        #print("b = " + str(b))
        return b


    #print ("la raiz es: " , xm, " con ",level, "iteraciones" )

def sign(f_x):

    if f_x < 0:
        return 1
    if f_x > 0:
        return -1
    if f_x == 0:
        return 0

if __name__ == "__main__":
	print("Starting...\n\n")
	try:
		main()
	except ValueError:
		print (ValueError)
	pass
