import math
"""
#Hoda HAJJI

#exo1 - Breakpoint 1

temps = 6.892
distance = 19.7

vitesse = distance / temps

print("La vitesse vaut", vitesse)
print("La vitesse vaut %.1f" %vitesse)

#exo2

print("Saisir nom")
nom = str(input())
print("Saisir age")
age = int(input())
print("Vous vous appelez",nom,"Vous avez",age)

#exo3

print("Saisir flottant")
flottant = float(input())
if flottant == 0 or flottant >0 :
    print(math.sqrt(flottant))
else :
    print("erreur")

#exo4

mot1 = dict()
mot2 = dict()

print("Saisir mot 1")
mot1 = input()
print("Saisir mot 2")
mot2 = input()

if mot1<mot2 :
    print("Le plus petit est", mot1)
elif mot1==mot2 :
    print("Ils sont égaux")
else :
    print("Le plus petit est", mot2)

#exo5

pSeuil = 2.3
vSeuil = 7.41

print("Saisir volume")
volume = float(input())
print("Saisir pression")
pression = float(input())
if pression>pSeuil and volume>vSeuil :
    print("arret immediat")
elif pression>pSeuil :
    print("augmenter le volume de l'enceinte")
elif volume>vSeuil :
    print("diminuer le volume de l'enceinte")
else :
    print("Tout va bien")

#exo6

print("Saisir une chaine de caractère")

ch = str(input())
if "@" in ch and ch.endswith(".com") :
    print("email valide")

#exo 7

for i in range(10):
    print("message")

#exo8

mot = "houda"
for i in mot :
    print(i)
    
#exo 9

a = 0
b = 10
for i in range(a,b) :
    print(i)

#exo10
a = 0
b = 10
for i in range(b,a,-1) :
    if i%2==1 :
        print(i)

#exo11

print("Veuillez saisir une valeur entre 1 et 10")
val = int(input())
while val < 1 or val > 10 :
    print("Veuillez saisir une valeur entre 1 et 10")
    val = int(input())
print(val)

#exo12

ch = "houda"
liste = ['h','a','j','j','i']

for i in ch :
    print(i)
for i in liste :
    print(i)

#exo13

for i in range(0,15,3) :
    print(i)

#exo14

print("Veuillez saisir un entier n")
n = int(input())
for i in range(n) :
    if i%2==0 :
        print(i)

i=0
while i<n :
    if i%2==0 :
        print(i)
    i=i+1

#exo15

liste=[17,38,10,25,72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[2:3])
print(liste[0:2])
print(liste[3:len(liste)])
print(liste[0:len(liste)])

#exo16

ch1 = "crevette"
print(ch1[::-1])

#exo17

ch=str(input())
if(ch == ch[::-1]):
      print( ch, "est un palindrome")
else:
      print(ch, "n'est pas un palindrome")

#exo18

a = input("Saisir mail")
ch = '.'+a[-3:]
ch1 = '.'+a[-2:]
ch2 = '.'+a[-1:]
if "@" in a and "." in a and (a.endswith(ch) or a.endswith(ch1) or a.endswith(ch2)) :
    print("valide")
else :
    print("invalide")

#exo19

truc = []
machin = [0.0]*5
print(truc)
print(machin)

#exo20

for i in range(0,4) :
    print(i)
for i in range(4,8) :
    print(i)
for i in range(2,9,2) :
    print(i)
chose = [0,1,2,3,4,5]

if 3 in chose :
    print("3 est dans chose")
else :
    print("3 n'est pas dans chose")

if 6 in chose :
    print("6 est dans chose")
else :
    print("6 n'est pas dans chose")

#exo21 - Breakpoint4

x = int(input("saisir un nombre x"))
f = open("test.txt",mode="a")
for i in range(x) :
    ch = input("Saisir une chaîne de caractère : ")
    f.write(ch+"\n")
f.close()

#exo22

file = open('test.txt', "r")
for ligne in file :
    if "@" in ligne and ligne.endswith(".com\n"):
        print("C'est un email")
    else :
        print("Ce n'est pas un email")

file.close()

#exo23
def compterMots(ch) :

   ch=ch.split()
   liste=[]
   for i in range(len(dictionnaire)) :
        if dictionnaire[i]==dictionnaire[i-1] :

            liste.append(dictionnaire[i])

   return liste

print(compterMots("houda et moi houda et et bleu"))

def compterMots(ch) :
  dict={}
  for i in ch.split() :
        print(dict)
        if i in dict :
            dict[i] +=1
        else :
            dict[i] = 1
  return dict

print(compterMots('abc et la abc et petit petit chat '))

#exo24

def cube(r) :
    return r**3

def volumeSphere(r) :
    return 4 / 3 * 3.14 * cube(r)

print(volumeSphere(4))
"""
#exo25

def somme(a,b,c) :
    return a+b+c

a,b,c=(4,5,6)
print(somme(a,b,c))


