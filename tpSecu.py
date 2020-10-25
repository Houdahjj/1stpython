import hashlib


#fonction qui retourne le mot de passe crypté en md5

def cryptage(mdp):
    mdp_crypted = hashlib.md5(mdp.encode('utf-8')).hexdigest()
    return mdp_crypted

#fonction qui crypte le prénom et verifie si elle est égale au mot de passe

def test(prenom, mdp):
    if cryptage(prenom) == mdp:
        return True
    else:
        return False

#Certains utilisent leur prénom avec optionnellement des nombres rajoutés (maximum 4) devant ou derrière, avec ou sans une majuscule a la première lettre de leur prénom

def prenom_num(prenom,mdp):

    maj = prenom[0].upper() + prenom[1:]
    if test(maj, mdp):
        return maj
    elif test(prenom, mdp):
        return prenom

    for i in range(10000):
        if test(prenom + str(i), mdp):
            return prenom + str(i)

        elif test(maj + str(i), mdp):
            return maj + str(i)

        elif test(str(i) + prenom, mdp):
            return str(i) + prenom

        elif test(str(i) + maj, mdp):
            return str(i) + maj
    return False


def prenom_num_lettre(prenom,mdp):
    maj = prenom[0].upper() + prenom[1:]
    i = ord('a')
    while i <= 26:
        if test(chr(i) + maj, mdp):
            return chr(i) + maj
        elif test(chr(i).upper() + maj, mdp):
            return chr(i).upper() + maj
        elif test(chr(i) + prenom, mdp):
            return chr(i) + prenom
        elif test(chr(i).upper() + prenom, mdp):
            return chr(i).upper() + prenom
        i = i + 1

    i = ord('a')
    while i <= ord('a') + 26:
        for j in range(10000):
            if test(chr(i) + prenom + str(j), mdp):
                return chr(i) + prenom + str(j)

            elif test(chr(i).upper() + prenom + str(j), mdp):
                return chr(i).upper() + prenom + str(j)

            elif test(chr(i) + maj + str(j), mdp):
                return chr(i) + maj + str(j)

            elif test(chr(i).upper() + maj + str(j), mdp):
                return chr(i).upper() + maj + str(j)

            elif test(str(j) + chr(i) + prenom, mdp):
                return str(j) + chr(i) + prenom

            elif test(str(j) + chr(i).upper() + prenom, mdp):
                return str(j) + chr(i).upper() + prenom


            elif test(str(j) + chr(i) + maj, mdp):
                return str(j) + chr(i) + maj

            elif test(str(j) + chr(i).upper() + maj, mdp):
                return str(j) + chr(i).upper() + maj
        i = i + 1
    return False


def animal(mdp):
    for i in tab_dico_animaux :
        if test(i.rstrip(), mdp):
            return i.rstrip()
    return False


def deux_animaux(mdp):  # Certains ont utilisés la concaténation de 2 animaux

    for i in tab_dico_animaux :
        for j in tab_dico_animaux :
            if test(i.rstrip() + j.rstrip(), mdp):
                return i.rstrip() + j.rstrip()
    return False


def animal_num(mdp):

    for j in tab_dico_animaux :
        j = j.rstrip()
        maj = j[0].upper() + j[1:]
        for i in range(1000):
            if test(j + str(i), mdp):
                return j + str(i)

            elif test(maj + str(i), mdp):
                return maj + str(i)

            elif test(str(i) + j, mdp):
                return str(i) + j

            elif test(str(i) + maj, mdp):
                return str(i) + maj
    return False


def animal_deform(
        mdp):  # Certains prennent le nom d'un animal, le mettent à l'envers, et le dédoublent./Certains concatènent 2 fois le nom d'un animal mis à l'envers
    for i in tab_dico_animaux :
        i = i.rstrip()
        i = i[::-1]
        if test(i + i, mdp):
            return i + i
    return False


def deux_animaux_verso(mdp):  # Certains concatènent le nom d'un animal et le nom d'un autre animal mis à l'envers

    for i in tab_dico_animaux :
        i = i.rstrip()
        for j in tab_dico_animaux :
            j = j.rstrip()
            j = j[::-1]
            if test(i + j, mdp):
                return i + j
    return False


def double_animal_verso(mdp):
    for i in tab_dico_animaux :
        i = i.rstrip()
        i = i[::-1]
        for j in tab_dico_animaux :
            j = j.rstrip()
            j = j[::-1]
            if test(i + j, mdp):
                return i + j
    return False


def alternance(prenom, mdp):  # Certains alternent les minuscules et majuscules dans leur prénom
    val = list(prenom)
    val1 = list(prenom)
    j = 0
    for i in prenom:
        if j % 2 == 0:
            val[j] = i.upper()
        j = j + 1

    val = ''.join(val)
    if test(val, mdp):
        return val


    for i in prenom:
        if j % 2 != 0:
            val1[j] = i.upper()
        j = j + 1

    val1 = ''.join(val1)
    if test(val1, mdp):
        return val1

    return False

#--MAIN--
dico_animaux = open("dico_animaux.txt","r")
tab_dico_animaux = dico_animaux.readlines()

fichier_mdp = open("MDP.txt","r")
tab_mdp = fichier_mdp.readlines()

fichier_prenom = open("Nom_Etudiants.txt","r")
tab_prenom = fichier_prenom.readlines()

for i in tab_prenom:
    for j in tab_mdp:
        print(prenom_num_lettre(i,j))








