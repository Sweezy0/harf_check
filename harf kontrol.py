def kontrol(str):
    sayac=0
    for ch in str:
        if ch=="ş":
            sayac=sayac+1
            return True
            break
metin=input("Metin:")
if(kontrol(metin)==True):
    print("ş harfi metnin içinde mevcuttur.")
else:
    print("ş harfi metnin içinde mevcut değildir.")