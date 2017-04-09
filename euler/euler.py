#!/usr/bin/python3
import math

x0 = 0
y0 = 0
xn = 5
h = 0.5
n = int((xn - x0)/h)
y = [y0]
x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]

def func(x,y):
	return math.sin(x)

for i in range(n):
	y.append(y[i] + h*func(x[i],y[i]))

data_result = open("result.txt", "w")
for i in range(n+1):
	data_result.write("{0:3}    {1:.4f}\n".format(x[i], y[i]))
data_result.close()
