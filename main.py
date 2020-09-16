import os
import re

#Pb pour le moment : La regex qui detecte que si c un nombre et non pas le nb de car
#Quand on incremente ça enlève les 0
#Il faut modifier certains if en while

increment = input("Veuillez choisir un incrément : ")   #Initialisation de increment
test = re.match('\d{1,3}',increment)                    #Verification avec regex que increment est un entier sur 3 caractères max

while not test :                                        #Si le test n'est pas un entier sur 3 caractères max, rebelotte
    print("Incrément invalide")
    increment = input("Veuillez choisir un incrément : ")
    test = re.match('\d{1,3}', increment)


rep = r"renommage"
noms = os.listdir(rep)                                  #On met le repertoire dans une variable pour pouvoir le parcourir grâce à cette fonction

if test :                                               #Si test est ok, alors on lance le programme

    texte = input("Voulez-vous choisir un texte à accoler ? - répondre : oui ou non ")
    original = input("Voulez-vous garder le texte original? - répondre : oui ou non ")


    if original == 'oui' and texte =='oui' :
        texte = input("Veuillez choisir le texte à acoler ")
        nb = int(input("A partir de combien de caractères voulez vous garder l'original "))
        for nom in noms:
            if nb > len(nom)-4:                           #Tant que le nombre de caractère est plus grand que la taille du nom du fichier (-4 car pour ne pas compter l'extension
                print("Nb de caractère trop grand, recommencez")                              # on lance une erreur
                break
            nfc = os.path.join(rep, nom)                    #Nfc devient notre chemin, pour cela on concatène le nom du repertoire et chaque nom de fichier
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + '-' + texte + '-' + nom[(nb - 1):]))       #On met nfc en chemin de base car il contient le nom du répertoire/chaquefichierdudossier
                                                                                                        #En 2e argument on renomme le fichier avec les nouvelles saisies de l'utilisateur et avec la sous liste nb-1 pour savoir à partir de cb de car on garde
                increment = int(increment)               #On caste increment (str) en int pour pouvoir l'incrémenter
                increment = increment+1
                increment = str(increment)              #On recaste increment (int) en str pour pouvoir le mettre dans la fonction rename qui prend que des str

    elif original == 'oui' and texte == 'non' :
        nb = int(input("A partir de combien de caractères voulez vous garder l'original "))
        for nom in noms:
            if nb > len(nom) - 4:
                print("Nb de caractère trop grand, recommencez")
                break
            nfc = os.path.join(rep, nom)
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + '-' + nom[(nb - 1):]))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)


    elif original == 'non' and texte == 'oui':
        texte = input("Veuillez choisir le texte à acoler ")
        new_nom = input("Veuillez choisir le nouveau texte ")
        for nom in noms:
            nfc = os.path.join(rep, nom)
            fileName, fileExtension = os.path.splitext(nfc)         #On recupere l'extention pour pas qu'elle change quand on modifie le texte
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + '-' + texte + '-' + new_nom+fileExtension))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)

    elif original == 'non' and texte == 'non':
        new_nom = input("Veuillez choisir le texte ")
        for nom in noms:
            nfc = os.path.join(rep, nom)
            fileName, fileExtension = os.path.splitext(nfc)
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment +'-' + new_nom + fileExtension))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)

    else :
            print("Nous n'avons pas compris votre choix, veuillez recommencer")







