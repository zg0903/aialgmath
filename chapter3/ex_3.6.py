import numpy as np
from scipy.integrate import quad

func = lambda x: np.cos(np.exp(x)) ** 2
sou = quad(func, 0, 3)
print(sou)

# 积分值 误差值
# (1.296467785724373, 1.3977971853986262e-09)