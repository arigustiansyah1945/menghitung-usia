from datetime import date


def tahun():
    nama = str(input("Masukkan nama anda: "))
    tahun_lahir = int(input("Masukkan tahun lahir anda: "))
    tahun_sekarang = date.today().strftime("%Y")
    print("Umur", nama, "sekarang adalah: ", int(tahun_sekarang)-tahun_lahir)


tahun()
