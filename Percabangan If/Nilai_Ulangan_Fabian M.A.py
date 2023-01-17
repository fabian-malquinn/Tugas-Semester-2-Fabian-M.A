# Menginput Nilai Tugas, UTS, dan UAS
tugas = float(input("Masukkan Nilai Tugas : "))
uts = float(input("Masukkan Nilai UTS : "))
uas = float(input("Masukkan Nilai UAS : "))

# Menghitung Nilai Akhir Sesuai Dengan Bobot
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

# Menentukan Grade Berdasarkan Nilai Akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'

# Menentukan Status Kelulusan Berdasarkan Nilai Akhir
if nilai > 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"

# Menampilkan Nilai Akhir, Grade, dan Status Kelulusan
print("\nNilai Akhir: %0.2f" % nilai)
print("Grade: {}".format(grade))
print("Status: {}".format(status))
