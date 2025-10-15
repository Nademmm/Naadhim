def calculator (a,b,operasi):
    if (operasi == "+"):
        return a+b
    if (operasi == "-"):
        return a-b
    if (operasi == "x"):
        return a*b
    if (operasi == ":"):
        return a/b
    
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+/-/x/:): ")

hasil = calculator(a, b, operasi)
print(f"Hasilnya adalah: {hasil}")