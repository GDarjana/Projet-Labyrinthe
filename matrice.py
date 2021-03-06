# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~

   Ce module gère une matrice.
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
  M = []
  for ligne in range(nbLignes):
    M.append([])
    for colonne in range(nbColonnes):
      M[ligne].append(valeurParDefaut)
  return M

  """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant
    valeurParDefaut dans chacune des cases
    paramètres:
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """


def getNbLignes(matrice):
  return len(matrice)
  """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """


def getNbColonnes(matrice):
  return len(matrice[0])
  """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """


def getVal(matrice,ligne,colonne):
  if ligne <= getNbLignes(matrice) and colonne <= getNbColonnes(matrice):
    return matrice[ligne][colonne]

  """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """


def setVal(matrice,ligne,colonne,valeur):
  if ligne <= getNbLignes(matrice) and colonne <= getNbColonnes(matrice):
    matrice[ligne][colonne] = valeur

  """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """



#------------------------------------------
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
  valEject = matrice[numLig].pop(0)
  matrice[numLig].append(nouvelleValeur)
  return valEject

  """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
  valEject = matrice[numLig].pop()
  matrice[numLig].insert(0, nouvelleValeur)
  return valEject
  """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
  valEject = matrice[0][numCol]
  for i in range(len(matrice)-1):
    matrice[i][numCol] = matrice[i+1][numCol]
  del matrice[len(matrice)-1][numCol]
  matrice[len(matrice)-1].insert(numCol, nouvelleValeur)
  return valEject
  """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """


def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
  valEject = matrice[len(matrice)-1][numCol]
  for i in range(len(matrice)-1):
    matrice[-i-1][numCol] = matrice[-i-2][numCol]
  del matrice[0][numCol]
  matrice[0].insert(numCol, nouvelleValeur)
  return valEject


  """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """


if __name__ == '__main__':
  matrice = Matrice(7,7)
  print(getNbColonnes(matrice))
  print(getNbLignes(matrice))
  setVal(matrice, 1, 0, 9)
  print(matrice)
  print(getVal(matrice,1,0))
  print(decalageLigneAGauche(matrice, 1, nouvelleValeur=1))
  print(matrice)
  print(decalageLigneADroite(matrice, 1, nouvelleValeur=1))
  print(matrice)
  print(decalageColonneEnHaut(matrice, 0, nouvelleValeur=2))
  print(matrice)
  print(decalageColonneEnHaut(matrice, 0, nouvelleValeur=2))
  print(matrice)
  print(decalageColonneEnBas(matrice, 1, nouvelleValeur=4))
  print(matrice)
  print(decalageColonneEnBas(matrice, 1, 4))
  print(matrice)
