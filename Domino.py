import math

class Domino:

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def affiche_points(self):
        print("La valeur de la face A est :", self.A, " la valeur de la face B est :", self.B)

    def totale(self):
        return self.A + self.B

    def __repr__(self):
        return "Domino: A({}), B({})".format(self.A, self.B)


class CompteBancaire:

    def __init__(self, nomT, solde=0):
        self.nomT = nomT
        self.solde = solde

    def depot(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        self.solde = self.solde - somme

    def affiche(self):
        print("le solde courant est :", self.solde)

    def __repr__(self):
        return "CompteBancaire: Solde({})".format(self.solde)


class TableMultiplication:

    def __init__(self, int, i=0):
        self.int = int
        self.i = i

    def prochain(self):
        yield self.int * self.i
        self.i = (self.i) + 1

    def __repr__(self):
        return "TableMultiplication: nb({})".format(self.int)


class Fraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def affiche(self):
        print(self.num, "/", self.denom)

    def __add__(self, obj):
        pgcd1 = math.gcd((self.num * obj.denom) + (obj.num * self.denom), (self.denom * obj.denom))
        return Fraction(((self.num * obj.denom) + (obj.num * self.denom)) / pgcd1, (self.denom * obj.denom) / pgcd1)

    def __sub__(self, obj):
        pgcd1 = math.gcd((self.num * obj.denom) - (obj.num * self.denom), (self.denom * obj.denom))
        return Fraction(((self.num * obj.denom) - (obj.num * self.denom)) / pgcd1, (self.denom * obj.denom) / pgcd1)

    def __truediv__(self, obj):
        pgcd1 = math.gcd(round(self.num / obj.num), round(self.denom / obj.denom))
        return Fraction((self.num / obj.num) / pgcd1, (self.denom / obj.denom) / pgcd1)

    def __mul__(self, obj):
        pgcd1 = math.gcd(self.num * obj.num, self.denom * obj.denom)
        return Fraction((self.num * obj.num) / pgcd1, (self.denom * obj.denom) / pgcd1)

    def __repr__(self):
        return "Fraction: num({}), denom({})".format(self.num, self.denom)


class Poly:
    def __init__(self, *args):
        self.coeff1 = []
        for i in args:
            self.coeff1.append(i)

    def coeff(self):
        return self.coeff1

    def evalue(self, val):
        somme = 0
        i = 1
        while i < len(self.coeff1):
            somme = somme + (self.coeff1[i]) * (val ** i)
            i = i + 1
        return self.coeff1[0] + somme


d = Domino(8, 5)
d.affiche_points()
print(d.totale())

c = CompteBancaire("houda", 5000)
c.depot(500)
c.retrait(300)
c.affiche()

f = Fraction(2, 6)
f.affiche()

g = Fraction(6, 9)
g.affiche()

r1 = f + g
r1.affiche()

r2 = f / g
r2.affiche()

p = Poly(1, 2, 3)
print(p.evalue(6))
