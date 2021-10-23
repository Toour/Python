# Python'da dictionary veri türü 
'''
Dictionary yani sözlükler, key-value şeklinde çalışmaktadır.
Yani bir değere ulaşabilmek için o değerin sahip olduğu key'i bilmek gerekmektedir.
'''

plakalar = { 'kocaeli' : 41, 'istanbul' : 34}

# print(plakalar['kocaeli'])  # Key'i kocaeli olan "41" numarası değeri için yazdırma.

# plakalar['ankara'] = 6      # Sözlüğe yeni key-value ikilisi ekleme.
# plakalar['kocaeli'] = 'new value'   # Yeni value ataması.

# print(plakalar)

# Tablo şeklinde sözlük oluşturma

users = {                           # Users isimli dic. oluşturuldu.
'turan' : {                         # İlk kullanıcı olarak turan eklendi
    'age' : 22,                     
    'email' : 'hebele@gmail.com',   # Kullanıcıya ait bilgilerin girilmesi.
    'address' : 'ankara',
    'phone' : '123132'
},

'kaan' : {                           # İkinci kullanıcı olarak kaan eklendid.
    'age' : 20,                     
    'email' : 'kaan@gmail.com',     # Kullanıcıya ait bilgilerin girilmesi.
    'address' : 'ankara',
    'phone' : '123123123'
}
}

print(users['turan'])               # Dic. içerisinde tek nesnenin tüm bilgileri tek çatı altında toplanmakta.
print(users['turan']['age'])        # Dic. içerisinde bir key'in altındaki key'ler ile de gerekli değerlere ulaşılabilir.



