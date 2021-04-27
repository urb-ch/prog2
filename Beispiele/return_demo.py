def addieren(zahl_1, zahl_2, zahl_3):
    summe = zahl_1 + zahl_2
    summe_2 = summe + zahl_3
    return summe, summe_2


erste_zahl = 1
zweite_zahl = 2
dritte_zahl = 3

ergebnis = addieren(erste_zahl, zweite_zahl, dritte_zahl)
print(ergebnis)

def gruppen_preis(gruppen_groesse):
    if gruppen_groesse > 100:
        return "Gruppe zu gross"
    if gruppen_groesse > 50:
        preis = 100
    else:
        preis = 200
    return preis

gruppe = 101

ergebnis_2 = gruppen_preis(gruppe)
print(ergebnis_2)