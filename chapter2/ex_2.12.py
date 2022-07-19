import sympy
from sympy import oo, diff, asin, sqrt, sin, symbols
import numpy as np
from sympy.abc import x, y, z, f

# 偏导
f = x ** 2 + 3 * x * y + y ** 2

# x 偏导
x_ = diff(f, x)

# y 偏导
y_ = diff(f, y)

x__evalf = x_.evalf(subs={x: 1, y: 2})
y__evalf = y_.evalf(subs={x: 1, y: 2})

print(x_, x__evalf)
print(y_, y__evalf)
