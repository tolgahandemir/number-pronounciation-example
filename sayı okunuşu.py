birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def okunuş (sayi):
        birinci=sayi %10
        ikinci=sayi //10



        return onlar[ikinci] + " " + birler[birinci]
while True:
        sayi = int(input("Sayıyı giriniz "))
        if(sayi==0):
                print("program sonlandırıldı")
                break

        print(okunuş(sayi))