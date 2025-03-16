def perkalian(a, b):
    hasil = 0
    for i in range(a):
        hasil += b
    return hasil

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

hasil = perkalian(a, b)

penjumlahan_str = " + ".join([str(b)] * a)
print(f"{a} x {b} = {penjumlahan_str} = {hasil}")
