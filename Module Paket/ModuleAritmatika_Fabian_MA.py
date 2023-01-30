import Aritmatika_Fabian_MA


def main():
    a = int(input("Masukkan Nilai A : "))
    b = int(input("Masukkan Nilai B : "))

    print("A\t: ", a)
    print("B\t: ", b)

    print(f"\nA+B\t: {Aritmatika_Fabian_MA.tambah(a, b)}")
    print(f"A-B\t: {Aritmatika_Fabian_MA.kurang(a, b)}")
    print(f"A*B\t: {Aritmatika_Fabian_MA.kali(a, b)}")
    print(f"A/B\t: {Aritmatika_Fabian_MA.bagi(a, b)}")


if __name__ == "__main__":
    main()
