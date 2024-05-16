
notes = []

nombre_notes = int(input("donner le nombre des notes : "))


for i in range (nombre_notes) :
    note = float(input(f"Saisissez la note {i + 1} : "))
    notes.append(note)

print(" voicer la list : ",notes)

print("---------------------------")

notes.reverse()
print(notes)

#la somme des notes :
sum(notes)
print("la somme de les note  est : ",sum(notes))
print("---------------------------")

#la moyenne des notes :

moyenne = sum(notes) / len(notes)
print("la moyenne des notes est : ",moyenne)

print("---------------------------")

# le maximum :

max(notes)
print("le maximum est : ",max(notes))
print("---------------------------")

#e minimum :

min(notes)
print("le minimum est : ",min(notes))

#coupler les accurence d'une valeur :

for note in notes :
    occuence = notes.count(note)
    print(f"occurences de la note {note} : ",occuence)
   
 



