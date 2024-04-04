from math import *

a = float (input("Taper le nombre a : "))
b = float (input("Taper le nombre b : "))
c = float (input("Taper le nombre c : "))

if a != 0 : 
    d = b*b - 4*a*c
    if d > 0 :
        x1 = (-b-sqrt(d))/2*a
        x2 = (-b+sqrt(d))/2*a
        print(round(x1,2), round(x2,2))
    else:
        if d == 0 :
            x = -b /2*a 
            print(round(x,2)) 
        else :
            print(" pas de solution")    

elif b != 0 :
    print(round(-c/b,2))
elif c == 0 :
    print("tout nombre réel")
else : 
    print(" pas de solution")       
        