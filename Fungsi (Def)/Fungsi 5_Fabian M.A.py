def luas_persegi(sisi):
    return sisi*sisi


# Tidak Menghasilkan Output Apa Pun
luas_persegi(10)

# Menghasilkan Output
print("Luas Persegi Dengan Sisi 4 Adalah", luas_persegi(4))

# Kita Juga Bisa Simpan Di Dalam Variable
persegi_besar = luas_persegi(100)
persegi_kecil = luas_persegi(50)

print("Total Luas Persegi Besar Dan Aecil Adalah", persegi_besar + persegi_kecil)
