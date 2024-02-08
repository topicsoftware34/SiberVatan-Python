meyveler = ["Elma","kivi","limon","böğürtlen"]

print(meyveler[2])
print(meyveler)


sayilar = [10,20,30,40,50]

sayilar[0]+=sayilar[1]
sayilar[0]+=sayilar[2]
sayilar[0]+=sayilar[3]

print(sayilar[0])


sayilar = [10,20,30,40,50]

toplam = 0

for sayi in sayilar:
    toplam +=sayi

print(toplam)

meyveler = ["Elma","kivi","limon","böğürtlen"]

for meyve in meyveler:
    print(meyve)

sayilar = [2,3,6,7,8,89,43,76,34,23]

for sayi in sayilar:
    if sayi %2 == 0:
        continue
    else:
        print(sayi)

sayi = int(input("bir sayı giriniz :"))

sayac = 0
while sayac<=sayi:
    print(sayac)
    sayac+=1


bos_liste = []
x = 0 
while x < 5:
    sayi = int(input("sayı giriniz :"))
    bos_liste.append(sayi)
    x += 1 
print(bos_liste)
