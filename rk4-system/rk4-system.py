#!/usr/bin/python3

eq_num = 2
init_file = "init-val.txt"
coeff_file = "coeff-val.txt"
result_file = "result.txt"
init_val = []
coeff_val = []
h
x0
y0
xn

n = int((xn - x0)/h)

def get_init_val():
	global init_val
	file = open(init_file, "r")
	line = file.read()
	init_val = int(t) for t in line.split()
	file.close()
get_init_val()
# print(init_val)

def get_coeff_val():
	global coeff_val
	file = open(coeff_file, "r")
	for i in range(eq_num):
		line = file.readline()
		coeff_val.append(int(t) for t in line.split())
get_coeff_val()
# print(coeff_val[1][1])


def func(eq):
	val = int(coeff_val[eq][0])
	for i in range(1,eq_num):
		val = val + coeff_val[eq][i]*init_val[i]
	return val
# print(func(1))

def rk4(eq):
	f = func(eq)
	k1
	k2
	k3
	k4
	y

# def export_result():