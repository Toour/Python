# Set veri tipi
fruits = {'orange','apple','banana'} # Set aynı listeler gibi sıralanır.
# print(fruits[0]) # set veri tipleri indexlenemez ve sıralanamaz

fruits.add('cherry')                # set içerisine tekli eleman gönderme.
fruits.update(['mango','grape'])    # set içerisine çoklu eleman gönderme.
print(fruits)

fruits.remove('mango')      # Set'ten mangoyu siler. Eğer mango yoksa hata verir.
fruits.discard('apple')     # Set'ten apple'ı siler. Eğer apple yoksa sorun olmaz.
print(fruits)
fruits.pop()                # Set'ten rastgele bir değeri siler. (Sıralama olmadığı için her zaman son elemanı silmez.)
print(fruits)

myList = [1,2,3,3,4,5,5,4,5,2,1,2,3,4,2,3]
print(myList)       # Listenin yazdırılması
print(set(myList))  # Listenin Set'e dönüştürülmesi (Tekrarlayan değerler 1 adet yazılır)


