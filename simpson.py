"""
Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode de Simpson.

Parameters
----------
f : function
    Fonction à intégrer.
a : int
    Valeur minimale de l'intervalle.
b : int
    Valeur maximale de l'intervalle.
n : int
    Nombre de points à utiliser dans la méthode.

Returns
-------
float
    La valeur de l'intégrale calculée.

"""
from math import log, sqrt

fonction = lambda x: log(x)/x

def simpson(f, a, b, n):
    h = (b-a)/n
    I = f(a)+f(b)
    for i in range(1, n):
        I += 2*f(a + i * h) if i % 2 == 0 else 4*f(a + i * h)
    return I * h / 3

print(simpson(fonction, 1, 2, 10))