#huiswerk Les 07
Prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
Aanbieding = (Prijzen["vanille"] * 0.8)
Reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {Aanbieding}")
print (Reclame_tekst)
# print(f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {Aanbieding}") - vind ik fijner dan eerst via reclame_tekst. Maar opgave lijkt te zeggen dat het via die extra regel moet
# Ik heb als uitkomst 3.2 zonder alle nullen. Dus ik index maar op de 2 om de volgende vraag te voldoen en behoud de eerste print opdracht ook. 
Reclame_tekst2 = (Reclame_tekst[:61])
Reclame_tekst3 = (Reclame_tekst2.upper())
Reclame_tekst4 = ("VANDAAG", "IN", "DE", "AANBIEDING",":", "VANILLE-IJS",", ", "1", "LITER", "-", "SLECHTS", "€", "3",".")
El = (Reclame_tekst4)
for i in El:
    if len(i) < 5:
        print(i.lower())
    else:
        print(i.upper())