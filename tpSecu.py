import hashlib


def hachage(mdp) :              #crypte mdp en md5
    hMdp=hashlib.md5(mdp.encode('utf-8')).hexdigest()
    return hMdp

def verif(prenom, mdp) :        #crypte prénom et vérifie si c'est égale à mdp
    if hachage(prenom)==mdp :
        return True
    else :
        return False


def fonc1(prenom, mdp) :     #Certains utilisent leur prénom avec optionnellement des nombres rajoutés (maximum 4) devant ou derrière, avec ou sans une majuscule a la première lettre de leur prénom
    
    maj=prenom[0].upper()+prenom[1:]
    if verif(maj, mdp) :
        return maj
    elif verif(prenom, mdp) :
        return prenom
    
    for i in range(10000) :
        if verif(prenom+str(i),mdp) :
            return prenom+str(i)
        
        elif verif(maj+str(i),mdp) :
            return maj+str(i)
        
        elif verif(str(i)+prenom,mdp) :
            return str(i)+prenom
        
        elif verif(str(i)+maj,mdp) :
            return str(i)+maj
    return False

def fonc2(prenom, mdp) :     #Certains font la même chose mais on rajouter une lettre (min ou maj) devant leur prénom avant.
    maj=prenom[0].upper()+prenom[1:]
    i=ord('a')
    while i<=26 :
        if verif(chr(i)+maj, mdp) :
            return chr(i)+maj
        elif verif(chr(i).upper()+maj, mdp) :
            return chr(i).upper()+maj
        elif verif(chr(i)+prenom, mdp) :
            return chr(i)+prenom
        elif verif(chr(i).upper()+prenom, mdp) :
            return chr(i).upper()+prenom
        i=i+1
    
    i=ord('a')
    while i<=ord('a')+26 :
        for j in range(10000) :
            if verif(chr(i)+prenom+str(j),mdp) :
                return chr(i)+prenom+str(j)
            
            elif verif(chr(i).upper()+prenom+str(j),mdp) :
                return chr(i).upper()+prenom+str(j)
            
            elif verif(chr(i)+maj+str(j),mdp) :
                return chr(i)+maj+str(j)
            
            elif verif(chr(i).upper()+maj+str(j),mdp) :
                return chr(i).upper()+maj+str(j)
        
            elif verif(str(j)+chr(i)+prenom,mdp) :
                return str(j)+chr(i)+prenom
            
            elif verif(str(j)+chr(i).upper()+prenom,mdp) :
                return str(j)+chr(i).upper()+prenom
            
        
            elif verif(str(j)+chr(i)+maj,mdp) :
                return str(j)+chr(i)+maj
            
            elif verif(str(j)+chr(i).upper()+maj,mdp) :
                return str(j)+chr(i).upper()+maj
        i=i+1
    return False

def fonc3(mdp) :      #Certains utilisent un nom d'animal
    for i in tab :
        if verif(i.rstrip(),mdp) :
            return i.rstrip()
    return False

def fonc4(mdp) :     #Certains ont utilisés la concaténation de 2 animaux
     
    for i in tab :
        for j in tab :
            if verif(i.rstrip()+j.rstrip(),mdp) :
                return i.rstrip()+j.rstrip()
    return False

def fonc5(mdp) :    #Certains ont utilisé le nom d'un animal et lui ont rajoutés des chiffres devant ou derrière (max 3) avec ou sans une majuscule a la première lettre de l'animal
    
    for j in tab :
        j=j.rstrip() 
        maj=j[0].upper()+j[1:]
        for i in range(1000) :
            if verif(j+str(i),mdp) :
                return j+str(i)
            
            elif verif(maj+str(i),mdp) :
                return maj+str(i)
            
            elif verif(str(i)+j,mdp) :
                return str(i)+j
            
            elif verif(str(i)+maj,mdp) :
                return str(i)+maj
    return False


  
def fonc6(mdp) :    #Certains prennent le nom d'un animal, le mettent à l'envers, et le dédoublent./Certains concatènent 2 fois le nom d'un animal mis à l'envers
    for i in tab :
        i=i.rstrip()
        i=i[::-1]
        if verif(i+i,mdp) :
            return i+i
    return False


def fonc7(mdp) :   #Certains concatènent le nom d'un animal et le nom d'un autre animal mis à l'envers
    
    for i in tab :
        i=i.rstrip()
        for j in tab :
            j=j.rstrip()
            j=j[::-1]
            if verif(i+j,mdp) :
                return i+j
    return False
    
            
def fonc8(mdp) :  
    
    for i in tab :
        i=i.rstrip()
        i=i[::-1]
        for j in tab :
            j=j.rstrip()
            j=j[::-1]
            if verif(i+j,mdp) :
                return i+j
    return False

def fonc9(prenom,mdp) :  #Certains alternent les minuscules et majuscules dans leur prénom
    val=list(prenom)
    val1=list(prenom)
    j=0
    for i in prenom :
        if j%2==0 :
            val[j]=i.upper()
        j=j+1
    
    val=''.join(val)
    if verif(val,mdp) :
        return val
    
    j=0
    
    for i in prenom :
        if j%2!=0 :
            val1[j]=i.upper()
        j=j+1
    
    val1=''.join(val1)
    if verif(val1,mdp) :
        return val1
    
    return False

liste_mdp=["67ca881ef876c622c093419d0d8dbe13","14bfcc4be324181b91812b0b2f70ce40","e11f4bff1b9aa4c9b65224295dd22e16","42167255eb290439c4200edfe3639ab5","a9b0cd97f83f9251411af4b5f1f0bd59","6c69a73f35abf6c80c88f1e3801ca150","4eb01b0c1900c192da5c2aba253de3c0","a409f32fef1cc24d4fbe7256accf8eb9","8699fc754c2e40dc7ef0ca9634b92d17","4bda49907d7f2d949d6ba4ff299a280c","54fd8fb2eaf6b40ecd347713770e83d5"]

mon_fichier = open("dico_animaux.txt", "r") #ouvre le fichier dico_animaux et le place dans la variable mon_fichier
tab=mon_fichier.readlines()   #transforme le fichier en tableau


######      TEST
print(fonc1("vivien","54fd8fb2eaf6b40ecd347713770e83d5"))  # 167vivien
print(fonc2("abdelkarim","67ca881ef876c622c093419d0d8dbe13")) # WAbdelkarim1989
print(fonc3("a409f32fef1cc24d4fbe7256accf8eb9"))  # hippocampe
print(fonc4("14bfcc4be324181b91812b0b2f70ce40"))  # chatchien
print(fonc5("a9b0cd97f83f9251411af4b5f1f0bd59"))  # marsouin89
print(fonc5("e11f4bff1b9aa4c9b65224295dd22e16"))  # 17Poney
print(fonc5("8699fc754c2e40dc7ef0ca9634b92d17"))  # 673crabe
print(fonc6("42167255eb290439c4200edfe3639ab5"))  # nipalnipal
print(fonc7("4bda49907d7f2d949d6ba4ff299a280c"))  # crevetteteluop
print(fonc9("vincent","4eb01b0c1900c192da5c2aba253de3c0")) #ViNcEnT


    
    
    

    



