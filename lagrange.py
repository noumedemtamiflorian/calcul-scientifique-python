""" 
abscices => tableau d'abscice de point connues
ordonnees => tableau d'ordonnee de point connues
abscice => abscice dont on recherche sont ordonnee

"""
def lagrange(abscices, ordonnees, abscice):
    sum = 0
    for i in range(0, len(abscices)):
        product = 1
        k = 0
        while k < len(abscices):
            if k != i:
                product *= (abscice - abscices[k]) / (abscices[i] - abscices[k])
            k = k + 1
        sum += ordonnees[i] * product
    return "abscice "+str(abscice)+" a pour ordonnee "+str(sum)