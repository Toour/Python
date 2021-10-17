_musteriAdi = "Turan"
_musteriSoyadi = "Kılıç"
_musteriAdSoyad = _musteriAdi + " " + _musteriSoyadi
_musteriCinsiyeti = "E"
_musteriTC = "35345345340"
_musteriDogumYili = 1999
_musteriAdres = "Ankara"
_musteriYasi = 2021 - _musteriDogumYili

print("Müşteri Adı: " + _musteriAdSoyad)
print("Müşteri Cinsiyeti: " + _musteriCinsiyeti)
print("Müşteri TC: " + _musteriTC)
print("Müşteri Yaş: " + str(_musteriYasi))

_order1 = 110
_order2 = 1100.5
_order3 = 356.95

print("Sipariş Tutarı: " + str(_order1 + _order2 + _order3) + " TL")


