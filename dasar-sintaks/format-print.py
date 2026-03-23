# basic
print("Print dasar")
print("Hii, saya Hanari!")
print(100)
print(3.14)
print(True)
print()

# lebih dari satu nilai
print("Print banyak nilai")
nama = "Hanari"
usia = 20
kelamin = "unknown"
print("Nama:", nama, "| Usia:", usia, "| Kelamin:", kelamin)
print()

# Sep dan End
print("Separator dan End")
print("apel", "bluberry", "semangka", sep=" - ")
print("apel", "bluberry", "semangka", sep=", ")
print("Halo", end=" ")
print("ini buah kesukaan ku!")
print()

# f-string
print("f-string")
tinggi = 1.69
print(f"Nama: {nama}")
print(f"Usia: {usia} tahun")
print(f"Tinggi: {tinggi:.2f} meter")
print()

# Alignment
print("Alignment")
print(f"{'Nama':<9} {'Usia':>7} {'Wilayah':^10}")
print(f"{'Hanari-1':<9} {21:>5} {'JAWA':^10}")
print(f"{'Hanari-2':<9} {20:>5} {'JAWA':^10}")
print(f"{'Hanari-3':<9} {19:>5} {'JAWA':^10}")
print()

# angka
print("Format angka")
harga = 2500000
diskon = 0.50
pi = 3.14159265

print(f"Harga           : Rp{harga:,.0f}")
print(f"Diskon          : {diskon:.0%}")
print(f"Pi              : {pi:.9f}")
print(f"Biner           : {100:b}")
print(f"Heksadesimal    : {270:x}")
print()

# Print Tabel Sederhana
print("Tabel Sederhana")
print(f"{'No':<5} {'Nama':<5} {'Nilai':>10}")
print("-" * 25)
data_siswa = [
    (1, "Hanari-1", 95),
    (2, "Hanari-2", 92),
    (3, "Hanari-3", 90),]
for no, nama, nilai in data_siswa:
    print(f"{no:<5} {nama:<5} {nilai:>10}")


'''
1. Print Dasar               : Mencetak teks, angka, dan nilai boolean.
2. Print Banyak Nilai        : Mencetak beberapa nilai sekaligus dengan pemisah default spasi.
3. Separator dan End         : Menggunakan parameter sep untuk mengubah pemisah antar nilai dan end untuk mengubah karakter akhir setelah mencetak.
4. f-string                  : Format string yang memungkinkan penyisipan variabel dan ekspresi dengan sintaks yang mudah dibaca.
5. Alignment                 : Menyelaraskan teks ke kiri, kanan, atau tengah dalam lebar tertentu.
6. Format Angka              : Memformat angka dengan pemisah ribuan, desimal, persentase, dan format bilangan lainnya.
7. Print Tabel Sederhana     : Mencetak data dalam format tabel dengan header dan pemisah garis.
'''
