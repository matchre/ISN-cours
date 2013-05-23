Intéragir avec le serveur : envoyer et traiter des informations
###############################################################

Etape 5 : envoyer des données au serveur
========================================

Un peu de théorie
-----------------

Petit rappel sur la communication entre le client et le serveur (le
protocole complet est décrit dans le RFC 2616 :
http://www.w3.org/Protocols/rfc2616/rfc2616.html) : le
client envoie une *requète HTTP* au serveur ::

  METHOD URL HTTP/1.1
  Host: www.example.org
  Cookie: name=value; name2=value2
  HEADER: VALEUR

  CONTENU DE LA REQUETE

* La méthode METHOD peut être GET, POST, PUT, PATCH, DELETE...

* L'URL est l'adresse que l'on envoie au serveur, de forme absolue
  (http: //  nom.de.domaine :port chemin  ? query) ou sous la forme d'un
  chemin (/chemin ? query). Exemples ::

    http://abc.com:80/home/index.html?user=toto
    http://abc.com/home/index.html
    //abc.com/home/index.html
    /home/index.html

* Les lignes suivantes sont les en-têtes http, ici *Host* qui indique
  (en cas d'URL uniquement sous forme de chemin par exemple) à quel
  nom de domaine est destinée la requète, et *Cookie* qui envoit à
  chaque requète les valeurs stockées dans des petits fichiers (les
  gâteaux) dans le navigateur du client. Il existe plusieurs dizaines
  d'en-têtes HTTP
  (http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5.3) et on
  peut créer les siens (mais il vaut mieux éviter).

* Puis une ligne blanche sépare les en-têtes du contenu de la requète
  (si la requète a un contenu).

La transmission de données avec le serveur peut donc se faire de
différentes manières selon les besoins :

* en lui envoyant une requète HTTP par la méthode **GET**
* en lui envoyant une requète HTTP par la méthode **POST**
* via les cookies (que nous traiterons + loin)
* via les en-têtes (que nous ne traiterons pas)

Il convient tout d'abord de choisir la **méthode** (GET ou POST, voire
PUT, PATCH, DELETE que nous ne traiterons pas ici) à utiliser.

* GET une méthode réservée aux requètes "sûres" : en ayant en tête que
  les connexions internet sont souvent défectueuses, il arrive souvent
  que les utilisateurs s'excitent sur le bouton "envoyer" d'un
  formulaire, rechargent la page, etc... les requètes envoyées avec la
  méthode GET doivent être idempotentes, c'est à dire que même si
  quelqu'un recharge 20 fois la page, ça ne doit rien changer. On
  réserve donc le plus souvent la méthode GET aux consultations de
  pages n'écrivant aucune donnée du côté serveur. D'autre part, la
  méthode GET ne peut pas envoyer beaucoup de données puisque ces
  données sont envoyées via la chaîne de requète de l'url (la partie
  après le point d'interrogation dans
  http://google.fr?q=blabla). Exemple ::

    GET /meteoa10jours?ville=27200
    Host: www.meteofrance.com
    Cookie: maville=Houlbec%20Cocherel

* POST (et les autres) sont des méthodes que l'on utilise pour les
  requètes ayant un effet sur des données côté serveur (exemple:
  incrémenter un compteur, ajouter une ligne dans un tableau,
  etc..). Les requètes POST ne sont en effet pas systématiquement
  renvoyées par les navigateurs (pensez au message qui s'affiche
  souvent lorsque vous rechargez une page juste après avoir envoyé un
  formulaire). Autre avantage des requètes POST : elles peuvent
  contenir dans le corps même de la requète des données, sans
  limitation (ou peu) de taille. Exemple ::

    POST /acheter
    Host: www.ebay.fr
    Cookie: user=myusername; code=123456

    idpanier=123123&montant=3240&monnaie=EURO&article1=HomeCinema...

Passons à la pratique
---------------------

On passe à l'étape 5

.. code-block:: bash

  $ git reset --hard step05

Dans l'explorateur de fichiers, vous devez voir apparaître dans le
répertoire *views* des templates quatre fichiers appelés ``form1.html``,
``form2.html``, ``result1.html`` et ``result2.html``. Quelques lignes
ont aussi été ajoutées dans le fichier de l'application ``app.py``.


Méthode GET
~~~~~~~~~~~

``form1.html`` et ``result1.html`` sont un exemple d'utilisation d'une
méthode GET pour envoyer une donnée au serveur, et d'afficher une page
de résultat. La page ``form1.html`` contient le formulaire :

.. code-block:: html

  <html>
    <head>
      <title>Formulaire GET : exemple</title>
    </head>
    <body>
      <h1>Formulaire à remplir</h1>
      <form method='GET' action='/action1'>
        Votre nom : <input type='text' name='nom' /><br/>
        Votre prénom : <input type='text' name='prenom' /><br/>
        <input type='submit' value='Envoyer'/>
      </form>
    </body>
  </html>

 
On peut voir ici un un formulaire, ouvert par la balise **<form>**; les
attributs de cette balise form indiquent la *méthode* (method=GET) et
la page à laquelle *envoyer* le formulaire (action="/action1").

A l'intérieur de ce formulaire, on trouve du texte et des champs de
formulaire :

* balise **<input type="text">** : champ de texte sur une ligne
* balise **<input type="submit">** : bouton pour l'envoi du formulaire

Il existe plusieurs types de champs de formulaire, voir w3schools.com
par exemple pour plus de détails et la liste de tous leurs attributs
(longueur maximale, valeur initiale, ...).

Le seul attribut obligatoire si on veut transmettre les informations
rentrées dans le formulaire est l'attribut **name** : les données
saisies seront associées à ce nom.

Ce formulaire est affiché lors d'une requète à l'adresse
http://localhost:27200/form1 grâce aux lignes suivantes ajoutées à
``app.py`` ::

  # Exemple de formulaire 1 : méthode GET
  @route('/form1')
  def form1():
    return template("form1.tpl")

  # Traitement du formulaire 1; @get permet de ne répondre qu'aux
  #  requètes de méthode GET
  @get('/action1')
  def action1():
    # On récupère les valeurs du formulaire, envoyées dans la chaîne
    # de requète (query). La fonction get(nom, valeur_par_defaut)
    # permet de retourner une valeur par défaut si "nom" n'est pas
    # présent dans la chaîne de requète (principe de base: ne JAMAIS
    # faire confiance à l'utilisateur !!)
    nom = request.query.get('nom','INCONNU')
    prenom = request.query.get('prenom', 'INCONNU')

    # On utilise ces deux valeurs pour alimenter (via un dictionnaire)
    # l'affichage du template "result1.tpl"
    return template("result1.tpl", { 'nom': nom, 'prenom': prenom })


**Tester** : charger la page http://localhost:27200/form1 , remplir le
formulaire et le soumettre. La page
http://localhost:27200/action1?nom=BARBIER&prenom=Jean-Matthieu (par
exemple) se charge, et on peut constater que les éléments du
formulaire sont envoyés dans la chaîne de requète (la partie
nom=BARBIER&prenom=Jean-Matthieu)



Méthode POST
~~~~~~~~~~~~

Le formulaire form2.tpl et les fonctions form2 et action2 sont
quasiment identiques à form1 et action1. Les principales différences
sont :

* method="POST" au lieu de method="GET" dans la balise <form>

* action="/action2" au lieu de action="/action1" dans cette même balise

* @post à la place de @get dans ``app.py``

* request.forms à la place de request.query pour récupérer les valeurs
  transmises

* ajout des les lignes suivantes écrivent une ligne contenant le
  nom/prénom de l'utilisateur ainsi que la date/heure courante dans le
  fichier ``/tmp/logins.txt`` ::

    # On prend la date et l'heure courantes sous la forme
    # d'une chaîne de caractères au format ISO
    connexion = datetime.datetime.now().isoformat()

    # On sauvegarde le nom, prénom et heure de connexion dans un fichier
    with open('/tmp/logins.txt', 'a') as f:
        f.write("%s %s %s\n" % (nom, prenom, connexion))


**Tester** : charger la page http://localhost:27200/form2, remplir le
formulaire et le soumettre. La page http://localhost:27200/action2 se
charge et affiche un message. Vous pouvez vérifier que dans le
répertoire temporaire du système (/tmp, à partir de la racine), un
fichier logins.txt est apparu, et qu'il contient une ligne.

Rechargez cette page : votre navigateur devrait vous prévenir que ce
n'est pas innocent. Acceptez, une deuxième ligne a dû s'ajouter dans
logins.txt

Exercices
---------

* Observer à l'aide de FireBug le dialogue entre le navigateur et le
  serveur, dans l'onglet "réseau". Identifier les requètes Http, les
  en-têtes, les query strings et le corps de la requète POST.

* Modifier le programme app.py et le fichier form1.tpl pour afficher (à
  la place de ``result1.tpl``) le formulaire après qu'il ait été
  soumis, avec les valeurs des champs égales aux valeurs rentrées par
  l'utilisateur (indication : l'attribut **value** des champs input
  permet de préciser la valeur initiale).

* Modifier le programme de manière à vérifier que la longueur du nom
  et du prénom sont supérieures à 2. Renvoyer le formulaire avec un
  message d'erreur si nom ou prénom sont trop courts, et une page de
  succès (result1.tpl) si c'est OK.

* A partir de l'exemple donné sur le tutoriel de bottle
  http://bottlepy.org/docs/stable/tutorial.html#post-form-data-and-file-uploads,
  réaliser une page qui permet d'envoyer un fichier au serveur, ainsi
  que la fonction de traitement de ce formulaire, qui devra
  enregistrer le fichier sous un nom quelconque dans le dossier '/tmp'
