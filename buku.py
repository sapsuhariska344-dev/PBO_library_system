class Buku:
    def __init__(self, kode, judul, penulis):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        print(f"Kode Buku : {self.kode}")
        print(f"Judul     : {self.judul}")
        print(f"Penulis   : {self.penulis}")
        print("-" * 30)

buku1 = Buku("B001", "Pemrograman Python", "Guido van Rossum")
buku2 = Buku("B002", "Struktur Data", "Mark Allen Weiss")

buku1.tampilkan()
buku2.tampilkan()
