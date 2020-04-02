# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""
from matrice import *
from carte import *
def Plateau(nbJoueurs, nbTresors):
  tresors=list(range(1,13))
  mat = Matrice(7,7)
  setVal(mat, 0, 0, Carte(True, False, False, True, tresor=0, pions=[1]))
  if nbJoueurs > 1:
    setVal(mat, 0, 6, Carte(True, True, False, False, tresor=0, pions=[2]))
  else:
    setVal(mat, 0, 6, Carte(True, True, False, False, tresor=0, pions=[]))

  if nbJoueurs > 2:
    setVal(mat, 6, 0, Carte(False, False, True, True, tresor=0, pions=[3]))
  else:
    setVal(mat, 6, 0, Carte(False, True, True, False, tresor=0, pions=[]))

  if nbJoueurs > 3:
    setVal(mat, 6, 6, Carte(False, True, True, False, tresor=0, pions=[4]))
  else:
    setVal(mat, 6, 6, Carte(True, True, False, False, tresor=0, pions=[]))

  tres = random.choice(tresors)
  setVal(mat, 2, 0, Carte(False, False, False, True, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 4, 0, Carte(False, False, False, True, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 2, 2, Carte(False, False, False, True, tresor=tres, pions=[]))

  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 2, 6, Carte(False, True, False, False, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 4, 6, Carte(False, True, False, False, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 4, 4, Carte(False, True, False, False, tresor=tres, pions=[]))

  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 0, 2, Carte(True, False, False, False, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 0, 4, Carte(True, False, False, False, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 2, 4, Carte(True, False, False, False, tresor=tres, pions=[]))

  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 6, 2, Carte(False, False, True, False, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 6, 4, Carte(False, False, True, False, tresor=tres, pions=[]))
  tresors.remove(tres)
  tres = random.choice(tresors)
  setVal(mat, 4, 2, Carte(False, False, True, False, tresor=tres, pions=[]))
  tresors.remove(tres)

  listeCartesAmovibles = creerCartesAmovibles(13,nbTresors)
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 0:
        carte = listeCartesAmovibles[0]
        setVal(mat, i, j, carte)
        listeCartesAmovibles.remove(carte)

  return {'plateau' : mat, 'carte amovible' : listeCartesAmovibles[0]}
  """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """




def creerCartesAmovibles(tresorDebut,nbTresors):
  liste = []
  listeTres = []
  for i in range(tresorDebut,nbTresors+1):
    listeTres.append(i)
  for i in range(16):
    carte = tourneAleatoire(Carte(False, True, True, False, tresor=0, pions=[]))
    liste.append(carte)
  for i in range(6):
    carte = tourneAleatoire(Carte(False, False, False, True, tresor=0, pions=[]))
    liste.append(carte)
  for i in range(12):
    carte = tourneAleatoire(Carte(True, False, True, False, tresor=0, pions=[]))
    liste.append(carte)
  random.shuffle(liste)
  i = 0
  while len(listeTres) > 0 and i < len(liste):
    tres = random.choice(listeTres)
    liste[i]['trésor'] = tres
    listeTres.remove(tres)
    i+=1
  return liste
  """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """


def prendreTresorPlateau(plateau,lig,col,numTresor):
  res=False
  carteConsidéréé=getVal(plateau['plateau'],lig,col)
  if carteConsidéréé['trésor']==numTresor:
    res=True
  return res

"""
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """


def getCoordonneesTresor(plateau,numTresor):
  lig,col=0,0
  trésorTrouvé=0
  plateauConsidérée=plateau['plateau']
  for i in range(len(plateauConsidérée)):
    for j in range(len(plateauConsidérée[0])):
      if plateauConsidérée[i][j]['trésor']==numTresor:
        lig,col=i,j
        res=(lig,col)
        trésorTrouvé=1
  if trésorTrouvé==0:
    res=None
  
  return res

"""
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """


def getCoordonneesJoueur(plateau,numJoueur):
  lig,col=0,0
  JoueurTrouvé=0
  plateauConsidérée=plateau['plateau']
  for i in range(len(plateauConsidérée)):
    for j in range(len(plateauConsidérée[0])):
      if numJoueur in plateauConsidérée[i][j]['pions']:
        lig,col=i,j
        res=(lig,col)
        JoueurTrouvé=1
  if JoueurTrouvé==0:
    res=None
  return res
"""
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
  

def prendrePionPlateau(plateau,lin,col,numJoueur):
  carteConsidéréé=getVal(plateau['plateau'],lin,col)
  carteConsidéréé['pions'].remove(numJoueur)
      
"""
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
"""

def poserPionPlateau(plateau,lin,col,numJoueur):
  carteConsidéréé=getVal(plateau['plateau'],lin,col)
  carteConsidéréé['pions'].append(numJoueur)

"""
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
"""
  


def accessible(plateau,ligD,colD,ligA,colA):
  plateauConsidérée=plateau['plateau']
  """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin,
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass

if __name__ == '__main__':
  plateau1 = Plateau(4,25)
  print(prendreTresorPlateau(plateau1,2,0,3))
  print(getCoordonneesTresor(plateau1,100))
  print(getCoordonneesJoueur(plateau1,5))
  print(prendrePionPlateau(plateau1,6,0,3))