.. _analogique-numerique:

Analogique et numérique
#######################

Signal analogique
-----------------

Les gandeurs physiques qui décrivent le monde qui nous entoure sont
à notre échelle tout à fait continues (même si au niveau quantique, la
plupart sont quantifiées), dans leurs valeurs et dans le temps.

Exemples : la température, la pression (signal sonore, par exemple),
l'intensité lumineuse (vision du monde qui nous entoure, ...)

Pour transmettre une de ces informations à distance, on utilise la
plupart du temps un signal électrique. Il faut alors convertir cette
grandeur physique en signal électrique par l'intermédiaire d'un
capteur, qui convertit la grandeur physique en grandeur électrique.

Exemples : capteur de température (thermistance, LM335, ..), capteur
de lumière (photorésistance, photodiode, capteur CCD, ...), capteur de
son (microphone, ...)...

Le signal électrique est alors une "image" de la grandeur physique
initiale, et garde donc la continuité dans le temps et dans les
valeurs : c'est un signal analogique.

On peut transmettre directement ce signal, l'encodage du signal étant
donc la connaissance de la relation entre la grandeur physique
initiale et le signal électrique transmis, et le décodage se faisant
en inversant cette relation.

Exemple : le circuit électrique spécialisé LM335 fournit une tension
électrique proportionnelle à la température (10 mV/K).

On peut aussi *numériser* ce signal.

Signal numérique
----------------

La numérisation d'un signal consiste à le représenter sous la forme
d'une suite de nombres (d'où le nom "numérisation").

Cette numérisation est rendue nécessaire par le fait que les
ordinateurs ne sont que de grosses calculatrices qui fonctionnent avec
des circuits électriques qui effectuent des opérations en binaire (0
ou 1 : voir :ref:`binaire-bases`)

Un signal numérique est constitué d'une suite de valeurs discrètes, et
donc est intrinsèquement discontinu.

L'information à décrire numériquement peut être temporelle (un son,
par exemple), spatiale (une image), ou les deux à la fois (une scène
animée par exemple).

Les principes de numérisation sont un peu différents selon qu'il
s'agit d'une information temporelle, spatiale ou spatio-temporelle,
mais certains points sont communs, comme la résolution d'un signal
numérique.

Pour les détails concernant chaque type de signal, voir :

* :ref:`numerisation-temporel`
* :ref:`numerisation-spatial`

Résolution d'un signal numérique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les valeurs représentées par un ordinateur sont stockées à l'aide de
chiffres. Le nombre de chiffres utilisés pour décrire un élément
d'information donne la résolution du signal numérique.

Exemple en base 10 :

* si on utilise 2 chiffres pour décrire une température, on a 100
  valeurs disponibles. Si la plage de température que l'on décrit avec
  ces 100 valeurs va de 20 à 30 degrés, on aura une précision à 0,1 degrés.
* si on utilise 3 chiffres, on aura 1000 valeurs disponibles. Pour la
  même plage de température, on aura une précision à 0,01 degrés.
* de manière générale, avec n chiffres, on aura 10^n valeurs possibles.

Evidemment dans la nature, la température ne varie pas de 0,1 en 0,1
degrés, ni même de 0,01 en 0,01 degrés. On "manque" donc des valeurs.

Dans le monde informatique, les chiffres sont 0 ou 1, et sont appelés
des **bits**; en utilisant n bits, on peut décrire 2^n valeurs
possibles.

Plus le nombre de bits utilisés est grand, meilleure est la
résolution, mais cela prend aussi plus de place pour stocker
l'information et plus de temps pour la transmettre. Il faut donc à
chaque fois trouver le bon compromis entre la résolution et le
contraintes techniques / économiques.

Exemple : pour le son qualité CD, on utilise 16 bits, soit 65536
valeurs pour décrire une "tranche" de son. Pour une photo, on utilise
3x8 bits, soit 24 bits, ce qui donne environ 16 millions de valeurs
possible pour décrire un élément de photo.





Pixel : vient de l'anglais "Picture Element" (PictEl -> Pixel) :
élément d'image.

Pour représenter une image sous forme numérique, on doit la découper
en petit

Pixellisation
