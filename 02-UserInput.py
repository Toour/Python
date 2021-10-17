# Kullanıcıdan Input Alma 
r = int(input("Dairenin Yarıçapını Giriniz: "))
pi = 3.14
daireAlan = pi * (r**2)
daireCevre = 2 * pi * r


print("## Girilen Yarıçapa Sahip ##")
print("Dairenin Alanı: " + str(daireAlan))
print("Dairenin Çevresi: " + str(daireCevre))
