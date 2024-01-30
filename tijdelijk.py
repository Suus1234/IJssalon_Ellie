#huiswerk Les 07
#importeren functie vanuit ander bestand; les 08
from helper import decoreer

def print_aanbieding():
    Prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }
    Aanbieding = (Prijzen["aardbei"] * 0.8)
    Reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {Aanbieding}")
    
    Reclame_tekst2 = (Reclame_tekst[:63])
    
    Reclame_tekst3 = (Reclame_tekst2.upper())

    Reclame_tekst4 = ("VANDAAG", "IN", "DE", "AANBIEDING",":", "AARDBEI-IJS",", ", "1", "LITER", "-", "SLECHTS", "€", "2.40",".")
    for El in Reclame_tekst4:
        if len(El) < 5:
            print(El.lower())
        else:
            print(El.upper())

decoreer("Aanbieding")
print_aanbieding()
