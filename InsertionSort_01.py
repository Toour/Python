a = [53,23,74,94,64,71,36,87,19,43,62,57,90,100,1,5,2,7]
print(a)
temp = 0
for x in range(0,len(a)):
    for y in range(0,len(a)):
        if (a[x] < a[y]):
            temp = a[x]
            a[x] = a[y]
            a[y] = temp



print(a)