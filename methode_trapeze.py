"""
Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode des trapèzes.

Parameters
----------
f : function
    Fonction à intégrer.
a : int
    Valeur minimale de l'intervalle.
b : int
    Valeur maximale de l'intervalle.
n : int
    Nombre de trapèzes à utiliser dans la méthode.

Returns
-------
float
    La valeur de l'intégrale calculée.

"""
from math import log, sqrt

fonction = lambda x: log(x)/x

def trapeze(f, a, b, n):
    h = (b-a)/n
    I = 0
    for i in range(1, n):
        I += f(a + i*h)
    return (f(a) + f(b))/2 * h + I * h

print(trapeze(fonction, 1, 2, 10))