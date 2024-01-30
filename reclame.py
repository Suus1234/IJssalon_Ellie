# huiswerk van af Les 08.4-.14
from statistics import mean
from algemene_functies import mijn_functie_2


def Aanbieding_1(Smaak, Prijs, Korting):
    Korting = Prijs - (Prijs * Korting) 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {Smaak}, van {Prijs} euro voor {Korting:.2f} euro."
    return uitvoer
print(Aanbieding_1("aardbei", 4, 0.1))

def Inkomsten_Totaal():
    a = 220
    b = 430
    c = 125
    d = 160
    e = 205
    f = 90
    g = 345
    Inkomsten = a + b + c + d + e + f + g
    btw = 0.09
    btw_bedrag = btw * Inkomsten
    string = f"Het totaal van alle inkomsten van deze week is {Inkomsten:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    return string

print(Inkomsten_Totaal()) 

Mijn_lijst = (220, 430, 125, 160, 205, 90, 345)
def Laag_en_Hoog(Mijn_lijst):
    return min(Mijn_lijst), max(Mijn_lijst)
print(Laag_en_Hoog(Mijn_lijst))

def Gemiddelde():
    string = f"De gemiddelde inkomsten deze week zijn {mean(Mijn_lijst):.2f} euro"
    return string
print(Gemiddelde())

def Meervoudig():
    invoer_lijst = (10, 5, 3, 2, 1, 2, 9)
    uitvoer = Laag_en_Hoog(invoer_lijst)
    return uitvoer
print(Meervoudig())

def Combinatie(invoer_lijst2):
    Korte_Lijst = Laag_en_Hoog(invoer_lijst2)
    uitvoer = mijn_functie_2(Korte_Lijst[0],Korte_lijst[1])
    return uitvoer
print(Combinatie(invoer_lijst2))

