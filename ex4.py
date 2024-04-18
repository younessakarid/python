noms = []
notes = []

#saisi les donner

nb = int(input("taper le nombre de stagéres"))
for i in range(nb):
    nom = input("donner votre nom")
    noms.append(nom)
    note = float(input("donner la note de "))
    notes.append(note)

#affichage
    
print("nom   :  note")
for i in range(nb):
    print(noms[i], ":", notes[i])

#calculer la moyenne de la classe
    
    s = 0
    for i in range(nb):
        s = s+note[i]
    M=s/nb
    print("la moyenne est ",M)

    #    