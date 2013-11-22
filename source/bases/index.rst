###################
Les bases du python
###################

Ecrire un programme
===================

Utiliser l'interpréteur python
------------------------------

Un programme en python peut s'écrire en mode intéractif (comme pour
une calculatrice : les lignes sont exécutées au fur et à mesure qu'on
les tape). On lance, dans une console, le programme ``python`` (ou
bien ``ipython`` pour avoir de la couleur et quelques fonctionnalités
utiles en plus)::

  $ python

et on peut se servir du python comme d'une calculatrice.

>>> 1+1  # Addition
2
>>> 5*2  # Multiplication
10


Mais le mode intéractif est vite limité lorsqu'on veut écrire des
programmes un peu complexes. Dans ce cas, on tape le programme en
python dans un fichier texte, que l'on enregistre avec l'extension .py
caractéristique des fichiers source python.

On exécute alors le programme en appelant (via la console) ``python``
suivi du nom du programme ::

  $ python monprogramme.py

Attention, le programme doit se trouver dans le répertoire courant
(pour vérifier quel est le répertoire courant, utiliser l'instruction
``pwd`` dans la console, ``cd`` pour changer de répertoire).

Si le programme n'est pas dans le répertoire courant, on peut
l'appeler en précisant soit le chemin complet, soit le chemin
relatif::

  $ python ../../chemin/vers/le/fichier.py
  $ python /home/isn/chemin/vers/le/fichier.py

La syntaxe d'un programme python
--------------------------------

Tous les caractères situés derrière un # et jusqu'à la fin de la ligne
sont des commentaires, ils ne sont pas exécutés.

Si le programme contient (dans les commentaires, ou dans des chaînes
de caractère) au moins un caractère non ascii (accents, symboles,...),
il faut débuter le programme par un commentaire "spécial" indiquant
que l'encodage du programme n'est pas en ASCII. Nous utiliserons
systématiquement l'UTF-8 ::

  # -*- coding: utf-8 -*-

En revanche, les noms de variables, fonctions et de manière générale
toutes les "instructions" ne doivent comporter que des caractères
ascii.

Les espaces sont très importants, surtout en début de ligne : c'est
par l'indentation (décalage en début de ligne) que le code python est
structuré. Chaque niveau de code imbriqué doit être décalé de 4
caractères par rapport au niveau supérieur.

De manière générale, la *lisibilité* du code est très importante, et
permet de faire moins d'erreurs ou de repérer plus facilement les
éventuelles erreurs. Un recueil des bonnes pratiques est disponibles
sur le site de python : la PEP 8 (en anglais) :
http://www.python.org/dev/peps/pep-0008/ écrite par le créateur du
langage python, Guido van Rossum.

Les quelques points importants :

- indentation : 4 espaces (pas de tabulations)
- pas de lignes trop longues : 79 caractères maximum par ligne
- espacement des mots et symboles :
  
  * pas d'espace après/avant les parenthèses, accolades, crochets
  
  * espaces uniquement après les virgules, point-virgules ou deux
    points

Les types de base
=================

Texte repris et traduit du tutoriel python officiel :
http://docs.python.org/2/tutorial/introduction.html 

Les nombres
-----------

Python effectue des opérations : ``+``, ``-``, ``*``, ``/``, ``(``,
``)`` fonctionnent comme sur les calculatrices, à un petit détail près
: si aucun nombre ne comporte de virgule (un point, c'est de
l'anglais), les calculs sont faits en nombre entier (``7/3`` donne
2). En mode intéractif, cela donne :

>>> 2+2
4
>>> (50-5*6)/4
5
>>> 7/3
2
>>> 7/-3
-3

Le signe égal (``=``) est utilisé pour assigner une valeur à une
variable. Dans ce cas, en mode intéractif, aucune valeur n'est
affichée.

>>> largeur = 20
>>> hauteur = 5*9
>>> largeur * hauteur
900

Une valeur peut être assignée simultanément à plusieurs variables

>>> x = y = z = 0
>>> x
0
>>> y
0
>>> z
0

Les variables doivent être "définies" (une valeur doit leur avoir été
assigné) avant de pouvoir être utilisées, sous peine de d'erreur
parlant de ``NameError``

>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

Les nombres comportant un point sont des nombres "flottants". Si un
calcul contient au moins un nombre flottant, l'ensemble du calcul est
fait en flottant

>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5

Les calculs entiers sont faits en précision "illimitée" en utilisant
des entiers "longs" (terminés par L)

>>> 1000000000*1000000000000
1000000000000000000000L

On peut passer d'un format de nombre à un autre (entier / long /
flottant) en utilisant les fonctions ``long()``, ``float()``, et
``int()``

>>> float(1000000000000000000000L)
1e+21
>>> int(1e10)
10000000000

Les chaînes de caractères
-------------------------

Ecriture des chaines de caractères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les chaînes de caractères peuvent s'écrire de différentes
manières. Elles peuvent être entourées de guillemets simples ou
doubles

>>> 'cours isn'
'cours isn'
>>> 'cours d\'isn'
"cours d'isn"
>>> "cours d'isn"
"cours d'isn"
>>> '"Tout à fait", qu\'il dit'
'"Tout à fait", dit-il'
>>> "\"Tout à fait\", qu'il dit"
'"Tout à fait", qu\'il dit'

Les chaines de caractères peuvent être écrites sur plusieurs lignes,
en terminant chaque ligne par un backslash ::

  hello = "Une longue chaîne de caractères qui contient : \n\
  des passages à la ligne \
  et des espaces."

  print hello

Le passage à la ligne dans la chaîne se fait en utilisant le \n ::

  Une longue chaîne de caractères qui contient : 
  des passages à la ligne  et des espaces.

Les espaces en début de ligne sont conservés.

On peut aussi utiliser des triples-guillemets : ``"""`` ou ``'''`` ::

  print """ Ceci est une
  longue ligne avec des
    retours à la ligne"""

produit la sortie suivante ::

  Ceci est une
  longue ligne avec des
     retours à la ligne

On peut additionner des chaines de caractères (les concaténer) avec
l'opérateur ``+``, et les multiplier (concaténer une chaîne à elle-même un
certain nombre de fois) avec l'opérateur ``*``

>>> 'To'+'To'
'ToTo'
>>> 'To'*5
'ToToToToTo'

Deux chaines successives sont automatiquement concaténées

>>> 'To' 'To'
'ToTo'

Tranches de chaines (slices)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On peut récupérer une sous partie d'une chaine en utilisant un
"slice": des indices (de position), séparés par deux points.

>>> a="AZERTYUIOP"
>>> a[2]
'E'

Les positions **sont comptées à partir de zéro** pour le premier
caractère. Le premier indice donné correspond au premier caractère
extrait (inclus), le deuxième indice donné correspond au premier
caractère non extrait (exclus).

Si un nombre n'est pas précisé, une valeur par défaut "intelligente"
est choisie (longueur de la chaine, début de la chaine, fin, ..)

Les indices négatifs indiquent qu'on compte à partir de la fin (à l'envers).

>>> a="AZERTYUIOP"
>>> a[2:4]
'ER'
>>> a[:2]
'AZ'
>>> a[2:]
'ERTYUIOP'
>>> a[-2]
'O'
>>> a[-5:-2]
'YUI'
>>> a[:-2]
'AZERTYUI'

On ne peut pas modifier un caractère à l'intérieur d'une chaîne de
caractères, il faut recopier la chaîne.

Pour plus de détails, voir
http://docs.python.org/2/tutorial/introduction.html#strings


Listes
------

Le python a un certain nombre de types "composés", utilisés pour
regrouper différentes valeurs. Un de ces types est la liste
(list). Ecrite entre crochet, la liste a ses éléments séparés par des
virgules. Comme pour les chaînes de caractères, on peut accéder à des
portions de la liste en utilisant des slices.

>>> l=[1,2,3]
>>> l
[1, 2, 3]
>>> l[1]
2
>>> l[1:]
[2, 3]
>>> l[:2]
[1, 2]
>>> l[1::-1]
[2, 1]
>>> l[::-1]
[3, 2, 1]
>>> l[::-2]
[3, 1]


Mais à la différence des chaînes de caractères, on peut aussi changer
un ou plusieurs éléments d'une liste.

>>> l[1]=9
>>> l
[1, 9, 3]

Un élément de liste peut être de n'importe quel type : nombre entier,
flottant, chaîne de caractères, voire autre liste :

>>> l[2]=['A', 'zer', 'TY']
>>> l
[1, 9, ['A', 'zer', 'TY']]

Dans le cas d'éléments imbriqués (ci-dessus par exemple : caractère
dans chaine dans liste dans liste), on peut accéder aux différents
niveaux par des [] successifs.

Exemple : je veux le 3ème élément de la liste l (['A', 'zer', 'TY']),
dans ce troisième élément je veux le deuxième élément ('zer'), dans de
deuxième élément je veux le troisième ('r').

>>> l[2][1][2]
'r'

Voir http://docs.python.org/2/tutorial/introduction.html#lists

Dictionnaires
-------------






