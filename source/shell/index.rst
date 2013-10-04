La ligne de commande (le shell)
###############################

La ligne de commande peut paraître "désuète" face aux interfaces
"sexy" que l'on trouve aujourd'hui sur nos ordinateurs, cependant elle
reste un outil très important pour plusieurs raisons :

- elle ne demande que peu de ressources
- elle peut être utilisée en local ou sur des machines distantes
- avec un minimum d'habitude, elle est aussi rapide que le clic de
  souris
- elle peut être facilement programmée pour effectuer des tâches
  répétitives
- elle peut permettre de sauver un ordinateur quand (presque) plus
  rien ne fonctionne
- etc...

L'invite de commande est la plupart du temps de la forme ::

  utilisateur@machine:/chemin/du/repertoire/courant$

ce qui permet de savoir sur quelle machine, sous quelle identité et
dans quel répertoire on travaille

Le répertoire "home" de l'utilisateur est abrégé en ~

Trucs pratiques
===============

* complétion automatique : usez et abusez de la touche TAB qui
  complète les commandes, les noms de répertoires et de fichiers
* copier / coller : sélectionner un texte avec la souris, il est
  copié; cliquez quelque part avec le bouton du milieu (la roulette),
  il est collé


Mémento des commandes utiles
============================

Navigation et gestion des fichiers
----------------------------------

* **cd** : change directory (changement de répertoire)

  - sans rien : retourne au répertoire home de l'utilisateur

  - avec .. (cd ..) : remonte d'un niveau dans l'arborescence des répertoires

  - avec un nom de répertoire : va dans ce répertoire

  - avec - (cd -) : retourne au répertoire dans lequel vous étiez
    avant de changer

* **ls** : liste des fichiers

  - sans rien : liste simple

  - avec les options -al (ls -al) : liste complète des fichiers, avec
    les tailles, les types, les autorisations, et incluant les
    fichiers cachés (ceux qui commencent par .)

* **mkdir nomrepertoire** : crée le répertoire *nomrepertoire* dans le
  rpertoire cournt

* **rmdir nomrepertoire** : supprime le répertoire *nomrepertoire* SI
  IL EST VIDE (si il n'est pas vide, il faut le vider avant)

* **rm nomfichier** : supprime le fichier *nomfichier*

* **touch nomfichier** : crée un fichier vide appelé *nomfichier*

Réseau
------

