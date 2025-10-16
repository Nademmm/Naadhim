batas_awal = int(input("masukkan batas awal: "))
batas_akhir = int(input("masukkan batas akhir: "))

for i in range(batas_awal, batas_akhir+1):
    if i%2 ==0:
        print (i, "adalah Bilangan Genap")
    else:
        print (i, "adalah Bilangan Ganjil")