
def grille_vide():

    #création d'un tableau de 6 lignes et 7 colones.
    return [[0]*7 for i in range(6)]

def affiche(g):

    #affiche 1 par 1 chaque case du tableau en remplacent 0 par ".", 1 par "X" et 2 par "O".
    for i in range(6):
        for j in range(7):
            if g[5-i][j]==0:
                print(".","",end="")
            elif g[5-i][j]==1:
                print("X","",end="")
            else:
                print("O","",end="")
        print()
    print()


def coup_possible(g,c):

    #test pour la plus haute ligne de la colone "c" si elle est remplie ou non et renvoie True si c'est vide.
    if g[5][c]==0:return True
    else: return False



def jouer(g,j,c):

    # trouve la ligne la plus basse pour la quelle ont peut jouer pour une colone "c".
    for i in range(6):
        if g[i][c]!=1 and g[i][c]!=2:

            #remplace le 0 par le numéro de joueur (1 ou 2).
            g[i][c]=j
            break
    return g
            

def horiz(g,j,l,c):

    if g[l][c]==j:

        #initialisation du compteur "total" pour compter le nombre de pions d'affiler d'un même joueur a l'horrizontal.
        total=1
        y=c

        #compte a droit de la colone c.
        for i in range(3):
            y+=1

            # vérification pour ne pas sortir du tableau.
            if y>6 or y<0:break
            else:
                if g[l][y]==j:
                    total+=1
                else: break

        #renvoie True si il y a une suite de 4 pions du même joueur d'affilé.
        if total>=4:
            return True

        y=c

        #compte a gauche de la colone c.
        for i in range(3):
            y-=1
            
            # vérification pour ne pas sortir du tableau.
            if y>6 or y<0:break
            else:
                if g[l][y]==j:
                    total+=1
                else:
                    break

        #renvoie True si il y a une suite de 4 pions du même joueur d'affilé.
        if total>=4: return True


def vert(g,j,l,c):

    if g[l][c]==j:

        #initialisation du compteur "total" pour compter le nombre de pions d'affiler d'un même joueur a la vertical. 
        total=1
        x=l

        #compte vers le haut.
        for i in range(3):
            x+=1

            #vérification pour ne pas sortir du tableau.
            if x>5 or x<0:break
            else:
                if g[x][c]==j:
                    total+=1
                else: 
                    break

        #renvoie True si il y a une suite de 4 pions du même joueur d'affilé.
        if total>=4: return True

        x=l

        #compte vers le bas.
        for i in range(3):
            x-=1

            # vérification pour ne pas sortir du tableau.
            if x>5 or x<0:break
            else:
                if g[x][c]==j:
                    total+=1
                else:
                    break

        #renvoie True si il y a une suite de 4 pions du même joueur d'affilé.
        if total>=4: return True


def diag(g,j,l,c):

    if g[l][c]==j:

        #vérification pour la diagonale haut gauche - bas droite.

        #initialisation du compteur "total" pour compter le nombre de pions d'affiler d'un même joueur a l'horrizontal.
        total=1
        x=l
        y=c

        #vérification vers haut gauche de c.
        for i in range(3):
            x-=1
            y+=1

            #vérification pour ne pas sortir du tableau.
            if x>5 or y>6 or x<0 or y<0:break
            else:
                if g[x][y]==j:
                    total+=1
                else: break

        if total>=4:
            return True


        x=l
        y=c

        #vérification vers bas droite de c.
        for i in range(3):
            x+=1
            y-=1

            #vérification pour ne pas sortir du tableau.
            if x>5 or y>6 or x<0 or y<0:break
            else:
                if g[x][y]==j:
                    total+=1
                else:
                    break

        if total>=4: return True

        #vérification de la diagonal bas gauche - haut droite.
        total=1
        x=l
        y=c

         #vérification vers bas gauche de c.
        for i in range (3):
            x-=1
            y-=1

            #vérification pour ne pas sortir du tableau.
            if x>5 or y>6 or x<0 or y<0:break
            else:
                if g[x][y]==j:
                    total+=1
                else: break

                #vérifie si il y a un enchainement de pions de 4 ou plus et renvoie True si c'est le cas.
            if total>=4:
                return True

        x=l
        y=c
        
         #vérification vers haut droite de c.
        for i in range(3):
            x+=1
            y+=1

            #vérification pour ne pas sortir du tableau.
            if x>5 or y>6 or x<0 or y<0:break
            else:
                if g[x][y]==j:
                    total+=1
                else: break

        #vérifie si il y a un enchainement de pions de 4 ou plus et renvoie True si c'est le cas.       
        if total>=4:
            return True
        else: return False
    else: return False



def victoire(g,j):

    #vérifie pour chaque case si il y a un alignement verticale/horizontal/diagonal et renvoie True si il y a une victoire.
    for c in range (7):
        for l in range(6):
            if  horiz(g,j,l,c) or diag(g,j,l,c) or vert(g,j,l,c)==True:
                return True
    return False



def match_nul(g):

    #vérifie si il est encore possible de jouer dans le tableau et renvoie true si c'est la cas.
    a=0
    for i in range(7):
        if g[5][i]!=0 : 
            a+=1
    if a==7: return True
    else: return False 


from random import *

def coup_aléatoire(g,j):

    #génère une colone aléatoire entre 0 et 6:
    c=randint(0,6)

    # on vérifie si le coup est possible, si se n'est pas le cas on regénère un nombre.
    while coup_possible(g,c)==False:
        c=randint(0,6)

    #on joue le coup généré aléatoirement pour le joueur "j".
    jouer(g,j,c)



def partie_bot_VS_bot():

    #initialisation de la grille:
    g=grille_vide()

    #affichage de la grille 
    affiche(g)

    #initialisation des variable utile au fonctionement du programe. 
    j=2
    c=0

    #boucle du jeux:
    while  True:
        # changment de joueur.
        if j==1:
            j=2
            #le joueur 1 joue un coup aléatoire.
            c=coup_aléatoire(g,j)
        elif j==2:
            j=1
            #le joueur 2 joue un coup aléatoire.
            c=coup_aléatoire(g,j)

        #affichage du coup jouer.
        affiche(g)

        #test si il y a une victoire puis si il a  match nul, si c'est le cas la parti s'arrête.
        if victoire(g,j)==True:
            print("le joueur ",j," a gagner la parti !!")
            break
        if match_nul(g)== True: 
            print("égalité")
            break



def partie_joueur_VS_bot():

    #initialisation de la grille vide.
    g=grille_vide()

    #affichage de la grille.
    affiche(g)

    #initialisation des variable utile au fonctionement du programe.
    j=2
    c=0

    #boucle du jeux:
    while  True:

        # changment de joueur.
        if j==1:
            j=2
            #le bot joue un coup aléatoire.
            c=coup_aléatoire(g,j)

        elif j==2:
            j=1

            #le joueur 2 entre la colone souhaité.
            # le -1 permet de ne pas avoir a calculer la colone ou l'on veut jouer.
            c=int(input("joueur 1 ou voulez-vous jouer ?  "))-1

            #vérifie si la colone éxiste.
            while c<0 or c>6:
                affiche(g)
                print("vous ne pouvez pas jouer dans une colone inéxistante")
                c=int(input("joueur 1 ou voulez-vous jouer ?  "))-1

            # vérification si le coup du joueur est possible, si ce n'est pas le cas on redemande au joueur de rentrer une nouvel colone.
            while coup_possible(g,c)==False:
                affiche(g)
                print("vous ne pouvez pas jouer dans cette colone\n")
                c=int(input("joueur 1 ou voulez-vous jouer ?  "))-1

            # le coup est jouer.
            jouer(g,j,c)

        #affichage du coup jouer.
        affiche(g)


        #test si il y a une victoire ou match nul, si c'est le cas le partie s'arrête.
        if victoire(g,j)==True:
            print("le joueur ",j," a ganger la parti !!")
            break
        if match_nul(g)== True: 
            print("égalité")
            break
        


def choisir_mode_jeux():
    # permet a l'utilisateur de choisir le mode de jeux qu'il souhaite.
    choix=int(input("mode bot VS bot : tapez 1 \nmode joueur VS bot : tapez 2 \n"))

    #lance le programme correespondant au choix de l'utilisateur.
    if choix==1:
        partie_bot_VS_bot()
    elif choix==2:
        partie_joueur_VS_bot()

choisir_mode_jeux()