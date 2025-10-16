angka = int(input("Masukkan angka: "))

if angka > 1:
    for i in range(2, angka):
        if angka % i == 0:
            print(angka, "bukan bilangan prima")
            break
    else:
        print(angka, "adalah bilangan prima")


batas_awal = int(input("Masukkan batas awal: "))
batas_akhir = int(input("Masukkan batas akhir: "))

print(f"Bilangan prima dari {batas_awal} sampai {batas_akhir}:")
for angka in range(batas_awal, batas_akhir + 1):
    if angka > 1:
        for i in range(2, angka):
            if angka % i == 0:
                break
        else:
            print(angka)
