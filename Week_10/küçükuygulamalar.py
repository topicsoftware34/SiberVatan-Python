def hesaplamasaatlik(toplam_calisma_saati):
    saatlik_ücret = 50
    if toplam_calisma_saati <= 40:
        maas = toplam_calisma_saati * saatlik_ücret
    else:
        normal_calisma_saati = 40 
        fazla_mesai_saati = toplam_calisma_saati - 40
        maas = normal_calisma_saati * saatlik_ücret + fazla_mesai_saati * (saatlik_ücret* 1.5)
    return maas

def hesaplamakomisyon(aylik_satis):
    sabit_maas = 500
    komisyon_oranı = 0.05
    komisyon = aylik_satis * komisyon_oranı
    maas = sabit_maas + komisyon
    return maas

while True:
    odeme_kodu = int(input("Ödeme kodu girin Saatlik(1),,Komisyon(2)"))
    if odeme_kodu == 1 :
        calisma_saati = int(input("toplam calisma saatinizi giriniz :"))
        maas = hesaplamasaatlik(calisma_saati)
        print("maaşınız",maas)
        break
    elif odeme_kodu == 2 : 
        aylik_satis = int(input("aylik satis miktarinizi giriniz :"))
        maas = hesaplamakomisyon(aylik_satis)
        print("maaşınız",maas)
        break
    else:
        print("geçersiz kod")




def sicaklik_araligi(sicakliklar):
    sicaklik_aralikları = {
        "(-20) - (0)" : 0 ,
        "(0) - (20)" : 0 ,
        "(20) - (40)" : 0 
    }

    for sicaklik in sicakliklar :
        if -20 <= sicaklik < 0:
            sicaklik_aralikları["(-20) - (0)"] +=1
        elif 0 <= sicaklik < 20:
            sicaklik_aralikları["(0) - (20)"] +=1
        elif 20 <= sicaklik < 40:
            sicaklik_aralikları["(20) - (40)"] +=1

    for aralik,sayi in sicaklik_aralikları.items():
        print(aralik,"aralığında",sayi ,"adet sıcaklık bulunmaktadır")

sicaklik_listesi = [10,23,39,-12,32,1,-12,-14]
sicaklik_araligi(sicaklik_listesi)
