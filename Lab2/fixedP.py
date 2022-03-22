# Radebe, Bisection Method
import matplotlib.pyplot as plt
import numpy as np


# Given function f(x)
def f(x):
	return np.arcsin(x) - np.sqrt(x)


# Function x = g(x), to iterate on
def g(x):
	# return np.arcsin(x) - np.sqrt(x) + x
	return pow(np.arcsin(x), 2)


# def fixed(x, a=0.74, b=0.8, tol=0.5e-5, N=100):
#     i = 1
#     while i <= N:
#         p = g(x)
#         #    print(f(p) < tol)

#         if np.abs(p-x) < tol and f(p) >= tol:
#             print(p)
#             print(f(p) > tol)
#             break
#         i += 1
#         c = p


def fixedPointIteration(x0, tol, N=100):
	# Iterate on the function g(x) N times until the root is found,
	# where Xn+1 = g(Xn), the function f(x) and g(x) intersect at point f(root)
	i = 1
	flag = 1
	condition = True

	while condition:
		x_1 = g(x0)
		print('Iteration-%d, x_1 = %0.6f and f(x_1) = %0.6f' % (i, x_1, f(x_1)))
		x0 = x_1

		i = i + 1

		if i > N:
			flag=0
			break

		condition = abs(f(x_1)) < tol

	if flag==1:
	    print('\nRoot found')
	    return x_1
	else:
	    print('\nThe function is not Convergent.')


def main():
	a = 0.74
	b = 0.8
	x0 = (a+b) / 2
	tol = 0.5e-5

	root = fixedPointIteration(float(x0), tol)
	print('Root =', root)
	# print('f(root) = ', f(root))
	# print('g(root) = ', format(g(root), '3g'))



if __name__ == '__main__':
	main()
