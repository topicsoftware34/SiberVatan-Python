
def sayikontrol(sayi):
    basamaklar = str(sayi)
    if len(set(basamaklar)) == 1:
        return 1
    else:
        return 0
    
A =[233,45,777,82,00000]
for sayi in A:
    if sayikontrol(sayi):
        print(f"{sayi}: basamakları aynı.")
    else:
        print(f"{sayi} : basamakları farklı.")


liste = [10,20,30,40,50]
print(type(liste))

class Person:   
    address = "bilgi yok"
    def __init__(self,name,lname,address,yas):
        self.name = name 
        self.lname = lname
        self.address = address  
        self.yas = yas
    def intro(self):
        print("merhaba ben "+ self.name)
    def hesap(self):
        buyıl = 2024 
        yasım = buyıl - self.yas
        print(yasım)



p1 = Person("ali","koç","bostanbükü",1566)
print(p1)
print("benim adım",p1.name,p1.lname)
print("benim adresim",p1.address)
print(type(p1))
print("benim adım",p1.name,"soyadım",p1.lname,"adres bilgisi :",p1.address)

p2 = Person(name="Ömer Tarık",lname="Topak",address="bostanbükü",yas=2008)
print(p2)
print("adım",p2.name,"soyadım",p2.lname,"adres:",p2.address,"doğum yılım",p2.yas,"yaşım",p2.hesap())

p1.intro()
p2.intro()
p1.hesap()
p2.hesap()




class Daire:
    pi = 3.14
    yaricap = 5
    def __init__(self, yaricap,pi):
        self.yaricap = yaricap
        self.pi = pi
    def cevre_hesapla(self):
        cevre = 2 * self.pi * self.yaricap
        return cevre
    
    def alan_hesapla(self):
        alan = self.pi * (self.yaricap ** 2)
        return alan
tanımlamalar = Daire(5, 3.14)
print("Dairenin çevresi:", int(tanımlamalar.cevre_hesapla()))
print("Dairenin alanı:", int(tanımlamalar.alan_hesapla()))



class Daire:
    pi = 3.14
    yaricap = 5
    def __init__(self, yaricap,pi):
        self.yaricap = yaricap
        self.pi = pi
    def cevre_hesapla(self):
        cevre = 2 * self.pi * self.yaricap
        return cevre
    
    def alan_hesapla(self):
        alan = self.pi * (self.yaricap ** 2)
        return alan
yaricap = float(input("Dairenin yarıçapını girin: "))
tanımlamalar = Daire(yaricap, 3.14)
print("Dairenin çevresi:", int(tanımlamalar.cevre_hesapla()))
print("Dairenin alanı:", int(tanımlamalar.alan_hesapla()))
        
class Square:
    def __init__(self, kenar):
        self.kenar = kenar
    def alan_hesapla(self):
        alan = self.kenar ** 2
        return alan
    
kare = Square(4)
print("Karenin alanı:", kare.alan_hesapla())

