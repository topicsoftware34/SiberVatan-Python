
class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("person oluştu")
    def ben_kimim(self):
        print("insanım")
 

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
        print("teacher oluştu")
    def ben_kimim(self):
        print("öğretmenim")




class Student(Person):
    def __init__(self, fname, lname, number):
        self.number = number
        Person.__init__(self,fname,lname)
        print("student oluştu")
    def ben_kimim(self):
        print("öğrenciyim")
        


p1 = Person(fname="atakan",lname="kılıçcı")
print(p1.fname)

t1 = Teacher(branch="güvenlik uzmanı",fname="Serkan",lname="Toper")
print(t1.branch)

s1 = Student(fname="Sixpack Mert",lname="Mehmet",number="123")
print(s1.fname)

p1.ben_kimim()
s1.ben_kimim()
t1.ben_kimim()

class Islemler:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def sonucu_bul(self):
        pass

class Toplama(Islemler):
    def sonucu_bul(self):
        return self.sayi1 + self.sayi2 
    
toplama = Toplama(sayi1=15,sayi2=12)
print(toplama.sonucu_bul())


class Cıkarma(Islemler):
    def sonucu_bul(self):
        return self.sayi1 - self.sayi2 

cıkarma = Cıkarma(sayi1=56,sayi2=72)
print(cıkarma.sonucu_bul())

class Carpma(Islemler):
    def sonucu_bul(self):
        return self.sayi1 * self.sayi2 
    
carpma = Carpma(sayi1=12,sayi2=2)
print(carpma.sonucu_bul())

class Bolme(Islemler):
    def sonucu_bul(self):
        return self.sayi1 / self.sayi2 

bolme = Bolme(sayi1=92,sayi2=2)
print(bolme.sonucu_bul()) 

class Marka:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Motor:
    def __init__(self, motorgucu):
        self.motorgucu = motorgucu


class Araba(Marka, Motor):
    def __init__(self, marka, model, motorgucu):
        Marka.__init__(self, marka, model)
        Motor.__init__(self, motorgucu)

    def aracbilgileri(self):
        return f"Marka: {self.marka}, Model: {self.model}, Motor Gücü: {self.motorgucu}"

araba = Araba("Merso", "Maybach", 390)
print(araba.aracbilgileri())

def floyd(satır):
    sayı = 1 
    for i in range(1,1+satır):
        for y in range(1,i+1):
            print(sayı,end= " ")
            sayı += 1
        print()

floyd(int(input("kaç satır istersiniz :")))


