# basic
print("Input dasar")
nama = input("masukkan nama: ")
print(f"Halo, {nama}!")
print()

# angka
print("Input angka")
usia = int(input("konfirmasi usia: "))
print(f"usia kamu adalah {usia} tahun")
print()

# float
print("input float")
tinggi = float(input("konfirmasin tinggi badan (cm): "))
print(f"Tinggi badan kamu adalah {tinggi} cm")
print()

# validasi
print("input validasi")
nilai = int(input("Masukkan nilai ujian (0-100): "))
if 0 <= nilai <= 100:
    print(f"Nilai ujian mahasiswa: {nilai}")
else:
    print("Nilai tidak valid! Harus antara 0 sampai 100.")
print()

# nilai sekaligus
print("Input nilai lebih dari satu")
data = input("Masukan beberapa nilai dipisahkan dengan spasi: ")
nilai = list(map(int, data.split()))
print("Nilai yang dimasukkan:", nilai)
print("Total:", sum(nilai))
print()

# perulangan
print("Input dalam Perulangan")
total = 0
for i in range(5):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    total += angka
print("Total semua angka:", total)