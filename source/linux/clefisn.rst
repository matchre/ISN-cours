La clef ISN, le monde de GNU/Linux
##################################

Pour pouvoir travailler en mode "nomade" parmi les différentes salles
info de l'établissement, au CDI ou à domicile, vous êtes dotés d'une
clef ISN contenant tous les outils nécessaires aux différntes
activités de l'année.

Cette clef USB contient un système d'exploitation GNU/Linux complet et
peut donc être utilisée pour fournir un système d'exploitation ainsi
qu'un ensemble logiciel cohérent et adapté à l'enseignement d'ISN.


Démarrage
---------

Concrètement, il "suffit"[#f1]_ de dire à l'ordinateur de démarrer en
utilisant la clef USB comme disque où chercher le système
d'exploitation (selon les machines : F8, F9, Escape, Suppr, F2...).

.. rubric:: Notes

.. [#f1] Malheureusement : sur des machines récentes sous Windows 8,
         il peut être nécessaire de désactiver une sécurité au niveau
         du bios. Cette opération est en dehors des cours ISN (google
         is your friend : "EFI bios", à vos risques et périls -
         opération déconseillée)

Une fois l'ordinateur démarré sur la clef (patience, nos clefs ne
sont vraiment pas des Rolls, mais c'est normalement plus rapide que le
XP du lycée), vous avez accès à votre session avec le login/pass :
isn/isn (vous pourrez changer votre mot de passe par la suite).

Infos utiles
------------

Les logiciels se lancent via le petit logo Ubuntu en haut à gauche de
l'écran; il suffit de taper quelques lettres du nom du logiciel ou de
ses fonctionnalités pour qu'il apparaisse.

Vous pouvez conserver un logiciel que vous utilisez fréquemment via un
clic droit sur son icône lorsqu'il est lancé : "Conserver dans le
lanceur".

Nous utiliserons la clef à la fois en mode "graphique" (i.e. à la
souris et au clic) et en mode "rustique" (i.e. via un terminal et la
ligne de commande)

Un mémo des commandes utiles (en ligne de commande) est disponible via
:doc:`shell`

Exploration de l'arborescence des fichiers
------------------------------------------

Explorer (via le gestionnaire de fichier ou mieux, via un terminal en
utilisant les commandes `ls` et `cd` (voir :doc:`shell`)
l'architecture des répertoires de la clef.

- **/** est la racine de l'arbre (le point le plus haut - ou bas selon le
  sens de l'arbre)

- **/bin** contient des programmes de base du système

- **/sbin** contient des programmes de base du système, utilisables
  uniquement par le *superutilisateur* (sur la clef, c'est pas vous
  :-)

- **/lib** contient les librairies (morceaux de programme partagés
  entre plusieurs programmes)

- **/boot** contient les fichiers nécessaire au démarrage de
  l'ordinateur (le noyau, etc..)

- **/dev** est un répertoire où chaque fichier représente un "device"
  (composant) physique ou virtuel de la machine (exemple : /dev/sda
  représente le premier disque dur de la machine, /dev/sda1 représente
  la première partition de ce disque, etc..). Ecrire ou lire des
  valeurs dans ces fichiers permet d'envoyer ou de récupérer des
  informations de ces composants ::

    $ cat /dev/random # lit sans s'arrêter des valeurs aléatoires
    $ cat /dev/zero # lit des zéros
    $ echo "toto" > /dev/null # envoie "toto" dans un trou noir
    $ dd if=/dev/null of=/dev/sda # écrit des zéros sur tout le disque
    $ ...

  Tous ces exemples ne sont pas exécutables par vous (surtout le
  dernier...)

- **/proc** est un répertoire offrant une représentation de tous les
  processus (programmes) en train de tourner sur la machine à chaque
  instant : chaque numéro contient les infos sur un programme. Ce
  dossier contient aussi des entrées permettant d'obtenir des
  informations sur certains périphériques (/proc/bus/pci/devices par
  exemple, ou /proc/meminfo)

- **/sys** est un répertoire présentant des fichiers permettant
  d'intéragir avec le système (en y lisant ou en y écrivant). Par
  exemple écrire la valeur adéquate dans /sys/acpi/state permet de
  mettre l'ordinateur en veille
  (http://acpi.sourceforge.net/documentation/sleep.html)

- **/etc** contient toutes les informations de configuration pour les
  programmes du système, ainsi que les infos sur ce qu'il faut
  démarrer à l'allumage du système (/etc/init..)

- **/var** contient toutes les informations qui changent régulièrement
  pendant que l'ordi tourne (les "logs", les mails, les fichiers à
  envoyer aux imprimantes, etc..)

- **/usr** reprend /bin, /sbin, /lib mais pour des programmes non
  vitaux pour le fonctionnement du système, ainsi que des répertoires
  intéressants du genre **/usr/share/doc** (toute la documentation des
  programmes installés sur la machine)

- **/usr/local** reprend encore cette structure (/lib, /bin, /sbin...)
  mais pour des programmes installés "localement" (c'est à dire
  manuellement, pas via le "market/store/dépôt" officiel.

- **/tmp** est le répertoire temporaire, tout le monde peut y écrire,
  mais les fichiers disparaissent à chaque redémarrage de la machine

- **/home** contient les répertoires utilisateurs

