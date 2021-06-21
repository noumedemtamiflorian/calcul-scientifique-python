from math import log, sqrt
# from scipy.integrate import quad


fonction = lambda x: log(x)/x


def rectangle(f, a, b, n):
    h = (b-a)/n
    I = f(a)
    for i in range(1, n):
        I = I + f(a+i*h)
    I = I*h
    return I


print(rectangle(fonction, 1, 2, 10))
