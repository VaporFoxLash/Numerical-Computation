# Radebe, Bisection Method
import numpy as np
import matplotlib.pyplot as plt


def bisectionFunc(f, a, b, tol):
    '''Take continuous function f on the interval [a,b],
    and find the root with tolerence tol
    '''
    i = 0
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # Get midpoint
    c = (a + b)/2
    i = i + 1
    
    if np.abs(f(c)) < tol:
        # found c as root
        print('Iteration-%d, c = %0.6f and f(c) = %0.6f' % (i, c, f(c)))
        return c
    elif np.sign(f(a)) == np.sign(f(c)):
        # when c is an improvement on a
        return bisectionFunc(f, c, b, tol)
    elif np.sign(f(b)) == np.sign(f(c)):
        # when c is an improvement on b
        return bisectionFunc(f, a, c, tol)

def main():
    eps = 0.5e-5
    a = 0.74
    b = 0.8

    f = lambda x: np.arcsin(x) - np.sqrt(x)


    root = bisectionFunc(f, a, b, eps)
    print("root =", root)
    print("f(c) =", f(root))


if __name__ == '__main__':
    main()