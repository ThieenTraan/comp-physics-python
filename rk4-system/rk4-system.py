#!/usr/bin/python3
import numpy

eq_num = 2

# init_file = "init-val.txt"
# coeff_file = "coeff-val.txt"
# result_file = "result.txt"

# y0
# init_val = [6, 4]

# coeff_val = []

t0 = 0
tn = 1
h = 0.5

f = []
# func.append(lambda t,y1,y2: y1 + 2*y2)
# func.append(lambda t,y1,y2: 3*y1 + 2*y2)
# function type f(t,y0,y1,...,yn)
f.append(lambda *args: -0.5*args[1])
f.append(lambda *args: 4 - 0.1*args[1] - 0.3*args[2])

n = int((tn - t0)/h)
t = numpy.arange(t0, tn+h, h)
y = []
y.append([4])
y.append([6])

print(t)
print(n)

# def get_init_val():
# 	global init_val
# 	file = open(init_file, "r")
# 	line = file.read()
# 	init_val = int(t) for t in line.split()
# 	file.close()
# get_init_val()
# # print(init_val)

# def get_coeff_val():
# 	global coeff_val
# 	file = open(coeff_file, "r")
# 	for i in range(eq_num):
# 		line = file.readline()
# 		coeff_val.append(int(t) for t in line.split())
# get_coeff_val()
# # print(coeff_val[1][1])


# f = func[eq]
# y = [init_val[eq]]
for i in range(n):
	k1 = []
	k2 = []
	k3 = []
	k4 = []
	for j in range(2):
		arg = [t[i], y[0][i], y[1][i]]
		# k1.append(h*f[j](t[i], y[0][i], y[1][i]))
		k1.append(h*f[j](*arg))
	for j in range(2):
		k2.append(h*f[0](t[i] + h/2, y[0][i] + k1[0]/2, y[1][i] + k1[1]/2))
	for j in range(2):
		k3.append(h*f[j](t[i] + h/2, y[0][i] + k2[0]/2, y[1][i] + k2[1]/2))
	for j in range(2):
		k4.append(h*f[j](t[i] + h, y[0][i] + k3[0], y[1][i] + k3[1]))
	y[0].append(y[0][i] + 1/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]))
	y[1].append(y[1][i] + 1/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]))

print(y[0])
print(y[1])

# def export_result():