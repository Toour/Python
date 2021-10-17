# Yazdırma (Print) Formatı Ayarlama
name = "Turan"
print("My name is {}" .format(name)) # Format fonksiyonu ile tek değişken atanması.

surname = "Kılıç"
print("My name is {} {}" .format(name, surname)) # Format ile iki değişken atama.

# print("My name is {0} {1}" .format(name, surname)) # Default değişken sıralaması
print("My name is {1} {0}" .format(name, surname)) # Farklı sırada değişken sıralaması

# print("My name is {n} {s}" .format(n=name, s=surname)) # Default değişken isimlendirme sıralaması
print("My name is {s} {n}" .format(n=name, s=surname)) # Farklı sırada isimlendirilmiş değişken sıralaması

sonuc = 200/600
print("Sonuç: {s:1.2}" .format(s=sonuc)) # Sonucun "." dan sonra 2 basamağının yazdırılması.

print(f"My name is {name} {surname} .") # "f" ile formatta değişkenlerin kendi isimlerinin kullanılması.
