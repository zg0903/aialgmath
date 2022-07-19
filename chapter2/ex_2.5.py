import sympy
from sympy import oo
import numpy as np

x = sympy.Symbol('x')
f = sympy.sin(x) / x
limit = sympy.limit(f, x, oo)

print(limit)
