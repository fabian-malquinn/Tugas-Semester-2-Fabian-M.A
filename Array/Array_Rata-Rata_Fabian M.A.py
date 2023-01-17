# Deklarasikan Array
array = []
# Membuat Variable Total
total = 0
# Membuat Variable x Untuk Menampung Jumlah Array Yang Di Inputkan
n = int(input("Masukkan Jumlah Elemen Array : "))

for x in range(n):
    # Inputkan Nilai Yang Akan Bertambah 1
    nilai = float(input("Masukkan Nilai Ke- {} : ".format(x+1)))
    array.append(nilai)
    # Menampilkan Jumlah Dari Nilai
    print("\nHasil Nilai Total Adalah : {}".format(sum(array)))
    # Menampilkan Rata Rata
    print("\nHasil Nilai Total Adalah : {}".format(sum(array)/n))
