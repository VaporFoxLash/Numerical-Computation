# Radebe, Bisection Method
import matplotlib.pyplot as plt
import numpy as np


# Given function f(x)
def f(x):
	return np.arcsin(x) - np.sqrt(x)


# Function x = g(x), to iterate on
def g(x):
	return pow(np.arcsin(x), 2)


def fixedPointIteration(x0, tol, N):
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

		condition = abs(f(x_1)) > tol

	if flag==1:
	    print('\nRoot found')
	    return x_1
	else:
	    print('\nThe function is not Convergent.')


def main():
	x0 = 0.74
	tol = 0.5e-5
	N = 100

	root = fixedPointIteration(x0, tol, N)
	print('Root =', format(root, '3g'))
	print('f(root) = ', format(f(root), '3g'))
	print('g(root) = ', format(g(root), '3g'))
	


if __name__ == '__main__':
	main()