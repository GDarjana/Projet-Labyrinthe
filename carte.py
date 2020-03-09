# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random
"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']
c=random.choice(listeCartes)

def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
  c={'nord': nord , 'est': est , 'sud' : sud , 'ouest':ouest,'trésor':tresor,'pions': pions}
  return c
  """
  permet de créer une carte:
  paramètres:
  nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
  tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
  pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
  """
 

def estValide(c):
  cpt=0
  res=True
  for cle,valeur in c.items():
    if cle in ['nord','est','sud','ouest']:
      if valeur == True:
        cpt +=1
  if cpt>2:
    res=False
  return res
  """
  retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
  paramètre: c une carte
  """

def murNord(c):
 return c['nord']
"""
retourne un booléen indiquant si la carte possède un mur au nord
paramètre: c une carte
"""


def murSud(c):
  return c['sud']
  """
  retourne un booléen indiquant si la carte possède un mur au sud
  paramètre: c une carte
  """


def murEst(c):
  return c['est']
  """
  retourne un booléen indiquant si la carte possède un mur à l'est
  paramètre: c une carte
  """

def murOuest(c):
  return c['ouest'] 
  """
  retourne un booléen indiquant si la carte possède un mur à l'ouest
  paramètre: c une carte
  """

def getListePions(c):
  return c['pions']
  """
  retourne la liste des pions se trouvant sur la carte
  paramètre: c une carte
  """
def setListePions(c,listePions):
  if len(listePions)<=4:
    for pions in listePions:
      c['pions'].append(pions)
  else:
    print('Le nombre de pions ne doit pas dépasser 4')
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """

def getNbPions(c):
  return len(c['pions'])
  """
  retourne le nombre de pions se trouvant sur la carte
  paramètre: c une carte
  """

def possedePion(c,pion):
  res=False
  if pion in c['pions']:
      res=True
  return res
  """
  retourne un booléen indiquant si la carte possède le pion passé en paramètre
  paramètres: c une carte
  pion un entier compris entre 1 et 4
  """



def getTresor(c):
  return c['trésor']
  """
  retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
  paramètre: c une carte
  """

def prendreTresor(c):
  return c.pop('trésor')
  """
  enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
  paramètre: c une carte
  résultat l'entier représentant le trésor qui était sur la carte
  """

def mettreTresor(c,tresor):
  ancienTrésor=c['trésor']
  c['trésor']=tresor
  return ancienTrésor
  """
  met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
  paramètres: c une carte
  tresor un entier positif
  résultat l'entier représentant le trésor qui était sur la carte
  """

def prendrePion(c, pion):
  nouvelleListeDePions=c['pions']
  for i in range(len(nouvelleListeDePions)-1):
    if nouvelleListeDePions[i]==pion:
      del nouvelleListeDePions[i]
  """
  enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
  paramètres: c une carte
   pion un entier compris entre 1 et 4
  Cette fonction modifie la carte mais ne retourne rien
  """
def poserPion(c, pion):
  if pion not in c['pions']:
    c['pions'].append(pion)
  """
  pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
  paramètres: c une carte
  pion un entier compris entre 1 et 4
  Cette fonction modifie la carte mais ne retourne rien
  """
def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    pass

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    pass
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    pass

def coderMurs(c):
  
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    pass

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    pass


def toChar(c):
  carTrouvé='Ø'
  for x in listeCartes:
    if c==x:
      carTrouvé=x
  return carTrouvé
  """
  fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
  paramètres c une carte
  """

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    pass



if __name__=="__main__":
  carte1=Carte(True,False,False,False,3)
  carte2=Carte(False,True,True,False)
  carte3=Carte(False,True,True,False,4,[])
  print(estValide(carte1))
  print(estValide(carte2))
  
  print(murNord(carte1))
  print(murNord(carte2))
  
  print(getListePions(carte3))
  setListePions(carte3,[1,2,3,4])
  print(carte3)
  
  print(getNbPions(carte3))
  print(possedePion(carte3,3))
  
  print(getTresor(carte3))
  print(prendreTresor(carte3))
  print(carte3)

  print(mettreTresor(carte1,2))
  print(carte1)


  prendrePion(carte3,1)
  print(carte3)
  poserPion(carte3,1)
  print(carte3)
