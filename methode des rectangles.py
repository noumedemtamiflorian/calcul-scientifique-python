"""
Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode des rectangles.

Parameters
----------
f : function
    Fonction à intégrer.
a : int
    Valeur minimale de l'intervalle.
b : int
    Valeur maximale de l'intervalle.
n : int
    Nombre de rectangles à utiliser dans la méthode.

Returns
-------
float
    La valeur de l'intégrale calculée.

"""
from math import log, sqrt

fonction = lambda x: log(x)/x

def rectangle(f, a, b, n):
    h = (b-a)/n
    I = 0
    for i in range(n):
        I += f(a + i*h)
    return I * h

print(rectangle(fonction, 1, 2, 10))