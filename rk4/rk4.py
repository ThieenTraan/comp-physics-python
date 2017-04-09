#!/usr/bin/python3
import math
import numpy

def func(x,y):
	return 3*x + 2*y

x0 = 0
xn = 1
h = 0.2
y0 = 4

n = int((xn-x0)/h)

y = [y0]
x = numpy.arange(x0, xn+h, h)

for i in range(n):
	k1 = h*func(x[i], y[i])
	k2 = h*func(x[i] + h/2, y[i] + k1/2)
	k3 = h*func(x[i] + h/2, y[i] + k2/2)
	k4 = h*func(x[i] + h, y[i] + k3)
	y.append(y[i] + 1/6*(k1 + 2*k2 + 2*k3 + k4))

print(y)
# data_result = open("result.txt", "w")
# for i in range(n+1):
# 	data_result.write("{0:3}    {1:.4f}\n".format(x[i], y[i]))
# data_result.close()