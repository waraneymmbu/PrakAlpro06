
def ganjil(bawah, atas):
    step = 1 if bawah < atas else -1

    return [i for i in range(bawah, atas, step) if i % 2 != 0]

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

hasil_ganjil = ganjil(bawah, atas)

print("Deret bilangan ganjil:", end=" ")
for angka in hasil_ganjil:
    print(angka, end=", ")

