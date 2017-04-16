#!/usr/bin/python3

# define number of euations
eq_num = 2

# file structure:
# init-val has one column with one init-val per line
#
# coeff-val has n+1 columns and n rows corresponds n equations, 
# one list coefficents per one rows match t, y1, y2, y3,..., yn variable

init_file = "init-val.txt"
coeff_file = "coeff-val.txt"
result_file = "result.txt"
coeffs = []

t0 = 0
tn = 5
h = 0.25
f = []

# set function manually:
# function type: f(*args) = f(t,y0,y1,...,yn)
# notice that args[0] represent for t variable
# f.append(lambda *args: -4*args[1] + 3*args[2] + 6)
# f.append(lambda *args: -2.4*args[1] + 1.6*args[2] + 3.6)

n = int((tn - t0)/h)
t = [t0+i*h for i in range(n+1)] 
y = [[0], [0]]


def get_init_vals():
	global y
	file = open(init_file, "r")
	line = file.read()
	y = list(int(i) for i in line.split())
	file.close()

def get_coeffs():
	global coeffs
	file = open(coeff_file, "r")
	for i in range(eq_num):
		line = file.readline()
		coeffs.append(list(int(t) for t in line.split()))

# contructing function from coefficents
def get_linear_eq():
	global f
	for i in range(eq_num):
		f.append(lambda *args, coeff = coeffs[i]: sum(m*n for (m, n) in zip(args, coeff)))

# i is rk4 step index
# j is k[1..4] index
# k is y index
# for i in range(n):
# 	k1 = []
# 	k2 = []
# 	k3 = []
# 	k4 = []
# 	for j in range(eq_num):
# 		arg = [t[i]]
# 		for k in range(eq_num):
# 			arg.append(y[k][i])
# 		k1.append(h*f[j](*arg))
# 	for j in range(2):
# 		arg = [t[i] + h/2]
# 		for k in range(eq_num):
# 			arg.append(y[k][i] + k1[k]/2)
# 		k2.append(h*f[j](*arg))
# 	for j in range(2):
# 		arg = [t[i] + h/2]
# 		for k in range(eq_num):
# 			arg.append(y[k][i] + k2[k]/2)
# 		k3.append(h*f[j](*arg))
# 	for j in range(2):
# 		arg = [t[i] + h]
# 		for k in range(eq_num):
# 			arg.append(y[k][i] + k3[k])
# 		k4.append(h*f[j](*arg))
# 	for k in range(eq_num):
# 		y[k].append(y[k][i] + 1/6*(k1[k] + 2*k2[k] + 2*k3[k] + k4[k]))

# for i in range(eq_num):
# 	print(*init_vals[i], sep="\t")

def export_result():
	f = open("result-file.txt", "w")
	line = ""
	for i in range(n):
		line = line + str(t[i]) + " "
		for j in rang(n):
			line = line + str(y[j][i]) + " " + "\n"
	f.write(line)
	f.close()

# export_result()