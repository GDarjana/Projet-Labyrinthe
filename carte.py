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
  w=c['nord']
  x=c['est']
  y=c['sud']
  z=c['ouest']
  c['nord']=z
  c['est']=w
  c['sud']=x
  c['ouest']=y
  return c 
"""fait tourner la carte dans le sens horaire
paramètres: c une carte
Cette fonction modifie la carte mais ne retourne rien    
"""    

def tournerAntiHoraire(c):
  w=c['nord']
  x=c['est']
  y=c['sud']
  z=c['ouest']
  c['nord']=x
  c['est']=y
  c['sud']=z
  c['ouest']=w

"""
fait tourner la carte dans le sens anti-horaire
paramètres: c une carte
Cette fonction modifie la carte mais ne retourne rien    
"""
def tourneAleatoire(c):
  for i in range(random.randrange(10)):
    tournerHoraire(c)
  return c

"""
faire tourner la carte d'un nombre de tours aléatoire
paramètres: c une carte
Cette fonction modifie la carte mais ne retourne rien    
"""

def coderMurs(c):
  dicoBinaire={'bN':c['nord'],'bE':c['est'],'bS':c['sud'],'bO':c['ouest']}
  codeListe=[]
  code=0
  j=3
  listeBool=dicoBinaire.values()
  for elem in reversed(listeBool):
    if elem == True:
      codeListe.append(1)
    else:
      codeListe.append(0)
  for binaire in codeListe:
    code+=binaire*(2**j)
    j=j-1
  return code
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
  
def decoderMurs(c,code):
  resBinaire=bin(code).replace("0b","")
  listeBinaire=[]
  listeCardinal=['ouest','sud','est','nord']
  for x in resBinaire:
    listeBinaire.append(x) 
  while len(listeBinaire)<4:
    listeBinaire.insert(0,'0')
  for i in range(len(listeCardinal)):
      if listeBinaire[i]=='1':
        c[listeCardinal[i]]=True
      else:
        c[listeCardinal[i]]=False
  return c 
"""
positionne les murs d'une carte en fonction du code décrit précédemment
paramètres c une carte
code un entier codant les murs d'une carte
Cette fonction modifie la carte mais ne retourne rien
"""    

def toChar(c):
  indice=coderMurs(c)
  for i in range(len(listeCartes)):
    if i==indice:
      return listeCartes[i]
"""
fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce
script)
paramètres c une carte
"""

def passageNord(carte1,carte2):
  passage=False
  if carte2['sud']==False:
    if carte1['nord']==False:
      passage=True
  return passage

"""
suppose que la carte2 est placée au nord de la carte1 et indique
s'il y a un passage entre ces deux cartes en passant par le nord
paramètres carte1 et carte2 deux cartes
résultat un booléen
"""

def passageSud(carte1,carte2):
  passage=False
  if carte1['sud']==False:
    if carte2['nord']==False:
      passage=True
  return passage


"""
suppose que la carte2 est placée au sud de la carte1 et indique
s'il y a un passage entre ces deux cartes en passant par le sud
paramètres carte1 et carte2 deux cartes
résultat un booléen
"""
 
def passageOuest(carte1,carte2):
  passage=False
  if carte2['est']==False:
    if carte1['ouest']==False:
      passage=True
  return passage
"""
suppose que la carte2 est placée à l'ouest de la carte1 et indique
s'il y a un passage entre ces deux cartes en passant par l'ouest
paramètres carte1 et carte2 deux cartes
résultat un booléen
"""
    

def passageEst(carte1,carte2):
  passage=False
  if carte2['ouest']==False:
    if carte1['est']==False:
      passage=True
  return passage
"""
suppose que la carte2 est placée à l'est de la carte1 et indique
s'il y a un passage entre ces deux cartes en passant par l'est
paramètres carte1 et carte2 deux cartes
résultat un booléen    
"""





if __name__=="__main__":
  carte1=Carte(True,False,False,False,3)
  carte2=Carte(False,True,True,False)
  carte3=Carte(False,True,True,False,4,[])
  carte4=Carte(False,False,False,True)
  carte5=Carte(True,False,True,False)
  carte6=Carte(False,False,False,True)
  carte7=Carte(True,True,False,False)
  carteDecoder=Carte(True,True,False,False)

  carteGraph=Carte(False,False,True,False)

  carte10=Carte(False,True,False,True)
  carte11=Carte(True,False,True,False)

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


  print(carte4)
  print(tournerHoraire(carte4))
  print(tournerAntiHoraire(carte5))

  print(tourneAleatoire(carte6))

  print(coderMurs(carte7))


  print(decoderMurs(carte7,3))

  print(decoderMurs(carteDecoder,12))

  print(toChar(carteGraph))
  
  print(passageNord(carte10,carte11))
  print(passageSud(carte10,carte11))


  print(passageOuest(carte10,carte11))
  print(passageEst(carte10,carte11))
  
"""TEST COMMIT"""