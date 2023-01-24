# membuat variable global
nama = "Python"
versi = "1.0.0"

def help():
    # variable lokal
    nama = "C#"
    versi = "1.0.2"
    print("Nama : %s" % nama)
    print("Versi : %s" % versi)


help()
