"""
Calcule et retourne le résultat de l'algorithme de Lagrange pour un abscice donné.

Parameters
----------
abscices : list
    Liste des abscices.
ordonnees : list
    Liste des ordonnées.
abscice : int
    Valeur de l'abscice à laquelle on veut trouver l'ordonnée correspondante.

Returns
-------
str
    Une chaîne de caractères contenant le résultat de l'algorithme de Lagrange.

"""
def optimised_lagrange(abscices, ordonnees, abscice):
    sum = 0
    for i in range(0, len(abscices)):
        product = 1
        for k in range(len(abscices)):
            if k != i:
                product *= (abscice - abscices[k]) / (abscices[i] - abscices[k])
        sum += ordonnees[i] * product
    return f"abscice {abscice} a pour ordonnee {sum}"
