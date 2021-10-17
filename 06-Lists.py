# Listeler
# message = "Hello there. My name is Turan Kılıç".split()
# print(message[0])

my_list = [1,2,3]
my_list2 = ['bir',2,True,5.6] # Listeler farklı veri tiplerini barındırır.
print(my_list)
print(my_list2)

list1 = ["bir","iki","üç"]
list2 = ["dört","beş","altı"]

numbers = list1 + list2 # Birkaç liste birleştirilebilir.
print(numbers)
print(len(numbers))

numbers2 = [list1, list2] # Birkaç liste iç içe liste oluşturmada kullanılabilir.
print(numbers2)
print(numbers2[0]) # İç içe listedeki ilk listeyi döndürür.
print(numbers2[0][2]) # İç içe listedeki ilk listenin 2. indexini döndürür.

