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

def funct(x):
    return (pow(x,3)-13*pow(x,2)+69*x-92)*(1/5)

print(funct(1), funct(3), funct(4), funct(6))
