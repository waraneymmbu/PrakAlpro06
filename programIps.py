def hitung_ips():
    jumlah_matkul = int(input("Berapa Jumlah Mata Kuliah? "))

    sks_per_matkul = 3
    total_bobot = 0

    for i in range(1, jumlah_matkul + 1):
        while True:
            nilai = input(f"Nilai MK {i}: ")
            if nilai == 'A':
                bobot = 4
            elif nilai == 'B':
                bobot = 3
            elif nilai == 'C':
                bobot = 2
            elif nilai == 'D':
                bobot = 1

            total_bobot += bobot * sks_per_matkul
            break

    total_sks = jumlah_matkul * sks_per_matkul
    ips = total_bobot / total_sks

    print(f"Nilai IPS Anda Semester Ini {ips:.2f}")

hitung_ips()
