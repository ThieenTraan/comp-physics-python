#!/usr/bin/python3
import math
# import numpy

def func(x,y):
	return math.sin(x)

x0 = 0
xn = 5
h = 0.5
y0 = 0

l1 = 0.5
l2 = 1 - l1
l3 = 1/(2*l2)
n = int((xn-x0)/h)

y = [y0]
x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]

for i in range(n):
	k1 = h*func(x[i], y[i])
	k2 = h*func(x[i] + l3*h, y[i] + l3*k1)
	y.append(y[i] + l1*k1 + l2*k2)

data_result = open("result.txt", "w")
for i in range(n+1):
	data_result.write("{0:3}    {1:.4f}\n".format(x[i], y[i]))
data_result.close()