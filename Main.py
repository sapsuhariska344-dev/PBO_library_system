from Buku import Buku
from Anggota import Anggota

daftar_buku = []
daftar_anggota = []

def menu():
    print("\n=== SISTEM PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Tambah Anggota")
    print("4. Lihat Anggota")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        kode = input("Kode Buku   : ")
        judul = input("Judul Buku  : ")
        penulis = input("Penulis     : ")
        buku = Buku(kode, judul, penulis)
        daftar_buku.append(buku)
        print("✅ Buku berhasil ditambahkan")

    elif pilihan == "2":
        print("\n=== DAFTAR BUKU ===")
        if not daftar_buku:
            print("Belum ada data buku")
        else:
            for b in daftar_buku:
                b.tampilkan()

    elif pilihan == "3":
        nim = input("NIM Anggota  : ")
        nama = input("Nama Anggota : ")
        anggota = Anggota(nim, nama)
        daftar_anggota.append(anggota)
        print("✅ Anggota berhasil ditambahkan")

    elif pilihan == "4":
        print("\n=== DAFTAR ANGGOTA ===")
        if not daftar_anggota:
            print("Belum ada data anggota")
        else:
            for a in daftar_anggota:
                a.tampilkan()

    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem")
        break

    else:
        print("❌ Pilihan tidak valid")
