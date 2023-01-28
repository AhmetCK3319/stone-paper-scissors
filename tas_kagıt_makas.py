import random as r
userscore=0
bilscore=0

while True:
    #bilgisayarin çececeği değerleri liste içinde belirtiyoruz.
    secenek=["taş","kağit","makas"]
    #YANLIŞ YAPILABİLECEK SEÇİMLER LİSTE İÇERİSİNE GİRİLEREK İF YAPISINI KULLANMAYA GEREK KALMADI.
    secimler={ "Taş":0,"tas":0,"TAS":0,"TAŞ":0,"Tas":0,"taş":0,
                "kagit":1,"KAGIT":1,"KAĞIT":1,"Kagıt":1,"kağit":1,"kağıt":1,
                "Makas":2,"MAKAS":2,"makas":2   
    }
    #bilgisayarin seçim yapmasi için kodlarimizi yaziyoruz.
    bilsecim=r.choice(secenek)
    bilsecim=secimler.get(bilsecim)     
    #kullanicinin seçim yapmasini sağliyoruz
    usersecim=input("bir seçenek yapiniz(taş,kağit,makas) :")
    usersecim=secimler.get(usersecim)
    #kazanma durumları belirtiliyor
    if usersecim==bilsecim:
        print("berabere")
    elif usersecim==2 and  bilsecim==1:
        print("kazandınız")
        userscore+=1
    elif usersecim==1 and bilsecim==0:
        print("kazandınız")
        userscore+=1
    elif usersecim==0 and bilsecim==2:
        print("kazandınız")
        userscore+=1        
    else:
        print("kaybettiniz")
        bilscore+=1        
    print(secenek [bilsecim], "= bilgisayar puanı :",bilscore)
    print(secenek [usersecim],"= sizin puanınız :",userscore)
   
    if userscore==3 :
        print("TEBRİKLER OYUNU KAZANDINIZ")
        break
    elif bilscore==3 :
        print("ÜZGÜNÜM OYUNU KAYBETTİNİZ")
        break
