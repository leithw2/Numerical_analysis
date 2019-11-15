#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy

def rungeKutta_g4_EDO(F_x_y,x , y_1 , y_2 , ti, h):

	F_x_y = F_x_y
	ti = []
	wi = []

	ti.append(x)
	tf	  = 2

	h 	  = h
	wi.append(np.matrix([[y_1],[y_2]]))
	k=0

	for i in np.arange(ti[0], tf, h):
		k+=1
		f = evaluarFuncion(F_x_y,ti[k-1],wi[k-1])
		k1 = h*f
		#print("k1 =", k1)
		f = evaluarFuncion(F_x_y,ti[k-1] + h/2,wi[k-1] + k1/2)
		k2 =h*f
		#print(wi[k-1] + k1/2)
		f = evaluarFuncion(F_x_y,ti[k-1]+h/2,wi[k-1]+k2/2)
		#print("k3 =",f)
		k3 =h*f
		f = evaluarFuncion(F_x_y,ti[k-1]+h,wi[k-1]+k3)
		#print("k4 =",f)
		k4 =h*f
		w = wi[k-1] + 1/6*(k1+2*k2+2*k3+k4)
		print(w)
		wi.append(w)
		ti.append(ti[0]+i+h)

	sRH_4 = ti ,wi
	sRH_4 = np.array(sRH_4).T
	return (sRH_4)

def evaluarFuncion(F_x_y, _x , _y,):
	x , y1, y2 = sympy.symbols('x y1 y2')
	#print(F_x_y.item(0))
	#print(F_x_y.item(1))
	f_eva1 = F_x_y.item(0).subs(y2,_y.item(1))
	f_eva2 = F_x_y.item(1).subs(x,_x).subs(y1,_y[0])


	return (np.matrix([[f_eva1],[f_eva2]]))

def main():
	x , y1, y2 = sympy.symbols('x y1 y2')

	F_x_y = np.matrix([[y2],[(-0.1 * y1)-x]])
	#---- Initial conditions -----
	y_1   =  0.0
	y_2   =  1.0
	h     =  0.25		# increment
	x_i = 0
	ti=0
	#-----------------------------

	print (F_x_y)
	sRH_4  = rungeKutta_g4_EDO(F_x_y,x_i, y_1 , y_2 , ti, h)



if __name__ == "__main__":
	print("Solucionando Ecuacion Diferencial --- Starting...\n\n")
	try:
		main()
	except ValueError:
		print (ValueError)
	pass
