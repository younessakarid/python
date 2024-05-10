
D = {}

# remplissage de  dictinonaire

D["nom"]= input("saiser ton nom :")
D["age"]= int(input("saiser  ton age:"))



#afichage de dictionnaire

print(D)

#afichage par clé

for i in D.items() :
    print(i)

#afichage  en illustrant la clé est la valeur    

for cle,valeur in D.items() :
    print("la cle est ",cle, "est la valeur est : ",valeur)