#Menu pour choisir les différents
import random
def jeux():
    jeu=int(input("Choississez le jeu: 1:juste prix; 1.2 : Nombre Mystère; 2:allumette ; 3:Jupiter Green ; 4:chasse au trésor "))
    if jeu==1:
        def JustePrix():
            """
            Cette fonction permet de jouer au juste prix
            """
            choix=int(input("Si vous voulez jouer, notez 1, sinon pour faire jouer l'ordi, notez 2: "))
            Trouvé=False
            if choix==2:
                nombreMystère = int(input("Entrez un nombre entre 1 et 1000:"))#Le joueur choisit manuellement un nombre entre 1 et 1000
                Trouve = False #On définit une valeur booléenne
                nombreDessais = 0
                IntervalleBas = 0
                IntervalleHaut = 1000 #On définit l'intervalle de valeur possible

                while nombreDessais <= 10 and Trouve == False : #On pose une condition tant que prennant en compte le nombre d'essais et la valeur booléenne "Trouve"
                    nombreRobot = random.randint(IntervalleBas,IntervalleHaut) #Ici le robot va d'abord choisir une valeur aléatoire entre 1 et 1000
                    print(nombreRobot)
                    if nombreRobot > nombreMystère : #Comme pour avant, on test les différentes options
                        print("Le nombre est plus petit\n")
                        nombreDessais += 1
                        IntervalleHaut = nombreRobot #Ici, on définit un nouvel intervalle (nouvelle valeur maximale) pour que se soit plus facile pour l'ordinateur
                        Trouve = False

                    elif nombreRobot < nombreMystère :
                        print("Le nombre est plus grand\n")
                        nombreDessais = nombreDessais + 1
                        IntervalleBas = nombreRobot #Pareil que pour avant sauf que ici on change juste la valeur minimale
                        Trouve = False

                    else :
                        print("L'ordinateur à trouvé le juste prix!\n") #Cette condition permet de stopper le jeu avec l'attribut break lorsque l'ordinateur trouve la bonne valeur, elle revoit également le nombre de tentatives faites par celui ci
                        nombreDessais = nombreDessais + 1
                        print(nombreDessais)
                        Trouve = True
                        break

                    if nombreDessais >= 10 :
                        print("L'ordinateur n'a pas deviné le juste prix\n")

            elif choix==1.2:

                for i in range(1):
                    NombreMystère = random.randint(1,1000)
                    print(NombreMystère)
                    #Ici on génère le nombre aléatoire entre 1 et 1000 que le candidat va devoir trouver

                for i in range(1, 11) : #Ici nous allons faire une boucle qui va se répéter 10 fois, ainsi, le programme s'arrête automatiquement à 10 tentatives
                    prop = int(input("Entrez votre proposition:")) #Variable permettant au candidat de rentrer le nombre qu'il souhaite proposer
                    if prop > NombreMystère : # Puis on test les différentes possibilités
                        print("Le prix est plus petit\n")
                        nombreDessais = nombreDessais + 1 #On met donc en place un compteur permettant de savoir le nombre de tentatives du candidat

                    elif prop < NombreMystère :
                        print("Le prix est plus grand\n")
                        nombreDessais = nombreDessais + 1

                    else :
                        print("Vous avez deviné le juste prix !\n")
                        nombreDessais = nombreDessais + 1
                        print(nombreDessais)
                        break # Arrête automatiquement le programme si le candidat devine le nombre avant les 10 tentatives possibles

                    if nombreDessais >= 10 :
                        print("Vous n'avez pas réussi à trouver le juste prix\n") #Affiche un petit message pour indiquer au candidat qu'il a perdu, s'affiche uniquement si le nombre de tentatives est supérieur à 10
    if jeu==2:
        def jeu_allu():
            """
            Cette fonction permet de jouer au jeu d'allumette seul ou à 2
            """
            nb_allumettes=21 #On définit quelques notions de bases
            nombre_j=int(input("Si vous êtes seul pour jouez, notez 1, si vous êtes 2, notez 2: "))
            Perdu=False
            allu_restant=[]
            allu= '|'
            if nombre_j==2: #Si il y a 2 joueurs
                while Perdu==False:
                    if nb_allumettes>0:
                        nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes"))#On demande le nombre d'allumette à enlever

                        if nombre_enl>3 or nombre_enl<1: #Affiche un message d'erreur et redemande le nb d'allumettes à enlever si le chiffre n'est pas compris dans ce qu'on attend
                            print("Mauvais nombre d'allumette à enlever")
                            nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes"))

                        if nombre_enl>nb_allumettes: #On demande d'enlever un + petit nombre d'allumettes si le nb précédent est supérieur au nb restant d'allumettes
                            nombre_enl=int(input("Donnez un nombre d'allumette plus petit à enlever"))
                        nb_allumettes=nb_allumettes-nombre_enl

                        for i in range (nb_allumettes): #On ajoute dans une variable les allumettes restantes et on l'affiche
                            allu_restant.append(allu)
                        print (allu_restant)
                        allu_restant=[] #On remet à 0 la variable

                        if nb_allumettes<=0: #On affiche la victoire du Joueur 2 et on arrête le jeu
                            Perdu=True
                            print("Bravo Joueur 2, vous avez gagnez !")

                    if nb_allumettes>0: #On fait la même chose pour le joueur 2
                        nombre_enl=int(input("Joueur 2, enlevez 1, 2 ou 3 allumettes"))

                        if nombre_enl>3 or nombre_enl<1:
                            print("Mauvais nombre d'allumette à enlever")
                            nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes"))
                        nb_allumettes=nb_allumettes-nombre_enl

                        for i in range (nb_allumettes):
                            allu_restant.append(allu)
                        print (allu_restant)
                        allu_restant=[]

                        if nb_allumettes<=0: #On affiche la victoire du joueur 1 et on arrête le jeu
                            Perdu=True
                            print("Bravo Joueur 1, vous avez gagnez !")

            if nombre_j==1: #Si il y a qu'un seul joueur
                joueur_commence=input("Si vous voulez commencez en premier, mettez oui, sinon mettez non: ") #On demande au joueur si il veut enlever les allumettes en premier
                if joueur_commence=="oui" or joueur_commence=="Oui": #Si le joueur veut commencer :
                    while Perdu==False:
                        if nb_allumettes>0:
                            nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes")) #On demande le nombre d'allumette à enlever

                            if nombre_enl>3 or nombre_enl<1: #Affiche un message d'erreur et redemande le nb d'allumettes à enlever si le chiffre n'est pas compris dans ce qu'on attend
                                print("Mauvais nombre d'allumette à enlever")
                                nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes"))

                            if nombre_enl>nb_allumettes: #On demande d'enlever un + petit nombre d'allumettes si le nb précédent est supérieur au nb restant d'allumettes
                                nombre_enl=int(input("Donnez un nombre d'allumette plus petit à enlever"))
                            nb_allumettes=nb_allumettes-nombre_enl

                            for i in range (nb_allumettes): #On ajoute dans une variable les allumettes restantes et on l'affiche
                                allu_restant.append(allu)
                            print (allu_restant)
                            allu_restant=[] #On remet à 0 la variable

                            if nb_allumettes<=0: #On affiche que le joueur à perdu si le nb d'allumettes atteint 0
                                Perdu=True
                                print("Dommage, vous avez perdu !")

                        if nb_allumettes>0: #Et on fais jouer le robot

                            nombre_enl=random.randint(1,3)
                            nb_allumettes=nb_allumettes-nombre_enl

                            if nb_allumettes>0: #Si le nb d'allumettes restantes est supérieur à 0, on affiche le restant
                                for i in range (nb_allumettes):
                                    allu_restant.append(allu)
                                print (allu_restant)
                                allu_restant=[]

                            else: #Sinon le joueur à gagner
                                Perdu=True
                                print("Bravo, vous avez gagnez !")


                if joueur_commence=="non" or joueur_commence=="Non": #Et on fais la même chose que comme si le joueur avait commencé, on inverse juste l'ordre de jeu
                    while Perdu==False:
                        if nb_allumettes>0:
                            nombre_enl=random.randint(1,3)
                            nb_allumettes=nb_allumettes-nombre_enl

                            if nb_allumettes>0:
                                for i in range (nb_allumettes):
                                    allu_restant.append(allu)
                                print (allu_restant)
                                allu_restant=[]

                            else:
                                Perdu=True
                                print("Bravo, vous avez gagnez !")

                        if nb_allumettes>0:

                            nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes"))

                            if nombre_enl>3 or nombre_enl<1:
                                print("Mauvais nombre d'allumette à enlever")
                                nombre_enl=int(input("Joueur 1, enlevez 1, 2 ou 3 allumettes"))

                            if nombre_enl>nb_allumettes:
                                nombre_enl=int(input("Donnez un nombre d'allumette plus petit à enlever"))
                            nb_allumettes=nb_allumettes-nombre_enl

                            for i in range (nb_allumettes):
                                allu_restant.append(allu)
                            print (allu_restant)
                            allu_restant=[]

                            if nb_allumettes<=0:
                                Perdu=True
                                print("Dommage, vous avez perdu !")

    if jeu==3:
        def multiples(n,nmax):
            """
            Cette fonction permet d'avoir les multiples de n jusqu'à n_max
            """
            l=[]
            for i in range(2,nmax+1):
                if n*i <= nmax:
                    l.append(n*i)
            return l

        def diviseurs(n,nmax):
            """
            Cette fonction permet d'avoir les diviseurs de n
            """
            l=[]
            for i in range(2,nmax/2):
                if n%i ==0:
                    l.append(int(n/i))
            return l

        def union(E1, E2) :
            """
            Cette fonction permet d'unir 2 ensembles
            """
            l= E1+E2
            l.sort()
            return l

        def filtres(E1, E2):
            M2=[]
            for i in range(len(M)):
                M2.append(M[i])
                for j in range(len(R)):
                    if M[i]==R[j]:
                        del M2[-1]
            return(M2)
        def Jupiter_Green():
            """
            Cette fonction permet de jouer au Jupiter Green
            """
            n_max = int(input("avec quel valeur maximale voulez vous jouer : ")) #on définit jusqu'à où on veut jouer
            l = [i for i in range(1,n_max+1)]
            print("nombres valides : ",l) #on affiche les nombres
            nbr_utilise = []
            n = 1
            while n%2 != 0:
                n = int(input("quel valeur vous choisissez : ")) #on oblige à choisir un nombre pair
            joueur = 1
            jeux = union(diviseurs(n,n_max+1),multiples(n,n_max+1)) #on cherche les diviseurs et les produits de n
            nbr_utilise.append(n)
            l = filtres(jeux,nbr_utilise) #on met dans la liste les nombres valide
            print("nombres valides :", l)
            n = int(input("quel est votre choix ? "))
            joueur += 1
            while n in jeux: #et on tourne le jeu jusqu'à que ça se termine
                jeux = union(diviseurs(n,n_max+1),multiples(n,n_max+1))
                nbr_utilise.append(n)
                l=filtres(jeux,nbr_utilise)
                if l!=[]:
                    print("nombres valides :", l)
                    n = int(input("quel chiffre voulez vous selectioner ? "))
                else:
                    n = n_max+1
                joueur += 1
            if joueur%2 == 0:
                print("le joueur 2 a gagné!")
            else :
                print("le joueur 1 a gagné!")
    if jeu==4:
        def chasse_tré ():
            """
            Cette fonction permet de jouer à une chasse au trésor avec un ordinateur. Les règles sont simples: si vous cherchez le trésor, vous devez mettre une position comme un couple et vous avez le droit jusqu'à 10 essais. SI vous faites chercher le trésor à l'ordinateur, il suffit de mettre une position aléatoire"
            Pour faciliter le jeu, nous limitons la position minimum à (-99, 99) et la position maximum à (99, 99)
            """
            choix=int(input("Voulez-vous cherchez ou faire chercher un trésor avec l'ordinateur ? Pour chercher, marquez 1, sinon marquer 2 "))

            Trouvé= False
            essais=0

            if choix==1:
                x_trésor=random.randint(-99,99) #Pour faciliter le programme ainsi que les recherches, nous limitons le minimum pour la longitude et la latitude à -99

                                                #Ainsi que le maximum à 99
                y_trésor=random.randint(-99,99)

                while Trouvé==False and essais<10: #On joue au jeu jusqu'à que le joueur est trouvé, ou pas
                    x_joueur=int(input("Donnez un chiffre entier entre -99 inclus et 99 inclus (Latitude)"))
                    y_joueur=int(input("Donnez un chiffre entier entre -99 inclus et 99 inclus (Longitude)"))

                    if x_joueur==x_trésor and y_joueur==y_trésor:
                        Trouvé= True
                        print("gagné")
                    if x_joueur!=x_trésor: #Ici, on indique où doit aller le joueur pour la latitude si elle n'est pas bonne
                        if x_joueur<x_trésor:
                            print("Plus à droite")
                        else:
                            print("Plus à gauche")
                    else:
                        print("Vous avez la bonne latitude")
                    if y_joueur!=y_trésor: #Ici, on indique où doit aller le joueur pour la longitude si elle n'est pas bonne
                        if y_joueur<y_trésor:
                            print ("Plus en haut")
                        else:
                            print ("Plus en bas")
                    else:
                        print ("Vous avez la bonne longitude")
                    essais= essais + 1

                if Trouvé==False:
                    print("Perdu")

            elif choix==2:
                x_tré_jou=int(input("Donnez un nombre entre -99 et 99 inclus(Latitude)"))#ici nous choisissons les coordonnées du trésors
                y_tré_jou=int(input("Donnez un nombre entre -99 et 99 inclus(Longitude)"))
                x_ordi=random.randint(-99,99) #Ici, l'ordinateur essais de deviner
                y_ordi=random.randint(-99,99)
                essais=1
                if x_ordi==x_tré_jou and y_ordi==y_tré_jou:
                    print ("L'ordinateur à gagné")
                    Trouvé=True
                else:

                    while Trouvé==False and essais<10: #Ici, on fais tourner le jeu jusqu'à que l'ordinateur trouve, ou pas
                        if x_ordi<x_tré_jou:        #L'ordinateur devine en faisant une recherche dichotomique
                            x_ordi=(x_ordi+99)/2
                        else:
                            x_ordi=(-99+x_ordi)/2
                        if y_ordi<y_tré_jou:
                            y_ordi=(99+y_ordi)/2
                        else:
                            y_ordi=(-99+y_ordi)/2
                        if x_ordi==x_tré_jou and y_ordi==y_tré_jou:
                            Trouvé=True
                        essais+=1
                    if Trouvé==False:
                        print("L'ordinateur à perdu")
            else:
                print("Mauvais chiffre choisis")


