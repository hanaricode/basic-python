baris = 5
kolom = 5
array = [[0 for j in range(kolom)] for i in range(baris)]

# isi array pakai nested loop
for i in range(baris):
    for j in range(kolom):
        if j <= i:
            array[i][j] = 1
        else:
            array[i][j] = 0

# tampilkan hasilnya
for i in range(baris):
    for j in range(kolom):
        print(array[i][j], end=" ")
    print()
