x = str(2)
y = int(5)
z = float(8)

"""
Değişken oluşturma kuralları:
1- ingilizce karakter
2- harf ile veya _ başlamalı, sayı ile başalyamaz
3- özel karakterlerden sadece_ kullanılabilir
4- pythondaki özel fonksiyon isimleri değişken adına verilemez


sayi1=10
sayi2=20
sayi3=30

toplam= sayi1+sayi2+sayi3
çarp= sayi1*sayi2*sayi3
ortalama=(sayi1+sayi2+sayi3)/3
print(toplam)
print(çarp)
print(ortalama)
-----------------

isim = input(" enter your name: ")
print(f"hello {isim}")

number1= int(input("enter a number:"))
number2 = int(input("enter a number:"))
number3 = int(input("enter a number:"))
print(number1 +number2+number3)


vize1 = int(input("vize 1 notu: "))
vize2 = int(input("vize 2 notu: "))
final = int(input("final notu: "))
total = vize1*0.30+vize2*0.30+final*0.40
print(f"vize 1: {vize1}, vize 2:{vize2}, final: {final}, total :{total}")

personel_isimleri = ["Büşra","Beyza","Zeynep"]
personel_yaslari=[10,11,12]
print(personel_isimleri[0:3])

personel_isimleri.append("Kadir")
len(personel_isimleri)
karisik= [10,"Yusuf",15]
sozluk1 = {
    "marka":"audi",
    "model" : "a5",
    "year" : 2000
}
sozluk2 = {
    "001":["beyza","risk","10",50000],
    "002": ["büşra", "ik","20",100000 ]

}


print(sozluk2["001"])

satiş = {
    "elma": [2,1.5,1],
    "armut": [3,2.5,2],
    "çilek": [4,3,2.5],
}

print((satiş["elma"][0])*8+(satiş["armut"][1])*20+(satiş["çilek"][2])*55)

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

yas = int(input("yaş giriniz:"))
if yas<18:
  print("çocuk")
elif yas >= 18 and yas <=25:
  print("genç")
elif yas>25 and yas<=40:
  print("orta yaş")
else:
  print("yaşlı")

---------------------

vize1 = int(input("vize 1 notu: "))
vize2 = int(input("vize 2 notu: "))
final = int(input("final notu: "))

ortalama = vize1*0.30+vize2*0.30+final*0.40

if (ortalama<=100 and ortalama>=0):
    if ortalama<=100 and ortalama>=90:
        harfNotu = "AA"
    if ortalama<90 and ortalama>=80:
        harfNotu = "BA"
    if ortalama<80 and ortalama>=70:
        harfNotu = "BB"
    if ortalama<70 and ortalama>=60:
        harfNotu = "CB"
    if ortalama<60 and ortalama>=50:
        harfNotu = "CC"
    if ortalama<50 and ortalama>=40:
        harfNotu = "DC"
    if ortalama<40:
        harfNotu = "Kaldı"
else:
    print("geçersiz not")

print(f"ortalamanız {ortalama} ve harf notunuz {harfNotu}")



cinsiyet = input("lütfen cinsiyeti giriniz").lower()

-------------------------

sayi1 = int(input("enter a number:"))
sayi2 = int(input("enter a number:"))
sayi3 = int(input("enter a number:"))

max = 0

if sayi1 >= max:
  max = sayi1
if sayi2 >=max:
  max = sayi2
if sayi3 >=max:
  max = sayi3

print(f"en büyük sayi {max}")  

total = 0

price = {
    "elma": [5,4,3.5],
    "armut": [6,5,4.5],
    "cilek": [8,7,6.5],
}

kg_elma = int(input("kaç kilo elma istersiniz:"))
kg_armut = int(input("kaç kilo armut istersiniz:"))
kg_cilek = int(input("kaç kilo çilek istersiniz:"))

if kg_elma>0 and kg_elma<=10:
    total +=kg_elma*price["elma"][0]
if kg_elma>10 and kg_elma<=50:
    total +=kg_elma*price["elma"][1]
if kg_elma>50:
    total +=kg_elma*price["elma"][2]

if kg_armut>0 and kg_armut<=10:
    total +=kg_armut*price["armut"][0]
if kg_armut>10 and kg_armut<=50:
    total +=kg_armut*price["armut"][1]
if kg_armut>50:
    total +=kg_armut*price["armut"][2]

if kg_cilek>0 and kg_cilek<=10:
    total +=kg_cilek*price["cilek"][0]
if kg_cilek>10 and kg_cilek<=50:
    total +=kg_cilek*price["cilek"][1]
if kg_cilek>50:
    total +=kg_cilek*price["cilek"][2]

print(f"toplam tutar {total} tl")

-------------------


choose = input("tek mi çift mi:")
sayi=0
checker = True
if choose =="tek":
    sayi=1
  
while checker:
    if choose == "tek":
        print(sayi)
        sayi +=2
    if choose == "cift":
        print(sayi)
        sayi +=2
    if sayi ==100:
        checker = False



------------

start = 0
checker = True

while checker:
  num1 = int(input("sayi 1 giriniz:"))
  num2 = int(input("sayi 2 giriniz:"))
  if num1 < num2:
      start = num1
      while start<=num2:
          print(start)
          start +=1
          checker=False
  if num2 < num1:
      start = num2
      while start<=num1:
          print(start)
          start +=1
          checker= False
  if num2 == num1:
      print("sayılar eşit")



num1 = int(input("faktöriyelini almak istediğiniz sayi giriniz:"))

start = 1
result = 1
if num1 >=0:
    while start<=num1:
        result *= start
        start+=1
    print(f"girdiğniz {num1}'nın faktöriyel sonucu: {result}")    
else:
  print("negatif sayı girdiniz")    

  
---------------------

sayi = int(input("Bir sayı girin: "))
 
if sayi <= 1:
    print(f"{sayi} asal bir sayı değildir.")
else:
    i = 2
    asal = True
    while i < sayi:
        if sayi % i == 0:
            asal = False
            break
        i += 1

    if asal:
        print(f"{sayi} asal bir sayıdır.")
    else:
        print(f"{sayi} asal bir sayı değildir.")

  

--------------------        

for i in range(1,10):
    print(i)
  
--------------------


personel_list = ["beyza","zeynep","nurhayat","irem"]

for i in personel_list:
    print(f"merhaba {i} hanım")


sayi1 = int(input("bir sayi giriniz:"))
sayi2 = int(input("bir sayi giriniz:"))

sayi_min = min(sayi1,sayi2)
sayi_max = max(sayi1,sayi2)

total =0
for i in range(sayi_min+1,sayi_max):
    total+=i

print(total)



sayi = int(input("Bir sayı girin: "))


if sayi <= 1:
    print(f"{sayi} asal bir sayı değildir.")
else:
    i = 2
    asal = True
    for  i in range (i,sayi):
        if sayi % i == 0:
            asal = False
            break
        i += 1

    if asal:
        print(f"{sayi} asal bir sayıdır.")
    else:
        print(f"{sayi} asal bir sayı değildir.")

# Break the loop when x is 3, and see what happens with the else block:
        
        
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")



-----------------

priceStock = {
    "süt": {"fiyat":20, "stok":50},
    "ekmek": {"fiyat":10, "stok":50},
    "kahve": {"fiyat":110, "stok":50},
    "peynir": {"fiyat":90, "stok":50},
    "zeytin": {"fiyat":70, "stok":50},

}
finalPrice = 0
cargo = 50

orders = [
    {
    "musteri": "Ayşe Yılmaz",
    "sepet": [("süt",4),("ekmek",2),("kahve",1)]
}, {
    "musteri": "Mehmet Arslan",
    "sepet": [("peynir",3),("zeytin",2)]
}, {
    "musteri": "Ece Demir",
    "sepet": [("süt",10),("asekmek",5),("peynir",1),("zeytin",1)]
}
]

for i in orders:
    for j in i["sepet"]:
        if j[0]=="süt":
            finalPrice += j[1]*20
            priceStock["süt"]["stok"]-=j[1]
        if j[0]=="ekmek":
            finalPrice += j[1]*10
            priceStock["ekmek"]["stok"]-=j[1]
        if j[0]=="kahve":
            finalPrice += j[1]*110
            priceStock["kahve"]["stok"]-=j[1]
        if j[0]=="peynir":
            finalPrice += j[1]*90
            priceStock["peynir"]["stok"]-=j[1]
        if j[0]=="zeytin":
            finalPrice += j[1]*70
            priceStock["zeytin"]["stok"]-=j[1]
    print(f"{i["musteri"]} müşterinin ara toplamı {finalPrice} TL, kargo {cargo} TL, toplam {finalPrice+cargo} TL")
    finalPrice=0


for k,l in priceStock.items():
    print(f"ürün {k} : stok {l["stok"]}")

-----------------------
    



def toplama():
    sayi1 = int(input("bir sayi giriniz:"))
    sayi2 = int(input("bir sayi giriniz:"))
    print(sayi1+sayi2)

toplama()

--------------





def calculate_age(birth):
    print(2025 - birth)


birth =int(input("doğum yılınızı giriniz:"))
calculate_age(birth)

----------------------



def toplama(sayi1,sayi2):
    toplam = sayi1 +sayi2
    print(f"{sayi1} + {sayi2} = {toplam}")


x = 5
y = 6

toplama(x,y)
----------------

# girilien iki sayının arasindaki sayıların ortalaması : örn (5,10) girildi ortalama = 6+7+8+9/4 = 7.5

def ortalama(sayi1,sayi2):
    min1 =  min(sayi1,sayi2)
    max1 = max(sayi1,sayi2)
    c = 0
    toplam = 0
    for i in range(min1+1,max1):
        toplam +=i
        c+=1
    result = toplam/c
    print(result)

ortalama(1,5)
---------------------------


# girilen iki sayı arasindaki asal sayıları ekrana bastır

def aradakiAsal(sayi1,sayi2):

    min1 = min(sayi1,sayi2)
    max1 = max(sayi1,sayi2)
    asalSayilar = []

    for k in range(min1,max1):
        sayi =k
        if sayi <= 1:
            asal = False
        else:
            i = 2
            asal = True
            while i < sayi:
                if sayi % i == 0:
                    asal = False
                    break
                i += 1

            if asal:
                 asalSayilar.append(sayi)

    return asalSayilar

sayi1 = int(input("Bir sayı girin: "))
sayi2 = int(input("Bir sayı girin: "))
print(aradakiAsal(sayi1,sayi2))


"""

