# posisi
print("Argumen Posisi")
def desk(nama, usia, keunikan):
    print(f"{nama} berusia {usia} tahun dan memiliki keunikan: {keunikan}")
desk("Hanari", 20, "eye owl night")
print()

# keyword
print("Argumen Keyword")
desk("Hanari", usia=20, keunikan="eye owl night")
print()

# posisi default (Argpd)
print("Argumen posisi default")
def total(*angka):
    hasil = 0
    for n in angka:
        hasil += n
    return hasil
print("Total (1,2,3,4,5):", total(10, 10, 10, 10, 10))
print("Total (1,2,3,4,5,6,7):", total(5, 5, 5, 5, 5, 5, 5))
print()

# keyword default (Argkd)
print("argumen keyword default")
def highlight(**info):
    for kunci, nilai in info.items():
        print(f"{kunci}: {nilai}")
highlight(nama="Hanari", usia=20, kota="Tangerang selatan", hobi="mendengarkan musik")
print()

# kombinasi
print("argumen posisi default & argumen keyword default")
def info(*argpd, **argkd):
    print("Argpd:", argpd)
    print("Argkd:", argkd)
info(7, 7, 7, nama="Hanari", bahasa="Bilingual")
print()

# keyword only
print("argumen keyword only")
def create(nama, *, pulau, negara):
    print(f"Nama: {nama}, Pulau: {pulau}, Negara: {negara}")
create("Hanari", pulau="JAWA JAWA JAWA!", negara="Indonesia")
print()

# posisi only
print("argumen posisi only")
def tambah(a, b, /):
    return a + b
print("7 + 7 =", tambah(7, 7))


'''
1. Argumen Posisi                   : Argumen yang diberikan berdasarkan urutan posisi parameter dalam definisi fungsi.
2. Argumen Keyword                  : Argumen yang diberikan dengan menyebutkan nama parameter, sehingga urutan bebas.
3. Argumen Default                  : Argumen yang memiliki nilai default jika tidak diberikan saat pemanggilan fungsi.
4. Argpd                            : Argumen posisi dalam jumlah bebas, semua nilai masuk sebagai tuple.
5. Argkd                            : Argumen keyword dalam jumlah bebas, semua nilai masuk sebagai dictionary.
6. Kombinasi (Argpd) dan (Argkd)    : Fungsi yang dapat menerima argumen posisi dan keyword dalam jumlah bebas sekaligus.
7. Argumen Keyword Only             : Argumen yang wajib dipanggil dengan menyebutkan nama parameter, tidak bisa dengan posisi.
8. Argumen Posisi Only              : Argumen yang wajib dipanggil berdasarkan urutan posisi, tidak boleh menggunakan nama parameter.
'''