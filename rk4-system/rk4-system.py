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

func = []
# func.append(lambda y1,y2: y1 + 2*y2)
# func.append(lambda y1,y2: 3*y1 + 2*y2)
func.append(lambda y1,y2: -0.5*y1)
func.append(lambda y1,y2: 4 - 0.1*y1 - 0.3*y2)

n = int((tn - t0)/h)
t = numpy.arange(t0, tn+h, h)
y1 = [4]
y2 = [6]
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
	k1 = h*func[0](y1[i], y2[i])
	l1 = h*func[1](y1[i], y2[i])
	k2 = h*func[0](y1[i] + k1/2, y2[i] + l1/2)
	l2 = h*func[1](y1[i] + k1/2, y2[i] + l1/2)
	k3 = h*func[0](y1[i] + k2/2, y2[i] + l2/2)
	l3 = h*func[1](y1[i] + k2/2, y2[i] + l2/2)
	k4 = h*func[0](y1[i] + k3, y2[i] + l3)
	l4 = h*func[1](y1[i] + k3, y2[i] + l3)
	y1.append(y1[i] + 1/6*(k1 + 2*k2 + 2*k3 + k4))
	y2.append(y2[i] + 1/6*(k1 + 2*k2 + 2*k3 + k4))
	print(k1,k2,k3,k4)
	print(l1,l2,l3,l4)
print(y1)
print(y2)
# def export_result():