from math import log, sqrt


fonction = lambda x: log(x)/x


def trapeze(f, a, b, n):
    h = (b-a)/n
    I = (f(a)+f(b))/2
    for i in range(1, n):
        I = I + f(a + i*h)
    I = I*h
    return I


print(trapeze(fonction, 1, 2, 10))
