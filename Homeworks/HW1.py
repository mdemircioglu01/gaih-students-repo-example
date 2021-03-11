#Ödevde 30'a kadar olan sayılar tek ve çift sayılar olmak üzere iki listeye kaydedilmişlerdir.
#Daha sonra bu iki liste birleştirilerek, elemanlarının hepsi iki ile çarpılmıştır.
#Birleştirilen ve elemanları iki ile çarpılan listenin değerleri ve veri tipleri tek tek yazdırılmıştır.

#1. Ödev
cift = [x for x in range(30) if x % 2 == 0]
tek = [x for x in range(30) if x % 2 == 1]
liste =cift+tek
cliste = [x*2 for x in liste]
i=0
while (i < len(cliste)):
  print(i, ". eleman: ///", "değeri:", cliste[i], "/// sınıfı:", type(cliste[i]))
  i+=1
