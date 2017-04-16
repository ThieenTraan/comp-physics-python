#!/usr/bin/python3

from itertools import zip_longest
import argparse

# file structure:
# init-val has one column with one init-val per line
#
# coeff-val has n+1 columns and n rows corresponds n equations, 
# one list coefficents per one rows match t, y1, y2, y3,..., yn variable

# set function manually:
# function type: f(*args) = f(t,y0,y1,...,yn)
# notice that args[0] represent for t variable
# f.append(lambda *args: -4*args[1] + 3*args[2] + 6)
# f.append(lambda *args: -2.4*args[1] + 1.6*args[2] + 3.6)

def get_init_vals():
	global y
	global eq_num
	file = open(init_file, "r")
	line = file.read()
	for i in line.split():
		y.append([float(i)])
	file.close()
	eq_num = len(y)

def get_coeffs():
	global coeffs
	file = open(coeff_file, "r")
	for i in range(eq_num):
		line = file.readline()
		coeffs.append(list(float(t) for t in line.split()))

# contructing function from coefficents
def get_linear_eq():
	global f
	for i in range(eq_num):
		f.append(lambda *args, coeff = coeffs[i]:\
		sum(m*n for (m, n) in zip_longest(args, coeff, fillvalue=1)))

def export_result():
	f = open(result_file, "w")
	line = ""
	for i in range(n+1):
		line = line + str(t[i]) + "\t"
		for j in range(eq_num):
			line = line + str(y[j][i]) + "\t"
		line = line + "\n"
	f.write(line)
	f.close()

def solve_system():	
	# print(eq_num)
	# i is rk4 step index
	# j is K[1..4] index
	# k is y index
	for i in range(n):
		K1 = []
		K2 = []
		K3 = []
		K4 = []
		for j in range(eq_num):
			arg = [t[i]]
			for k in range(eq_num):
				arg.append(y[k][i])
			K1.append(h*f[j](*arg))
		for j in range(eq_num):
			arg = [t[i] + h/2]
			for k in range(eq_num):
				arg.append(y[k][i] + K1[k]/2)
			K2.append(h*f[j](*arg))
		for j in range(eq_num):
			arg = [t[i] + h/2]
			for k in range(eq_num):
				arg.append(y[k][i] + K2[k]/2)
			K3.append(h*f[j](*arg))
		for j in range(eq_num):
			arg = [t[i] + h]
			for k in range(eq_num):
				arg.append(y[k][i] + K3[k])
			K4.append(h*f[j](*arg))
		for k in range(eq_num):
			y[k].append(y[k][i] + 1/6*(K1[k] + 2*K2[k] + 2*K3[k] + K4[k]))
	
parser = argparse.ArgumentParser(description='Solve ODE system by RK4 method')
parser.add_argument('--init', required=True, help='Init-vals filename')
parser.add_argument('--coef', required=True, help='Coefficent-filename')
parser.add_argument('--res', default='result.txt', help='Result filename')
parser.add_argument('--t0', type=int, default=0, help='Begin values')
parser.add_argument('--tn', type=int, required=True, help='End values')
parser.add_argument('--step', type=int, default=0.25, help='Step h')
args = parser.parse_args()

init_file = args.init
coeff_file = args.coef
result_file = args.res
t0 = args.t0
tn = args.tn
h = args.step

f = []
n = int((tn - t0)/h)
t = [t0+i*h for i in range(n+1)]
y = []
coeffs = []
eq_num = 0

get_init_vals()
get_coeffs()
get_linear_eq()
solve_system()
export_result()