list
liste =[1,2,3,4,5]
print(liste)
print(liste[4])
print(type(liste))

liste[4] = 35
print(liste)

alt_liste = liste[2:4]
print(alt_liste)

tuple
tuple = (1,2,3,4,5,6)
print(type(tuple))
print(tuple)
print(tuple[1])
#tuple[1] = 7
print(tuple)
#tuple sıralı ama değiştirilemez

alt_tupple = tuple[1:4]
print(alt_tupple)

#kumeler
kume = {100,200,300,400,500}
print(kume)
kume.add(890)
print(kume)
print(type(kume))

kume.update([400,900])
print(kume)

#dict.

dict = {'anahtar1' : 'deger1' , 'anahtar2' : 'deger'}
print(dict)
print(type(dict))

deger = dict['anahtar1']
print(deger)

liste1 = set(liste)
print(liste1)

dict = {'key1' : 'value' , 'key2' : 'value2'}
list2 = list(dict.keys())
list3 = list(dict.values())
print(type(list2))
print(list2)

sayilar = [10,8,6,4,15]
en_buyuk = max(sayilar)
print(en_buyuk)
en_kucuk = min(sayilar)
print(en_kucuk)
sayilar.append(20)
sayilar.append(1)
yeni_en_buyuk = max(sayilar)
yeni_en_kucuk = min(sayilar)
print(yeni_en_buyuk)
print(yeni_en_kucuk)
print(sayilar)
sayilar.pop()
print(sayilar)
sayilar.sort()
print(sayilar)
sayilar.reverse()
print(sayilar)
print(sayilar.count(10))

aralik = range(1,10)
print(list(aralik))

import random  
rastgele_sayi = random.randint (1,100)
print("tutulan sayi",rastgele_sayi)
