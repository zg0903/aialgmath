import sympy
from sympy import oo
import numpy as np

x = sympy.Symbol('X')
f = sympy.sin(x) / (3 * x + x ** 2)
limit = sympy.limit(f, x, 0)
print(limit)
