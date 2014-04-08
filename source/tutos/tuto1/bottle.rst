Mon premier serveur web
#######################


Etape 0 : clonage du dépôt du projet
====================================

Nous allons commencer par cloner le dépôt du projet. Dans un terminal,
tapez la commande suivante

.. code-block:: bash

  $ git clone https://github.com/jmbarbier/ISNTutoBottle.git

Cette commande va cloner le dépôt ISNTutoBottle.git situé sur github
vers votre machine, dans un répertoire appelé ISNTutoBottle. Ce
répertoire contient tous les fichiers et tout l'historique de
développement du projet.

Nous allons ensuite passer à la première étape du projet, en demandant
à git de remettre le dépôt dans l'état enregistré sous le nom de
step01

.. code-block:: bash

  $ cd ISNTutoBottle
  $ git reset --hard step01

La commande ``git reset --hard REV/TAG`` permet de remettre le
répertoire dans l'état exact qui avait été enregistré lors du commit
référencé REF (ou du tag TAG = référence de commit nommée par
l'utilisateur).

A ce moment, si vous listez les fichiers présents dans le répertoire
ISNTutoBottle (en utilisant l'explorateur de fichiers par exemple),
vous ne verrez qu'un fichier "lisez-moi" (README.rst) presque
vide. C'est normal, on commence tout juste.

.. TODO: Expliquer en footnote ce que veut dire .rst

.. TODO: Expliquer l'intérêt d'un README


Etape 1 : mettre en place un environnement de développement
===========================================================

Pour pouvoir bricoler sur notre projet sans "polluer" le reste de
notre système, nous allons créer un environnement python virtuel
(virtualenv).

Cet environnement virtuel constitue en fait en une copie des
exécutables python et des librairies utiles dans un répertoire, à
partir duquel le programme python sera exécuté

.. code-block:: bash

  $ virtualenv venv

Cette commande crèe un répertoire venv contenant tout ce qu'il faut
pour exécuter des programmes en python. Deux paquets externes sont
téléchargés et installés dans cet environnement virtuel :
``distribute`` et ``pip``. Le second est le programme permettant
d'installer de librairies (programmes python que vous pouvez
réutiliser dans votre projet).

ATTENTION: là, votre environnement virtuel est créé (dans le
répertoire venv), mais pas activé. Si vous tapez ``python`` dans le
terminal, c'est le python de votre système qui se lancera, alors qu'on
veut désormais utiliser le python de *venv*. 

Pour activer un environnement virtuel, il faut taper la commande
suivante

.. code-block:: bash

  $ source venv/bin/activate

Cette commande lit (source) le fichier ``activate`` (activation) situé
dans le répertoire ``bin`` du répertoire ``venv`` : cela active
l'environnement virtuel, ce qui est visible dans l'invite de commande
: avant, vous aviez une invite de commande commençant par
*isn@isnusbkXX*, et maintenant, un (venv) s'est rajouté en début de
ligne.

C'est le signe que l'environnement virtuel est activé (=> que lorsque
vous exécutz ``python``, c'est celui de l'environnement virtuel qui
est appelé.

Si vous fermez votre terminal, que vous en ouvrez un deuxième, il faut
refaire l'activation dans chaque terminal (vérifiez que vous avez bien
le *(venv)* en début de ligne.


Etape 2 : installer les prérequis
=================================

Passage à l'étape 2 

.. code-block:: bash

  $ git reset --hard step02

Dans l'explorateur de fichiers, vous devez voir apparaitre un fichier
nommé *requirements.txt*.

Dans cette étape, nous allons installer les paquet / librairies /
programmes externes dont nous allons avoir besoin. Le micro framework
bottle consiste en un seul fichier (*bottle.py*), nous pourrions le
télécharger et le coller dans le répertoire du projet, mais cette
opération peut être fastidieuse si notre projet a besoin de beaucoup
dépendances (librairies nécessaires), et que ces librairies doivent
être mises à jour régulièrement.

On utilise donc le système ``pip`` qui automatise toutes ces étapes
(téléchargement, installation, mise à jour, ...). ``pip`` comme
arguments une action et un nom de librairie : ``pip install bottle``
par exemple va télécharger et installer la dernière version du micro
framework bottle.

Et pour que n'importe qui puisse installer toutes les librairies
requises pour faire fonctionner le programme, on les liste dans le
fichier *requirements.txt*; il suffit alors de lancer pip en lui
disant d'installer tous les paquets requis présents dans ce fichier
(un par ligne)

.. code-block:: bash

  $ pip install -r requirements.txt

A la fin de la commande, bottle est installé dans l'environnement
virtuel *venv*.

Etape 3 : créer votre premier serveur web
=========================================

On passe à l'étape 3

.. code-block:: bash

  $ git reset --hard step03

Dans l'explorateur de fichiers, vous devez voir apparaître un fichier
nommé ``app.py``. Ce fichier est le programme principal de notre
serveur web. Analysons un peu son contenu ::

  # On importe les fonctions run et route de bottle
  from bottle import route, run

  # On définit une route : une url à laquelle le serveur 
  # répondra en exécutant la fonction placée en dessous (ici
  # appelée index, n'importe quel nom de fonction convient)
  @route('/')
  def index():
    # Cette fonction renvoie une chaîne de caractères
    # fort classique...
    return "HELLO WORLD"

  # On lance le serveur, qui écoutera les requètes uniquement
  # en local, sur le porte 27200, en affichant les informations
  # de débuggage.
  run(host='localhost', port=27200, debug=True)

Pour comprendre un peu mieux ce petit programme, il faut bien se
rappeler les points suivants : 

* la communication entre un client et un serveur se fait en  `TCP/IP`_


* le client envoie une requète au serveur (une machine identifiée par
  son adresse IP ou son nom de domaine), sur un port donné; dans notre
  cas, la requète est une requète  `HTTP`_ 

* le serveur écoute le port sur l'IP, et répond à la requète.

.. _TCP/IP: http://fr.wikipedia.org/wiki/Suite_des_protocoles_Internet
.. _HTTP: http://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol 

Ici, le port d'écoute est 27200, l'IP est l'ip locale 127.0.0.1 (qui
ne sort pas de la machine), et le serveur est configuré pour renvoyer
le messge "HELLO WORLD" à une requète spécifique.

Nous allons tester ce serveur et décortiquer un peu son
fonctionnement. Il faut d'abord le lancer, en exécutant le programme
`app.py`

.. code-block:: bash

  $ python app.py

Si tout se passe bien, le programme nous affiche quelques lignes du
genre ::

  (venv)isn@isnusbk01:~/ISNTutoBottle$ python app.py 
  Bottle v0.11.6 server starting up (using WSGIRefServer())...
  Listening on http://localhost:27200/
  Hit Ctrl-C to quit.

Traduction : je suis un serveur utilisant Bottle v0.11.6, j'écoute sur
localhost, sur le port 27200 (notation IP:PORT); pour terminer mon
exécution, appuyez sur Ctrl-C.

Prenez un navigateur, et tapez l'adresse de votre serveur dans la
barre d'adresse (pas dans google ni dans le champ de recherche
!!)... votre navigateur doit afficher le message HELLO WORLD.

Et votre programme dans son terminal, a lui affiché une ou plusieurs
lignes du type ::

  127.0.0.1 - - [08/Mar/2013 00:00:38] "GET / HTTP/1.1" 200 11
  127.0.0.1 - - [08/Mar/2013 00:00:39] "GET /favicon.ico HTTP/1.1" 404 743

qui sont affichées grâce au paramètre de debug, et qui précisent :

* l'adresse IP du client : ici 127.0.0.1
* la page qui fait référence à la page actuelle (lorsqu'on suit un
  lien sur un site, ce qui n'est pas le cas ici, le champ est donc
  vide : c'est l'espace entre les - -)
* la date et l'heure de la requète
* la requète HTTP
* le code de réponse
* le nombre d'octets de la réponse

Les requètes et les réponses HTTP sont composées de plusieurs parties,
une lecture attentive de
http://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol est fortement
conseillée avant d'aller plus loin.

Ici, la **méthode** de la requète est **GET**, le client demande
l'**URL** **/** en utilisant le protocole HTTP/1.1. Il y a aussi des
en-têtes (non affichés ici), au minimum un en-tête "Host:" indiquant
quel est la partie "hôte" de la demande ( http://host/url ).

Le serveur renvoie une réponse comprenant entre autres un code-réponse
: ici 200 indique un succès, et 404 indique "page non trouvée" (le
navigateur demande la favicon, l'icône pour les favoris, que notre
serveur n'est pas programmé pour envoyer).

Pour mieux saisir cet échange, nous allons l'espionner un peu plus :
dans votre navigateur, vous trouverez un bouton en forme de scarabée
en haut à droite (FireBug). Lorsque vous l'activez, un panneau se
rajoute en bas de votre navigateur, vous permettant d'explorer le code
des pages que vous visitez, le trafic HTTP et beaucoup d'autres
choses.

Dans le panneau de FireBug, activez l'onglet réseau (case à cocher sur
la petite flèche sur l'onglet), et rechargez votre page
http://localhost:27200 ... Vous voyez apparaître une ligne, indiquant
qu'une requète a été faite. En développant cette ligne, vous avez
toutes les informations sur la requète et la réponse, formatté
sympathiquement (ou pas : vous pouvez consulter les données brutes en
cliquant sur "voir le code source").

Dans le terminal, tuez votre serveur en appuyant sur Ctrl + C, et
faites les exercices ci-dessous... pensez à tuer et relancer le
serveur à chaque fois que vous modifiez le code source de
l'application.

Exercices
---------

* Essayez de trouver à quoi correspondent les en-têtes de l'échange
  HTTP que vous venez de capturer entre votre serveur et votre navigateur.

* Naviguez sur un ou deux sites avec FireBug activé, et familiarisez
  vous un peu avec les panneaux HTML, CSS et Réseau.

* Modifiez le programme app.py pour que votre serveur réponde "ISN"
  lorsque vous visitez l'adresse http://localhost:27200/ISN dans votre
  navigateur (en conservant le hello world pour l'url racine /)

* Cherchez dans la documentation de bottle la manière de créer une
  route répondant à une requète HTTP avec une méthode autre que GET
  (POST par exemple).

Etape 4 : utiliser des templates
================================


On passe à l'étape 4 (si le fichier app.py est encore ouvert dans un
éditeur de texte, fermez le avant).

.. code-block:: bash

  $ git reset --hard step04

Dans l'explorateur de fichiers, vous devez voir apparaître un dossier
nommé ``views`` contenant un fichier appelé ``index.tpl`` :

.. code-block:: html

  <!DOCTYPE html>
  <html>
    <head>
      <title>Welcome to ISN land</title>
    </head>
    <body>
      <h1>Bienvenue {{toto}}</h1>
    </body>
  </html>


Dans l'étape 3, nous avons renvoyé une chaîne de caractère très simple
pour la route /. Pour renvoyer une page html complète, il "suffirait"
de taper cette page html à la place de HELLO WORLD dans la chaîne de
caractères. Mais de manière générale, dans un souci de lisibilité et
d'évolutivité du code, il est déconseillé de mélanger les torchons et
les serviettes : le python avec le python, le HTML avec le HTML.

Nous allons pour cela utiliser des templates (modèles) : des fichiers
contenant le html à renvoyer au navigateur. Par défaut, bottle cherche
ces templates dans un répertoire appelé **views**.

Si on retourne voir le fichier ``app.py``, on constate les changements
suivants ::

  from bottle import route, run, template

  #...

  @route('/')
  def index():
    return template('index.tpl', {'toto':'TITI'})

Au lieu de retourner une chaîne de caractères, on appelle la fonction
``template`` avec deux arguments :

* une chaîne de caractères 'index.tpl' qui désigne le template à
  utiliser
* un dictionnaire contenant une clef ('toto') associée à une valeur
  ('TITI')

La fonction *template* va aller chercher le fichier index.tpl contenu
dans le dossier views, et va le renvoyer au navigateur après avoir
remplacé toutes les occurrences de {{toto}} par la valeur TITI.

Si vous relancez le serveur (``python app.py``), et que vous visitez
la page http://localhost:27200/ vous constaterez que s'affiche le
message "Bienvenue TITI", avec un titre de page de "Welcome to ISN
land"...

Il est tout à fait possible de ne pas mettre le deuxième argument de
la fonction *template*, auquel cas aucun remplacement ne sera effectué
dans le template.

Exercices
---------

* Créez une route "/me" affichant une page html présentant votre nom,
  prénom, date de naissance.

* Créez une route "/now" affichant une page html donnant le jour et
  l'heure (indications : la fonction datetime.now() du module datetime
  permet d'obtenir l'instant présent. Pour utiliser cette fonction, il
  faut importer la fonction datetime du module datetime via ``from
  datetime import datetime``.

Une fois que vous avez terminé ces premières étapes, il est désormais
temps d'intéragir un peu avec notre serveur. :doc:`Aller aux étapes
suivantes <getpost>`
