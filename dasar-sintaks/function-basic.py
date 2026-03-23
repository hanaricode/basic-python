# basic
print("Fungsi Sederhana")
def turun():
    print("Haii!")
turun()
print()

# parameter
print("Fungsi dengan Parameter")
def sebut(nama):
    print(f"Halo, {nama}!")
sebut("Hanari")
sebut("Python")
print()

# return
print("Fungsi dengan Return")
def tambah(a, b):
    return a + b
hasil = tambah(2, 7)
print("2 + 7 =", hasil)
print()

# parameter default
print("Parameter default")
def sapaan(nama, sapaan="Halo"):
    print(f"{sapaan}, {nama}!")
sapaan("Hanari")
sapaan("Hanari", "morning guys!")
print()

# Nilai return
print("Banyak Nilai Return")
def min_maks(angka):
    return min(angka), max(angka)
terkecil, terbesar = min_maks([3, 1, 7, 2, 9, 4])
print("Terkecil:", terkecil)
print("Terbesar:", terbesar)
print()

# fungsi lain
print("Fungsi Memanggil Fungsi Lain")
def kuadrat(n):
    return n * n
def jumlah_kuadrat(a, b):
    return kuadrat(a) + kuadrat(b)
print("Jumlah kuadrat (3, 4):", jumlah_kuadrat(3, 4))
print()

# Docstring
print("Docstring")
def kali(a, b):
    """
    mengalikan dua angka dengan,
    Parameternya:
        a: angka pertama
        b: angka kedua
    return:
        hasil perkalian a * b
    """
    return a * b
print("2 x 7 =", kali(2, 7))
print("Dokumentasi:", kali.__doc__)