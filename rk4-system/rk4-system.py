#!/usr/bin/python3
import numpy
import pprint

# define number of euations
eq_num = 2

# init_file = "init-val.txt"
# coeff_file = "coeff-val.txt"
result_file = "result.txt"
# coeff_val = []

t0 = 0
tn = 5
h = 0.25

f = []

# function type: f(*args) = f(t,y0,y1,...,yn)
f.append(lambda *args: -4*args[1] + 3*args[2] + 6)
f.append(lambda *args: -2.4*args[1] + 1.6*args[2] + 3.6)

n = int((tn - t0)/h)
t = numpy.arange(t0, tn+h, h)
y = [[0], [0]]

print(*t,sep="\t")

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

# i is rk4 step index
# j is k[1,4] index
# k is y index
for i in range(n):
	k1 = []
	k2 = []
	k3 = []
	k4 = []
	for j in range(eq_num):
		arg = [t[i]]
		for k in range(eq_num):
			arg.append(y[k][i])
		k1.append(h*f[j](*arg))
	for j in range(2):
		arg = [t[i] + h/2]
		for k in range(eq_num):
			arg.append(y[k][i] + k1[k]/2)
		# k2.append(h*f[0](t[i] + h/2, y[0][i] + k1[0]/2, y[1][i] + k1[1]/2))
		k2.append(h*f[j](*arg))
	for j in range(2):
		arg = [t[i] + h/2]
		for k in range(eq_num):
			arg.append(y[k][i] + k2[k]/2)
		# k3.append(h*f[j](t[i] + h/2, y[0][i] + k2[0]/2, y[1][i] + k2[1]/2))
		k3.append(h*f[j](*arg))
	for j in range(2):
		arg = [t[i] + h]
		for k in range(eq_num):
			arg.append(y[k][i] + k3[k])
		# k4.append(h*f[j](t[i] + h, y[0][i] + k3[0], y[1][i] + k3[1]))
		k4.append(h*f[j](*arg))
	for k in range(eq_num):
		y[k].append(y[k][i] + 1/6*(k1[k] + 2*k2[k] + 2*k3[k] + k4[k]))

for i in range(eq_num):
	print(*y[i], sep="\t")

def export_result():
	f = open("result-file.txt", "w")
	line = ""
	for i in range(n):
		line = line + str(t[i]) + " "
		line = line + str(y[0][i]) + " " + str(y[1][i]) + "\n"
	f.write(line)
	f.close()

export_result()