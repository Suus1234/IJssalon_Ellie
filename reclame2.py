#ik heb wat gestudeerd en maak nu huiswerk van Les 08 nog een keer. Kijken of het nu beter gaat. Bestand algemen functies heb ik niet aangepast.
from statistics import mean
from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting:.2f} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(btw, *inkomsten):
    totaal = 0
    for i in inkomsten:
        totaal += i
    btw_bedrag = btw * totaal
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro betaald dient te worden."
    return uitvoer
print(inkomsten_totaal(0.09, 220, 430, 125, 160, 205, 90, 345))

# test_voor_mij aangemaakt of ik het begrijp. Wat ik wilde, lukte!
#test_voor_mij = 156, 235, 51, 69, 504, 305, 624, 24, 58
mijn_lijst = 220, 430, 125, 160, 205, 90, 345
def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)
print(laag_en_hoog(mijn_lijst))
#print(laag_en_hoog(test_voor_mij))

def gemiddelde(mijn_lijst):
    bedrag = mean(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro"
    return uitvoer
print(gemiddelde(mijn_lijst))

invoer_lijst = 10, 5, 3, 2, 1, 2, 9
def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer
print(meervoudig(invoer_lijst))

invoer_lijst2 = 1, 2, 6, 80, 40, 60
def combinatie(invoer_lijst2):
    korte_lijst = meervoudig(invoer_lijst2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(invoer_lijst2))







    