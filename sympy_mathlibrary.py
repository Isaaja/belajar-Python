from sympy import *

x, y = symbols('x y')
pers1 = Eq(x + y, 6)
pers2 = Eq(x + 2 * y, -1)
solusi = solve((pers1, pers2), (x, y))
print(solusi)
