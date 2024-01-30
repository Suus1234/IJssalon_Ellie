# huiswerk van af Les 08.4
def Aanbieding_1(Smaak, Prijs, Korting):
    Korting = Prijs - (Prijs * Korting) 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {Smaak}, van {Prijs} euro voor {Korting:.2f} euro."
    return uitvoer
print(Aanbieding_1("aardbei", 4, 0.1))
#verder met 6. LET op er zijn opmerkingen over 10, 11 en 12!!!


