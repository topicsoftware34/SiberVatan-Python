def selamdünya():
    print("hello world")

selamdünya()
        
    
def hoşgeldin(name):
    print("hoşgeldin "+name)

hoşgeldin("tarık")
    
    
 
def hoş():
    print("hoşgeldin "+input("isiminizi giriniz :"))

hoş()

def hoş(name):
    print("hoşgeldin "+name)

hoş(input("isiminizi giriniz :"))


def fonksiyon(sehir = "konya"):
    print("en sevdiğim şehir "+sehir)

fonksiyon("istanbul")
fonksiyon()  

def sayi(x):
    x = x+5 
    return x     
sonuc = sayi(10)
print(sonuc)


def toplama(x,y):
    z = x + y
    return z
sonuc = toplama(10,5)
print(sonuc)


def fonk_tuple(*argv):
    for arg in argv:
        print(arg)

fonk_tuple('selam','naber','nasılsın','iyidir','bende iyiyim')


def çift_sayı(x):
    bos_liste = []
    for a in range(0, x+1, 2):
        bos_liste.append(a)
    return bos_liste

alınan_sayı = int(input("sayı giriniz :"))
bos_liste = çift_sayı(alınan_sayı)
print("çift sayılar :",bos_liste)


def çift_sayı(x):
    bos_liste = []
    for i in range(0,x+1):
        if i%2==0:
           bos_liste.append(i)
        else:
            continue
    return bos_liste

alınan_sayı = int(input("sayı girin :"))
bos_liste = çift_sayı(alınan_sayı)
print("çift sayılar :",bos_liste)

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Tanımsız"
    else:
        return x / y
    
def faktoriyel(n):
    faktoriyel = 1
    for i in range(1, n+1):
        faktoriyel *= i
    return faktoriyel

while True:
    
    print("$$$$$$$$$$----HOŞGELDİNİZ----$$$$$$$$$$")
    print("Hangi işlemi yapmak istersiniz:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("6.ÇIKIŞ")
    print("5.Faktoriyel")

    secim = input("Tercih yapınız : 1,2,3,4,5,6  ")

    if secim == '6':
        print("Çıkılıyor...")
        break

    birinci_sayı = int(input("Birinci sayıyı giriniz :"))

    ikinci_sayı = float(input("İkinci sayıyı giriniz :"))

    if secim == "1" :
        print("Sonuç",toplama(birinci_sayı,ikinci_sayı))    
    elif secim == "2" :
        print("Sonuç",cikarma(birinci_sayı,ikinci_sayı))
    elif secim == "3" :
        print("Sonuç",carpma(birinci_sayı,ikinci_sayı))
    elif secim == "4" :
        print("Sonuç",bolme(birinci_sayı,ikinci_sayı))    
    elif secim == "5":
        print("Sonuc",faktoriyel(birinci_sayı))
    else:
        print("Sayı girişi yanlış")
