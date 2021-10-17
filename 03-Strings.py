# Stringler aynı zamanda birer karakter dizileridir.
name = "Turan"
surname = "Kılıç"
age = 21

greeting = "I\'m " + name + " " + surname + ".\nMy age is " + str(age) + " :)"

print(greeting)        # ==> Tamamını yazdırma.
print()
print(greeting[0])     # ==> İlk harfi yazdırma. 
print()
print(greeting[-1])    # ==> Son harfi yazdırma. (Diğer Opsiyon: print(greeting[length - 1]))
print()
print(len(greeting))   # ==> Uzunluğunu yazdırma.
print()
print(greeting[4:9])   # ==> 4. karakterden (dahil değil) 9. karaktere (dahil) yazdırma.
print()
print(greeting[4:])    # ==> 4. karakterden itibaren geri kalanı yazdırma.
print()
print(greeting[:16])   # ==> Başından 16. karaktere kadar yazdırma.
print()
print(greeting[2:len(greeting):3]) # ==> 2. karakterden sonuna kadar 3-3-3. sıradaki karakterleri yazdırma.


