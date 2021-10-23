# Value ve Reference Type 
# Value Types => string, number
x = 5
y = 25
# x ve y value type değişkenler oldukları için birbirlerine eşitlendiklerinde sadece değerleri aynı olur.
# Bir diğerinin 
x = y
y = 10

# print(x,y)

# Reference Type => list
a = ["apple","banana"]
b = ["apple","banana"]
a = b

b[0] = "lemon"
print(a,b) # Artık a ve b aynı adresi gösterdiği için ikisi de aynı liste haline gelmiş oluyor.