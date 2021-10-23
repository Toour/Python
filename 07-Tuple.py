# Tuple kavramı ve liste ile arasındaki fark
list = [1,2,3]          # Listeler köşeli parantez ile tanımlanırken
tuple = (1, 'iki', 3)   # Tuple'lar normal parantez ya da parantezsiz tanımlanabilir.

print(type(list))       # Tip karşılaştırması Liste - Tuple
print(type(tuple))

print(list[2])          # Listelerde olduğu gibi
print(tuple[2])         # Tuple'larda da index ile verilere erişim mümkündür.

# list[0] = 0           # Listelerde eleman değiştirilebilirken.
# tuple[0] = 0          # Tuple'larda eleman değiştirilemez.

