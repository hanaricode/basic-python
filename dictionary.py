student = {"job": "engineering"} #job = key, engineering = value
print(student["job"], "\n")   #job = akses key(engineering = mendapatkan value)
                            
student = {"job":170.6}     #value bisa diganti/isi oleh semua tipe data
print(student["job"])
print()

student = {"job": ["engineering", 20]}  #job = akses key
print(student["job"][0], "\n")          #akses nomor indeks sesuai value (indeks dimulai dari 0 untuk pertama)

student = {"job": ["engineering", 20]}
print(student["job"][1])                #akses indeks ke 1 (kedua jika didalam list)
print()

student = { #data 1
    "job":{
        "department":"Mechanical Engineering",
        "course":"AutoCAD",
        "grade":"A+",
        "IPK":4.00
    },
    "desk":{ #data 2
        "department":"Electric Engineering",
        "course":"electric physics",
        "grade":"A",
        "IPK":3.95
    }
}
print(student["job"])
print()                                 #membuat 1 baris dilewati(kosong) bisa juga dengan
print(student["job"]["grade"])
print()
print(student["job"]["IPK"])
print()

#data 2 bisa dimanipulasi dengan menambahkan: student["desk"]["IPK"] = 4.0
print(student["desk"], "\n")           #"\n" = membuat 1 baris dilewati(kosong)tetapi harus didalam list
print(student["desk"]["grade"], "\n")
print(student["desk"]["IPK"], "\n")

