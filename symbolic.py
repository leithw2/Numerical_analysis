import sympy as sym


x = sym.Symbol('x')
y = sym.Symbol('y')

z= sym.expand((x + y)**4)
a = x/z
print a
