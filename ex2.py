ncopie = int (input("Tapper le nombre dee copie a faire : "))

if ncopie<  10 :
     print (" le  montant a payer est : ", ncopie * 0,50 , "dh")
elif ncopie < 20:
  print (" le  montant a payer est : ", ncopie * 0,40 , "dh")
elif ncopie <50 :
      print (" le  montant a payer est : ", ncopie * 0,30 , "dh")
else :
     print (" le  montant a payer est : ", ncopie * 0,20 , "dh")
