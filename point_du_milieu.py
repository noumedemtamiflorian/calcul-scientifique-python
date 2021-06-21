from math import log, sqrt

fonction = lambda x: log(x)/x

def point_du_millieu(f, a, b, n):
    h = (b-a)/n
    x0 = a + h/2
    I = f(x0)
    for i in range(1, n):
        I = I + f(a + i * h + h/2)
    I = I*h
    return I


print(point_du_millieu(fonction, 1, 2, 10))
