import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

x = [[1/3, 1/3], [-1/3, 1/3], [1/3, -1/3], [-1/3, -1/3]]
g = [np.square(a[0]) + np.square(a[1]) for a in x]
h = [np.power(a[0], 3) + np.power(a[1], 3) for a in x]
# y = [np.sin(x), np.sin
# plt.plot(y)
# plt.show()


def f(x, y):
    return np.square(x) + np.square(y)


def chislennoe_integrirovanie_ne_gauss(f):
    int_f, err = integrate.dblquad(f, -1, 1, lambda x: -1, 1)
    print(int_f)
    return int_f


def chislennoe_integrirovanie(f):
    integral_f = 0
    for i in range(len(f)):
        integral_f += f[i]
    return integral_f
# print(chislennoe_integrirovanie(g), " and ", chislennoe_integrirovanie(h))



