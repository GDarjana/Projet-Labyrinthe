# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
  return {'Nom' : nom, 'liste de trésor' : []}
"""
    creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
    paramètre: nom une chaine de caractères
    retourne le joueur ainsi créé
"""
  
def ajouterTresor(joueur,tresor):
  if tresor in joueur['liste de trésor']:
    pass
  else:
    if tresor > 0:
      joueur['liste de trésor'].append(tresor)  
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """
    

def prochainTresor(joueur):
  if len(joueur['liste de trésor']) <= 1:
    return None
  else:
    if joueur['liste de trésor'][1] != 0:
      return joueur['liste de trésor'][1]
    else:
      return None
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """


def tresorTrouve(joueur):
  del joueur['liste de trésor'][0]
  """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
  """
    

def getNbTresorsRestants(joueur):
    nb = 0
    for i in range(len(joueur['liste de trésor'])):
      nb+=1
    return nb
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """

def getNom(joueur):
    return joueur['Nom']
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    
