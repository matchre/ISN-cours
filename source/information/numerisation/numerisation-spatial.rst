.. _numerisation-spatial:

Numérisation d'un signal spatial - images numériques
####################################################

La numérisation d'un signal spatial (on prendra ici l'exemple d'une
image) passe d'abord par le découpage de l'image en petites zones,
appelées pixels, la plupart du temps carrées (mais on peut faire des
découpages rectangulaires, hexagonaux, ...)

Chaque pixel sera représenté par un nombre représentant l'intensité
lumineuse.

* pour une image en noir et blanc, chaque pixel sera représenté par
  un nombre représentant l'intensité lumineuse moyenne de la zone du
  pixel.
* pour une image en couleurs, chaque pixel sera représenté par une
  suite de 3 nombres, représentant l'intensité de la lumière dans le
  domaine du rouge, du vert et du bleu (correspondant aux 3 domaines
  du visibles que peuvent recevoir les récepteurs situés dans notre
  oeil) : les "canaux" Rouge, Verts, Bleus.
* pour une image pouvant présenter une transparence, on rajoute un
  nombre représentant la transparence de chaque pixel : le canal
  "Alpha"

Le nombre de bits utilisés pour coder chaque information d'intensité
lumineuse est généralement de 8 bits (soit 256 valeurs), mais on peut
en utiliser moins ou plus selon les usages.

Exemples :

* une image strictement noire et blanc (exemple : un texte) peut être
  codée avec 1 bit par pixel (noir ou blanc)
* une image couleur avec transparence sera codée avec 4x8 bits.

Des exemples avec Lena
======================

En couleurs
-----------

L'image que nous prendrons pour illustrer la numérisation d'un signal
spatial est l'image de Lena (miss Novembre 1972 de Playboy, devenue un
standard industriel et scientifique - c'est pas une blague :
http://www.cs.cmu.edu/~chuck/lennapg/

Tout d'abord voilà l'image "réelle" (c'est faux, c'est déjà une image
numérisée, mais on va faire "comme si")...

.. image:: images/lena_std.*

La numérisation de cette image commence par la définition d'une
"grille" plus ou moins fine de pixels (PixEl = PICTure ELement à
partir de l'anglais un peu déformé). Exemple : grille de 21x21 pixels :

.. image:: images/lena_pixels21.*

Chaque pixel est UNE entité de couleur, luminosité. Pour un appareil
photo, chaque pixel est un élement photosensible du capteur de
l'appareil photo (CCD). Pour un scanner, c'est la même chose, sauf que
c'est une seule ligne de capteurs qui est déplacée verticalement sur
l'image. Les détails en dessous du pixel sont donc "écrasés", lissés,
moyennés sur toute la surface du pixel.

Lena en 21x21 pixels a donc cette tête (plus carrée et moins sympa) :

.. image:: images/lena_pixels21_result.*

Avec 128x128 pixels, l'image serait plus reconnaissable mais ça ne
change rien au principe

.. image:: images/lena_pixels128_result.*

Puis pour chaque pixel, l'intensité de la lumière dans le rouge, le
vert et le bleu sont mesurées et transformées en nombres. Le nombre de
chiffres (la résolution du signal numérique) utilisés pour exprimer le
résultat de cette mesure est généralement de 8 par couleur, soit 256
valeurs (0 = absence d'intensité lumineuse dans la couleur, 255 =
intensité maximale dans la couleur).

.. image:: images/lena_trichro_21.*

* Premier pixel (en haut à gauche) : R=226, V=132, B=112
* Deuxième pixel (le suivant à droite) : R=231, V=142, B=113
* Troisième pixel : R=204, V=102, B=97
* ...
*  441ème pixel (en bas à droite) : R=122, V=46,B=72

La suite de ces valeurs forme l'image numérisée brute (raw : non
compressée) : en gros : 226123112213142113.......204102097.

Dans la réalité, un ordinateur stocke des bits, donc des suites de 0
et de 1, regroupés en paquets. Il rajoute aussi souvent au début du
fichier des informations sur le type de fichier, la taille du fichier,
etc..

Lena en 21x21 pixels, en format de fichier TIFF (non compressé) a
cette tête là ::

  49 49 2A 00 34 05 00 00
  E2 84 70    E7 8E 71    CC 66 61    B0 48 53    BC 52 57    CD 62 5E
  D0 64 60    D1 64 61    CF 65 62    CE 63 5F    CF 65 62    CB 61 60
  C2 5B 5F C6 64 64 E1 86 71 E0 81 69  E6 9B 7A D7  97 7B BC 59 5D
  C4 5F 5F 9C 45 54 E5 89 70 E7 8B 6E CC 62 5A B0 45 50 BD 4F 54
  CC 5E 5C D0 5F 5F D2 5F 5F CF 5D 5C C8 60 5F CB 5B 5D CE 5F 5F
  C8 5B 5E BE 55 5F DF 83 73 E0 83 6D DB 7A 6A EB AD 83 C5 6A 66
  96 3D 51 61 18 40 E3 80 68 E5 84 69 CC 61 5A AC 41 4E BF 4E 54
  CD 5A 5A CF 5F 60 C5 63 6A C5 80 83 D2 A7 9C D6 A7 9A C8 6F 73
  C2 53 5A BD 50 5A DC 77 6F DE 79 6A DB 71 63 DD 7B 69 B0 6E 6A
  ...

La première ligne est l'en-tête du fichier, on ne s'en occupe pas ici.

Les lignes suivantes représentent les pixels :

* premier pixel *E2 84 70*, en base 16 (hexadécimal, chaque chiffre
  représente 4 bits), correspondant à 226 (=E2), 132 (=84) et 112
  (=70), valeurs R,V,B de notre premier pixel.

* deuxième pixel *E7 8E 71* correspondant à 231, 142, 113...

* etc..

En niveaux de gris
------------------

Pour une image en niveaux de gris, c'est la même chose, en plus simple
: il n'y a qu'une valeur à enregistrer pour chaque pixel, c'est la
luminosité du point : 0 = noir, 255 = blanc.

.. image:: images/lena_nb.*

.. image:: images/lena_pixels21_result_nb.*

Ce qui donne un fichier (sans l'en-tête)  ::

  __ __ __ __  __ __ __ __  97 9F 7C 5F  69 78 7B 7C  7B 79 7B 78  71 79 98 94  A8 A2 6E 74  58 9A 9D 78
  5D 67 75 77  78 75 76 73  76 72 6C 95  95 8D B8 7D  52 2A 94 97  77 59 67 73  76 79 8F AF  B0 83 6B 68
  8C 8D 87 8F  7C 24 2A 66  94 74 58 63  71 6A 71 83  A5 BF CC 86  61 8A 5F 89  82 2D 2C 66  52 93 74 57
  63 70 69 7D  83 AC C3 C9  D5 6B 8C 2E  A1 3C 2A 47  98 5A 94 78  58 6C 6A 68  78 9A AE B2  BF C2 C1 94
  B7 DF 32 2B  92 97 59 99  7B 56 6C 87  69 83 8E 9B  A2 A9 AB B5  C8 C9 AA 22  6C 9A 97 5D  9A 7D 57 69
  99 71 79 7B  50 5F 45 B5  C0 B5 77 53  32 92 98 94  60 97 7E 56  5B AF 6F 68  42 34 51 B1  B2 B8 6D 63
  26 57 A0 9C  96 5C 97 80  59 63 7F 63  32 34 44 A6  A1 B6 CA 64  32 2A 8F 98  94 93 58 96  81 58 70 5A
  ...

soit 151, 159, 124, 95, ...

En pratique : Do It Yourself avec Gimp
======================================

Les outils :

* un éditeur d'images libre : The Gimp (http://www.gimp.org/)

* un visionneur binaire : hexedit (libre) sous linux, Hexedit
  (gratuit, pas libre) sous windows (http://www.hexedit.com/) et
  iJeSaisPasMaisCaDoitExister sous mac...

TODO

En pratique : utilisation pour interférences / diffraction
==========================================================

TODO: exploitation (RegAVI ou ImageJ) d'une photo de figure
d'interférence / diffraction pour récupérer courbe intensité
lumineuse.


Vocabulaire et trucs pratiques
==============================

* définition (ou taille)
* résolution
* espace disque (ou taille)

