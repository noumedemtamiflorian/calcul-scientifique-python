from math import log, sqrt


fonction = lambda x: log(x)/x


def simpson(f, a, b, n):
    h = (b-a)/n
    I = f(a)+f(a+(n-1)*h)
    print(a+n*h)
    for i in range(1, n):
        if i % 2 == 0:
            I = I + 2*f(a + i * h)
        else:
            print(a + i * h)
            I = I + 4*f(a + i * h)
    I = I*(h/3)
    return I


print(simpson(fonction, 1, 2, 10))
