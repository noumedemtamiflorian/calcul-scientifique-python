## Calcul scientifique : approche de fonction en python

### Dichotomie

#### function_to_find_root

A function that takes an input x and returns 2*x-cos(x)

* Parameters:
  * x (float): The input value
* Returns:
  * float: 2*x-cos(x)

#### dichotomie

A function that finds the root of a given function using bisection method.

* Parameters:
  * function_to_find_root (function): The function for which the root needs to be found.
  * left_interval (float): The left end of the interval in which the root is supposed to be.
  * right_interval (float): The right end of the interval in which the root is supposed to be.
  * tolerance (float): The desired precision of the root approximation.
  * max_iterations (int): The maximum number of iterations to perform before giving up.
* Returns:
  > tuple: A tuple containing the root of the function and the value of the function at that root.
  >

### index

#### optimised_lagrange

Calcule et retourne le résultat de l'algorithme de Lagrange pour un abscice donné.

* Parameters
  * abscices : list
    > Liste des abscices.
    >
  * ordonnees : list
    > Liste des ordonnées.
    >
  * abscice : int
    > Valeur de l'abscice à laquelle on veut trouver l'ordonnée correspondante.
    >
* Returns
  > str, Une chaîne de caractères contenant le résultat de l'algorithme de Lagrange.
  >

### lagrange

#### optimised_lagrange

Calcule et retourne le résultat de l'algorithme de Lagrange pour un abscice donné.

* Parameters

  * abscices : list
    > Liste des abscices.
    >
  * ordonnees : list
    > Liste des ordonnées.
    >
  * abscice : int
    > Valeur de l'abscice à laquelle on veut trouver l'ordonnée correspondante.
    >
* Returns

  > str, Une chaîne de caractères contenant le résultat de l'algorithme de Lagrange.
  >

### methode_des_rectangles

#### rectangle

Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode des rectangles.

* Parameters
  * f : function
    > Fonction à intégrer.
    >
  * a : int
    > Valeur minimale de l'intervalle.
    >
  * b : int
    > Valeur maximale de l'intervalle.
    >
  * n : int
    > Nombre de rectangles à utiliser dans la méthode.
    >
* Returns
  * float
    > La valeur de l'intégrale calculée.
    >

### methode_trapeze

#### trapeze

Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode des trapèzes.

* Parameters
  * f : function
    > Fonction à intégrer.
    >
  * a : int
    > Valeur minimale de l'intervalle.
    >
  * b : int
    > Valeur maximale de l'intervalle.
    >
  * n : int
    > Nombre de trapèzes à utiliser dans la méthode.
    >
* Returns
  * float
    > La valeur de l'intégrale calculée.
    >

### point_du_milieu

#### point_du_millieu

Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode du point du milieu.

* Parameters
  * f : function

    > Fonction à intégrer.
    >
  * a : int

    > Valeur minimale de l'intervalle.
    >
  * b : int

    > Valeur maximale de l'intervalle.
    >
  * n : int

    > Nombre de points à utiliser dans la méthode.
    >
* Returns
  * float

    > La valeur de l'intégrale calculée.
    >

### simpson

#### simpson

> Calcule et retourne le résultat de l'intégrale d'une fonction sur un intervalle donné en utilisant la méthode de Simpson

Parameters

* f : function

  > Fonction à intégrer.
  >
* a : int

  > Valeur minimale de l'intervalle.
  >
* b : int

  > Valeur maximale de l'intervalle.
  >
* n : int

  > Nombre de points à utiliser dans la méthode.
  >

Returns

* float

  > La valeur de l'intégrale calculée.
  >
