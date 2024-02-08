a=90
b="Siber Vatan"

num1,num2,num3=5,55,65
print("sayilar",num1,num2,num3)

num1=num1+50
num2=num2+55
num3=num3+90

num1+=num2
num1+=90
num1/=num2


numbers=(50,55,65)
print(type(numbers))
# num1,num2,num3,num4=numbers

# print(num4) #hata verir tanımlı olmadığı için

a,b,c,d=50,100,50,7

sonuc=(a>b)
print(sonuc)

sonuc=(a==c)
print(sonuc)

sonuc=(a>d)
print(sonuc)

sonuc=(a!=d)
print(sonuc)


username1="Ömer"
username2="tarık"
print("A.R.O.G'a hoşgeldiniz\n" )
Username_input=input("İsminizi giriniz :")

sonuc=(username1.lower()==Username_input.lower())
sonuc2=(username2.lower()==Username_input.lower())

sonuc3=(sonuc != sonuc2)

print("Eşleşme sonucu ...:",sonuc3)




dict = {        "qcxx@gmail.com":"AbC123",
                "abcde@gmail.com":"qcxx741"
        }
email = input("E-posta adresinizi giriniz: ")
sifre = input("Şifrenizi giriniz: ")

sonuc_mail=(email in dict.keys())
sonuc_sifre=(sifre in dict.values())

sonuc_final=(int(sonuc_mail)+int(sonuc_sifre)==2)
print("Eşleşme durumu ....:",sonuc_final)


fruist={"elma","muz","portakal","kivi"}
#(<bir şey > <operatör> <bir şey> )
print("kiraz" in fruist)




x = y = [10,20,30]
z = [10,20,30]
print(x is y)
print(x is z)



vize= int(input("Vize puanınızı giriniz : "))
final=int(input("Final puanınızı giriniz : "))
puan=(vize*0.4)
puan2=(final*0.6)

ort=(puan+puan2)
geçti=(ort>=50)
print("geçme durumu",geçti)

sayı=int(input("bir sayı giriniz   : "))

sonuç=(sayı>0) and (sayı%2==0)

print("durum",sonuç)

x=98
y=98

if (x>y):
        print(x ,"büyüktür")
elif(x==y):
        print("sayılar eşittir")
else:    
        print(y,"büyüktür")
        
kullanıcı_adı=input("kullanıcı adı giriniz  : ")
sifre=int(input("Şifre giriniz : "))

ad="tarık"
sifresi=123
if ad==kullanıcı_adı and sifresi==sifre:
        print("kullanıcı adı ve şifre doğru")
elif ad==kullanıcı_adı and sifresi!=sifre:
        print("şifre hatalı")
elif ad!=kullanıcı_adı and sifresi==sifre:  
        print("kullanıcı adı hatalı")
else :
        print("kullanıcı adı ve şifre hatalı")


print("------------------HOŞGELDİNİZ------------------")


işlem=int(input("bir işlem seçiniz    \nToplama:1\n Çıkarma:2\nÇarpma:3\nBölme:4    :  "))
sayı1=int(input("1. sayı giriniz     : "))
sayı2=int(input("2. sayı giriniz    : "))
if işlem==1:
        sonuc=(sayı1+sayı2)
        print(sonuc)
elif işlem==2:
        sonuc=(sayı1-sayı2)
        print(sonuc)
elif işlem==3:
        sonuc=(sayı1*sayı2)
        print(sonuc)
elif işlem==4 :
        if sayı2!=0:
                sonuc=(sayı1/sayı2)
                print(sonuc)
        else:
                print("hatalı işlem")
else:
        print("1,2,3,4 rakamlarından birini seçiniz")
