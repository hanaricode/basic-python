if kondisi:
  aksi1      #harus diawali karakter spasi atau tab
  aksi2      #harus diawali karakter spasi atau tab

#Jika hanya terdiri dari satu aksi
if kondisi:aksi

x = 10
if x % 2 = 0:
  print ("%d merupakan bilangan genap")


#Jika terdiri dari dua aksi
if kondisi:
  aksi1
else:
  aksi2

x = -17
if x > 0:
  print("%d merupakan bilangan positif" % x)
else:
  print("%d bukan bilangan positif" % x)


#Jika terdiri dari tiga aksi atau lebih
if kondisi1:
  aksi1
elif kondisi2:
  aksi2
elif kondisi3:
  aksi3
else:
  aksi4

x = 0
if x > 0:
  print("%d bilangan positif" %x x)
elif x == 0:
  print("anda memasukan nilai 0")
else:
  print("%d bilangan negatif" % x)

-----------------------

cheese = 0
while cheese <= 10:
  cheese = cheese + 1
  if cheese % 2 == 0:
    print("nilai cheese dengan bilangan genap: ", cheese)
print("Sudah di luar kondisi while.")

-----------------------

# Print banyak tanpa harus ngetik satu satu
for i in range (100):
  name = "Saya Hanari"
  print ("haii, " + name)


