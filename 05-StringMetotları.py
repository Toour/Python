# String ifadeler için tanımlanmış bazı fonksiyonlar ve kullanımları.

message = "Hello there. Just stop pretending like you are a nice person."

# Tüm harfleri büyütme
# message = message.upper()

# Tüm harfleri küçültme
# message = message.lower()

# Her kelimenin baş harfini büyütme
# message = message.title()

# Sadece ilk harf büyütülür
# message = message.capitalize()

message2 = "  Hello there. Just stop pretending like you are a nice person.  "
# İfadenin baş ve son kısmındaki boşlukları kaldırma
# message2 = message2.strip()

# İfade içerisindeki kelimeleri boşluklardan ayırma
# message = message.split()

# İfadeyi farklı bir sembole-karaktere göre ayırma
# message = message.split('.')

# Bölünmüş ifadeyi birleştirme
# message = ' '.join(message)

# İfade içerisinde belirli bir pattern'i arama
# index = message.find('like')
# print(index)

# İfadenin belirtilen karakter ile başladığını bulma
# isFound = message.startswith("H")
# print(isFound)

# İfadenin belirtilen karakter ile bittiğini bulma
# isFound = message.endswith(".")
# print(isFound)

# İfadenin içerisindeki belirli karakter-kelime'yi değiştirme
# message = message.replace("nice","bad")

# İfadeyi belirtilen büyüklükteki alanın ortasına yerleştirme
# message = message.center(100) # Mesajı 100 adet boşluğun ortasına koyar.
# message = message.center(100,"#") # Mesahı 100 adet '#' ifadesinin ortasına koyar.

print(message)
# print(message2)