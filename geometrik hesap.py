
kirmizi = "\u001b[31;1m"
yesil = "\u001b[32m"
sari = "\u001b[33;1m"
mavi ="\u001b[34;1m"				
                
while True:

    print(yesil + """
        
        1.ucgen hesabi
        2.dortgen hesabi
        
        Çıkış yapmak için '0' giriniz
        """)


    secim = int(input(kirmizi + "lutfen isleminizi seciniz: "))
        
    
    if secim == 1:
        k1 = int(float(input(mavi + "lutfen birinci kenari giriniz:")))
        k2= int(float(input(mavi + "lutfen ikinci kenari giriniz:")))
        k3= int(float(input(mavi + "lutfen ucuncu kenari giriniz:")))

        if abs(k2+k1)>k3 and  abs(k2+k3)>k1 and abs(k3+k1)>k2:
                
            if(k2==k1 and k2==k3):
                print(kirmizi + "eskenar ucgen belirtir")
            
                
            elif(k2==k1 and k2!=k3 ) :

                print(kirmizi + "ikizkenar ucgen belirtir")

            else:
                print(kirmizi +  "cesitkenar ucgen belirtir")
        else:
            print(kirmizi + "girilen degerler ucgen belirtmez")
        

    elif secim == 2:

        kenar1 = int(float(input(kirmizi + "birinci kenari girin:")))

        kenar2 = int(float(input(kirmizi + "ikinci kenari girin:")))

        kenar3 = int(float(input(kirmizi + "ucuncu kenari girin:")))

        kenar4 = int(float(input(kirmizi + "dorduncu kenari girin:")))

        if  (kenar1==kenar2 and kenar2==kenar3) :
            
            print(mavi + "kare belirtir")

        elif(kenar1==kenar2 and kenar3==kenar4 or kenar2 == kenar3 and kenar1==kenar4  ):

            print(mavi + "dikdortgen belirtir")

        else:
            print(mavi + "herhangi bir dortgen olabilir")
    
    elif secim == 0:
        print('ÇIKIŞ YAPILIYOR')
        break
