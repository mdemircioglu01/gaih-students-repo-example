#Explain your work

#Question 1
cift = [x for x in range(30) if x % 2 == 0]
tek = [x for x in range(30) if x % 2 == 1]
liste =cift+tek
cliste = [x*2 for x in liste]
i=0
while (i < len(cliste)):
  print(i, ". eleman: ///", "değeri:", cliste[i], "/// sınıfı:", type(cliste[i]))
  i+=1
