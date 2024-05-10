#declaration de dictionnaire

D = {}

# remplissage de  dictinonaire

D["nom"]= input("saiser ton nom :")
D["age"]= int(input("saiser  ton age:"))



#afichage de dictionnaire

print(D)
print("----------------------------")

#afichage par clé

for i in D.items() :
    print(i)

print("----------------------------")    

#afichage  en illustrant la clé est la valeur    

for cle,valeur in D.items() :
    print("la cle est ",cle, "est la valeur est : ",valeur)

print("-----------------------------")    

#afichage  en ullustrant la clé  

for cle in D :
    print("la cle est : ",cle)

print("-----------------------------")  

#afichage  en ullustrant la valeur

for valeur in D.values() :
    print("la valeur est : ",valeur)
