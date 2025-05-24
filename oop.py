"""
class calisan():
    kabiliyetler = []
    unvan = ""
    print(f"{unvan} isimli çalışanın kabiliyetleri {kabiliyetler}")


print(calisan.kabiliyetler)
print(calisan.unvan)


class personel():
    adi = ""
    soyadi = ""
    id = ""
    maas = ""
    kabiliyetler = ""
    unvan = ""


personel1 = personel()
personel1.adi = "yusuf"
personel1.soyadi = "kaya"
personel1.id = "0001"
personel1.maas = 100000
personel1.kabiliyetler.append("ai modelleri")
personel1.unvan = "ai enginnerleri"

personel2 = personel()
personel2.adi = "sercan"
personel2.soyadi = "aydın"
personel2.id = "0002"
personel2.maas = 100000
personel2.kabiliyetler.append("ai siber güvenliği")
personel2.unvan = "ai cyber security"

print(personel1.kabiliyetler)




--------------------



class calisan():
    personel_listesi = [] #class özelliği

    def __init__(self):
        self.adi = "" #nesne özellği
        self.soyadi = ""
        self.id = ""
        self.maas = None
        self.kabiliyetler = []
        self.unvan = ""


calisan1 = calisan()
calisan1.adi = "yusuf"
calisan1.soyadi = "kaya"
calisan1.id = "0001"
calisan1.maas = 100000
calisan1.kabiliyetler.append("ai modelleri")
calisan1.unvan = "ai enginnerleri"

calisan2 = calisan()
calisan2.adi = "sercan"
calisan2.soyadi = "aydın"
calisan2.id = "0002"
calisan2.maas = 100000
calisan2.kabiliyetler.append("ai siber güvenliği")
calisan2.unvan = "ai cyber security"

calisan.personel_listesi.append(calisan1.adi)
calisan.personel_listesi.append(calisan2.adi)

print(calisan.personel_listesi)

-------------------


class urun():
    urun_listesi = []

    def __init__(self):
        self.adi = ""
        self.fiyati = None
        self.kategori = ""
        self.barcode = ""

urun1 = urun()
urun1.adi = "kaysı"
urun1.fiyati = 50
urun1.kategori = "meyve"
urun1.barcode = "0011"


urun2 = urun()
urun2.adi = "erik"
urun2.fiyati = 60
urun2.kategori = "meyve"
urun2.barcode = "0012"

urun3 = urun()
urun3.adi = "domates"
urun3.fiyati = 40
urun3.kategori = "sebze"
urun3.barcode = "0021"

urun.urun_listesi.append(urun1.adi)
urun.urun_listesi.append(urun2.adi)
urun.urun_listesi.append(urun3.adi)

print(urun.urun_listesi)

-----------
"""


class proje():
    proje_listesi = []

    def __init__(self):
        self.adi = ""
        self.deadline = ""
        self.sorumlusu = ""
        self.projeEkibi = []
        self.bütce = None

proje1 = proje()
proje1.adi = "yapay zeka"
proje1.deadline = "25.05.2025"
proje1.sorumlusu = "ali veli"
proje1.projeEkibi.append("hasan veli")
proje1.bütce = 1000


proje2 = proje()
proje2.adi = "siber güvenlik"
proje2.deadline = "25.06.2025"
proje2.sorumlusu = "hasan hüseyin"
proje2.projeEkibi.append("samet")
proje2.bütce = 1500


proje3 = proje()
proje3.adi = "devops"
proje3.deadline = "25.05.2025"
proje3.sorumlusu = "esra ece"
proje3.projeEkibi.append("aslı")
proje3.bütce = 2000


proje.proje_listesi.append(proje1.adi)
proje.proje_listesi.append(proje2.adi)
proje.proje_listesi.append(proje3.adi)

print(proje.proje_listesi)




