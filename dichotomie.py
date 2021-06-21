from math import log, sqrt, cos
# from scipy.integrate import quad


def f(x): return 2*x-cos(x)


def dichotomie(f, a, b, e):
    while abs(a-b) > e:
        c = (a+b)/2
        if f(c) == 0:
            return c
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return c #probleme x'existe pas au depart si abs(a-b)>3


x = dichotomie(f, 0, 0.5, pow(10, 3))
print(x, f(x))
