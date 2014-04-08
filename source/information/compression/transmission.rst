Chaîne de transmission d'informations
#####################################

Principe général
================

Définition : **Information** : Élément de connaissance susceptible d'être représenté à
l'aide de conventions pour être conservé, traité ou
communiqué.

La transmission d'une information est une activité que nous effectuons
en permanence dans la vie :

* j'ai une idée
* je l'exprime par une phrase
* je prononce la phrase
* mon interlocuteur entend la phrase
* il l'interprète et peut s'imaginer mon idée

Cette action classique est un exemple de base de transmission
d'information : 

- l'information à transmettre est mon idée (je suis une source d'information)
- je l'encode avec des mots, dans une langue donnée (je suis un encodeur)
- je la transmets via une onde sonore (je suis un émetteur)
- mon interlocuteur reçoit cette onde (c'est un récepteur)
- il décode le signal audio en phrase et l'interprète (c'est un
  décodeur)

C'est le schéma d'une chaîne de transmission d'informations :

 .. graphviz::

   digraph chainetrasmission {
     splines=ortho;
     size=8;
     subgraph  {

      subgraph clustertransmission {
          node [shape=ellipse, style=filled, fillcolor=yellow]; Emetteur; Récepteur;
          Emetteur -> Récepteur [label=" Info\ntransmise"]
          label="Canal de transmission";
          graph[style=dotted];
      }
      node [shape=diamond]; { node [label=""] infostart; infoend; }
      node [shape=ellipse]; Encodeur; Décodeur;
      infostart -> Encodeur [label = " Info à transmettre"]
      Encodeur -> Emetteur [label=" Information codée"]
      Récepteur -> Décodeur [label=" Information reçue"]
      Décodeur -> infoend [label=" Information décodée"]
     }
     subgraph  {
      subgraph clusterexempleransmission {
          node [shape=ellipse, style=filled, fillcolor=yellow]; "Ma voix"; "Ton oreille";
          "Ma voix" -> "Ton oreille" [label=" Info\ntransmise"]
          label="Canal de transmission";
          graph[style=dotted];
      }
      node [shape=diamond]; { node [label=""] infostart2; infoend2; }
      node [shape=ellipse]; "Mon cerveau"; "Ton cerveau";
      infostart2 -> "Mon cerveau" [label = " Info à transmettre"]
      "Mon cerveau" -> "Ma voix" [label=" Information codée"]
      "Ton oreille" -> "Ton cerveau" [label=" Information reçue"]
      "Ton cerveau" -> infoend2 [label=" Information décodée"]
     }
   }


Sur ce même schéma, on peut associer autant de chaines de transmission
d'information qu'il y a de manière de coder/décoder l'information et
de transmettre l'information.

Exemples : les indiens et les signaux de fumées, le télégraphe, le
téléphone, la parole, le language des signes... pour chacun de ces
exemples, identifier l'encodage, l'émetteur, le canal de transmission,
le récepteur et le décodeur.

Evolution des chaînes de transmission d'informations
====================================================

* Avant l'électricité, le canaux de transmissions étaient visuels,
  sonores ou physiques (écrit..)
* L'arrivée de l'électricité a permis de rajouter un canal jusqu'alors
  inutilisé (invention du télégraphe)
* La maîtrise des ondes électromagnétiques a permis de s'affranchir
  d'un support physique pour la transmission de l'information
* Le développement de l'électronique a permis la miniaturisation des
  dispositifs (comparer un téléphone sans fil 1ère génération à un
  smartphone actuel)
* Le développement de l'informatique a permis de coder des types
  d'informations très variés (images, sons, vidéos, textes) et de les
  transmettre par des réseaux.
* Le développement de la fibre optique a permis d'augmenter le débit
  et la qualité des transmissions.
* L'intégration des technologies sans fil (wifi, bluetooth, téléphonie
  mobile) a permis de s'affranchir des liaisons filaires dans les
  appareils du quotidien.
