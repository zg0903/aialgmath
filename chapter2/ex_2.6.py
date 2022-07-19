import sympy
from sympy import oo
import numpy as np

x = sympy.Symbol('X')
f = (x ** 2 - 1) / (x - 1)
limit = sympy.limit(f, x, 1)
print(limit)
