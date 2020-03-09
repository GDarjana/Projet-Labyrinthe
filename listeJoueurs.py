# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
  liste = []
  for noms in nomsJoueurs:
    liste.append(noms)
  return liste
  """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """


def ajouterJoueur(joueurs, joueur):
  joueurs.append(joueur)
  """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
  """

def initAleatoireJoueurCourant(joueurs):
  numJoueurCourant = random.randrange(len(joueurs))
  joueurs[0],joueurs[numJoueurCourant] = joueurs[numJoueurCourant],joueurs[0]
  """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
  
def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
  listeTresors = []
  i = 0
  for nb in range(1,nbTresors+1):
    listeTresors.append(nb)
  while len(listeTresors) > 0:
    tresor = random.choice(listeTresors)
    ajouterTresor(joueurs[i], tresor)
    i+=1
    if i > 3:
      i = 0
    listeTresors.remove(tresor)
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """


def changerJoueurCourant(joueurs):
  last = joueurs[0]
  del joueurs[0]
  joueurs.append(last)

  """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    

def getNbJoueurs(joueurs):
  return len(joueurs)
  """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """


def getJoueurCourant(joueurs):
  return joueurs[0]
  """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """

def joueurCourantTrouveTresor(joueurs):
  del joueurs[0]['liste de trésor'][0]
  """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """


def nbTresorsRestantsJoueur(joueurs,numJoueur):
  return joueurs[numJoueur]['liste de trésor']
  """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    pass

def nomJoueurCourant(joueurs):
  return joueurs[0]['name']
  """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    pass

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    pass

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    pass

def joueurCourantAFini(joueurs):
  res = False
  if len(joueurs[0]['liste de trésor']) == 0:
    res = True
  return res

  """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """

if __name__ == '__main__':
  joueurs = ListeJoueurs([Joueur('salut'), Joueur('bonsoir'), Joueur('aurevoir'), Joueur('yes')])
  initAleatoireJoueurCourant(joueurs)
  print(joueurs)
  distribuerTresors(joueurs)
  changerJoueurCourant(joueurs)
  print(joueurs)
  joueurCourantTrouveTresor(joueurs)
  print(joueurs)
  print(nbTresorsRestantsJoueur(joueurs,1))
  