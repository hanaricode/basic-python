#Menggunakan for
BARIS = 5
for i in range(1, BARIS+1):
  for j in range(i, i+1):
    print('%d ' % (i * j), end=' ')
  print() #ganti baris

#Menggunakan while
BARIS = 5
i = 1
while i <= BARIS:
  j = 1
  while j<= i:
      print('%d ' % (i * j), end=' ')
      j += 1
    print() #ganti baris
    i += 1

#Kombinasi for dan while
BARIS = 5
for i range(1, BARIS+1):
  j = 1
while j <=i:
  print('%d ' % (i * j), end=' ')
  j += 1
print() #ganti baris

#Bisa juga dengan seperti ini
BARIS = 5
i = 1
while i <= BARIS:
  for j in range(1, i+1):
    print('%d ' % (i * j), end=' ')
  print() #ganti baris
  i += 1

#Menambahkan fungsi sleep()
import time
BARIS = 5
KOLOM 3
for i in range(1, BARIS+1):
  print('Ketika i=%d: ' % i, end=' ')
for  j in range(i, KOLOM+1):
  print('[baris %d, kolom %d]' % (i, j), end=' ')
  time.sleep(1)
print() #ganti baris disetiap nilai 1

Ketika i=1: [baris 1, kolom 1] [baris 1, kolom 2] [baris 1, kolom 3]
ketika i=2: [baris 2, kolom 1] [baris 2, kolom 2] [baris 2, kolom 3]
ketika i=3: [baris 3, kolom 1] [baris 3, kolom 2] [baris 3, kolom 3]
ketika i=4: [baris 4, kolom 1] [baris 4, kolom 2] [baris 4, kolom 3]
ketika i=5: [baris 5, kolom 1] [baris 5, kolom 2] [baris 5, kolom 3]
        
  
