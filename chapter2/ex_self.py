import sympy
from sympy import oo, sin, ln, sqrt, Pow, real_root, diff, log
import numpy as np
from sympy.abc import x, y, z, f

#
# # 1)
# f = sin(ln(x))
# limit = sympy.limit(f, x, 1)
# print(limit)
#
# # 2)
# f2 = (real_root(x, 3) - 2) / (x - 8)
# limit_2 = sympy.limit(f2, x, 8)
# print(limit_2)
#
# # 3)
# f3 = x ** 4 - 2 * (x ** 3) + 5 * sin(x) + ln(3)
# diff = diff(f3)
# print(diff)

# 4)

f4 = ((3 * x * x) + (y * y)) ** ((4 * x) + (2 * y))
x_diff = diff(f4, x)
f5 = (3 * x ** 2 + y ** 2) ** (4 * x + 2 * y) * (
        6 * x * (4 * x + 2 * y) / (3 * x ** 2 + y ** 2) + 4 * log(3 * x ** 2 + y ** 2))

print(x_diff)
