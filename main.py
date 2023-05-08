import numpy as np
import matplotlib.pyplot as plt
# import scipy
from scipy import integrate

N = 20
T = [[0 for i in range(N)] for j in range(N)]
x0 = [i*2/N for i in range(N)]
y0 = [j*2/N for j in range(N)]



def boundary_conditions():
    for i in range(N):
        T[0][i] = 0
        T[2][i] = 0
    for j in range(N):
        T[j][0] = 0
        T[j][2] = np.sin(np.pi * j / 2)


def Tij(x, y):
    for i in range(N):
        for j in range(N):
            T[i][j] = np.sinh(np.pi * y[j] / 2) * np.sin(np.pi * x[i] / 2) / np.sinh(np.pi)
    # return np.sinh(np.pi * y / 2) * np.sin(np.pi * x / 2) / np.sinh(np.pi)


for i in range(N):
    for j in range(N):
        Tij(x0, y0)
plt.imshow(T, cmap='Greys', extent=[0, 2, 0, 2], interpolation='nearest')
plt.savefig('blkwht.png')

plt.show()

# # x = [[1/3, 1/3], [-1/3, 1/3], [1/3, -1/3], [-1/3, -1/3]]
# # g = [np.square(a[0]) + np.square(a[1]) for a in x]
# # h = [np.power(a[0], 3) + np.power(a[1], 3) for a in x]
# # y = [np.sin(x), np.sin
# # plt.plot(y)
# # plt.show()
#
#
# N = 20
#
#
# def f(x, y):
#     return np.square(x) + np.square(y)
#
#
# def chislennoe_integrirovanie_ne_gauss(f):
#     int_f, err = integrate.dblquad(f, -1, 1, lambda x: -1, 1)
#     print(int_f)
#     return int_f
#
#
# def chislennoe_integrirovanie(f):
#     integral_f = 0
#     for i in range(len(f)):
#         integral_f += f[i]
#     return integral_f
#
#
# # print(chislennoe_integrirovanie(g), " and ", chislennoe_integrirovanie(h))
#
#
# T = [[0 for i in range(N)] for j in range(N)]
# k = [[1, 2], [2, 1]]
#
#
# def boundary_conditions():
#     for i in range(N):
#         T[0][i] = np.sin(np.pi * i / 10)
#     for j in range(N):
#         T[j][0] = np.sin(np.pi * j / 10)
#
#
# ########################### Вычислим dT/dx #############################
#
# dN = [[-0.25, -0.25],
#       [0.25, -0.25],
#       [0.25, 0.25],
#       [-0.25, 0.25]]  # производные базисных векторов
#
# # расстояние между узлами элементов 1/N в глобальном смысле
# Na = [(dN[i][0]+dN[i][0])*2*N for i in range(4)]
#
# d = [[0 for i in range(N)] for j in range(N)]
# dT = [[0 for i in range(N)] for j in range(N)]
# for i in range(N):
#     for j in range(N):
#         d[i][j] = T[i][j]
#
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             dT[i][j] += Na[k]*d[i][j]  # derivative
#
# q = [0, 1]  # источник тепла


