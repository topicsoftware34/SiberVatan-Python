open("yenidosya.txt","w")

# "w" write = yazma modu , yoksa oluşturur , içeriyi silip ekleme yapar
# "a" append = ekleme modu
# "x" create = oluşturma modu , ayınısı varsa hata verir
# "r" read = okuma modu

file = open("yenidosya.txt","w")
print(file)
file.close()
file_dizin = open("E:\Ött Software Datas\ders9folder/dosyaaçma.txt","w")
file_dizin.close()
file = open("yenidosya.txt","w",encoding="utf-8")
file.write("Ömer Tarık")
file.close()

file = open("yenidosya.txt","a",encoding="utf-8")
file.write("\nYusuf Alperen")
file.close()

file = open("yenidosya2.txt","a")

try:
    file = open("yenidosya.txt", "w")
    file.close()

    file_dizin = open(r"E:\Ött Software Datas\ders9folder\dosyaaçma.txt", "w")
    file_dizin.close()

    file = open("yenidosya.txt", "w", encoding="utf-8")
    file.write("Ömer Tarık")
    file.close()

    file = open("yenidosya.txt", "a", encoding="utf-8")
    file.write("\nYusuf Alperen")
    file.close()

    file = open("yenidosya2.txt", "a")
    file.close()

except FileNotFoundError:
     print("Dosya bulunamadı.")

finally:
     print("işlem tamam")

try:
    file = open("yenidosya.txt","r",encoding="utf-8")
    print(file)
except FileNotFoundError:
    print("dosya bulunamadı")
finally:
      print("dosya kapanıyo")
      file.close()

file = open("yenidosya.txt","r",encoding="utf-8")
for a in file:
     print(a,end="")

içerik = file.read()
print(içerik)

file = open("yenidosya.txt","r",encoding="utf-8")

icerik_karakter = file.read(0)
icerik_karakter = file.read(20)
print(icerik_karakter)
print("##########")

print(file.readline(),end="")
print(file.readline(),end="")

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
file.close()

with open("yenidosya.txt","w",encoding="utf-8") as file:
    file.write("Ömer Tarık\n")
    file.write("Yusuf Alperen")

with open("yenidosya.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(10)
    print(file.tell())


with open("yenidosya.txt","r+",encoding="utf-8") as file:
    file.seek(27)
    file.write("\nsiber vatan")


with open("yenidosya.txt","r+",encoding="utf-8") as file:
    file.seek(27)
    file.write("\nTurabi\n")
    file.close()


famouslist = ['Murathan', 'Mustafa', 'Fatih']
index = 1
with open("yenidosya.txt", "a", encoding="utf-8") as file:
    for person in famouslist:
        if index==len(famouslist):
            file.write(person)
        else:
            file.write(person+"\n")
        index+=1


import math as islem

sonuc = islem.sqrt(5)
print(sonuc)

sonuc = islem.factorial(5)
print(sonuc)

from math import * 

print(factorial(5))
print(ceil(5))
print(sqrt(5))

import random

sonuc = random.random()
print(sonuc)

import random


list =""
sayilar = [0,1,2,3,4,5,6,7,8]
i = 0
while i!=6:
    list+=str(random.choice(sayilar))
    i+=1

print(list)

import mylibary

sayi = mylibary.sayilar[2]
print(sayi)

