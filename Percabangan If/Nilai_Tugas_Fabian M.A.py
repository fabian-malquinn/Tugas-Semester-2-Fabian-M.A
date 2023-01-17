nilai_tugas = int(input("Masukkan Nilai Tugas : "))

if nilai_tugas >= 80 and nilai_tugas <= 100:
    print("Nilai Tugas : A")
elif nilai_tugas >= 70:
    print("Nilai Tugas : B")
elif nilai_tugas >= 60:
    print("Nilai Tugas : C")
elif nilai_tugas < 60:
    print("Nilai Tugas : D")
else:
    print("Nilai Ketinggian")
