buah =["jeruk","mangga","pisang"]
print(buah[0])
print(buah[1])

for i in buah:
    print(i)

buah.append("apel")
print(buah)

buah.remove("jeruk")
print(buah)

buah.pop()
print(buah)


angka = (1,2,3,4,5)

hasil_kuadrat=map(lambda x: x**2, angka)
print(hasil_kuadrat)
print(list(hasil_kuadrat))

def genap(x):
    return x%2==0

hasil_filter=filter(genap, angka)
print(list(hasil_filter))