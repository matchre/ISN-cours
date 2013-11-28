##################
Quelques exercices
##################

Exercices sur les boucles et tests
==================================


* Ecrire un programme qui affiche les 25 premiers éléments de la suite
  de Fibonacci (F(0)=1, F(1)=1, F(n+2)=F(n+1)+F(n)) ::

    n2=0
    n1=1
    n0=0
    for i in range(2,25):
        n2=n1+n0
        n0=n1
        n1=n2
        print n2


* Ecrire un programme qui affiche les tables d'addition et de
  multiplication.

* Ecrire un programme (sans intéraction avec l'utilisateur) qui retrouve
  un nombre par dichotomie à l'intérieur d'un intervalle.


* Ecrire un programme qui trie de manière décroissante une liste de
  nombre par la méthode du tri à bulle (on parcourt la liste des
  nombres, si un nombre est plus petit que le suivant, on inverse leur
  position. Quand on arrive à la fin de la liste, on recommence -
  sachant qu'on peut n'aller que jusqu'au rang n-1 puisque le dernier
  élément de la liste est forcément le plus petit de tous)


* Ecrire un programme qui trouve tous les nombres premiers inférieurs
  à une certaine valeur en utilisant le crible d'Eratosthene.


Correction des exos
===================

