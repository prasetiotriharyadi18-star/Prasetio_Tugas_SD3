from sistem_akademik import SistemAkademik


def main():
    sistem = SistemAkademik()

    while True:
        print("\n" + "=" * 40)
        print("          SISTEM AKADEMIK")
        print("=" * 40)
        print("1. Tambah mahasiswa")
        print("2. Tampilkan mahasiswa")
        print("3. Cari mahasiswa berdasarkan NIM")
        print("4. Hapus mahasiswa")
        print("5. Undo tindakan terakhir")
        print("6. Tambah antrean pemrosesan")
        print("7. Proses antrean")
        print("8. Tampilkan antrean")
        print("0. Keluar")
        print("=" * 40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan nama: ").strip()
            jurusan = input("Masukkan jurusan: ").strip()
            sistem.tambah_mahasiswa(nim, nama, jurusan)
        elif pilihan == "2":
            sistem.tampilkan_mahasiswa()
        elif pilihan == "3":
            nim = input("Masukkan NIM: ").strip()
            sistem.cari_mahasiswa(nim)
        elif pilihan == "4":
            nim = input("Masukkan NIM yang akan dihapus: ").strip()
            sistem.hapus_mahasiswa(nim)
        elif pilihan == "5":
            sistem.batalkan()
        elif pilihan == "6":
            nim = input("Masukkan NIM ke antrean: ").strip()
            sistem.tambah_antrean(nim)
        elif pilihan == "7":
            sistem.proses_antrean()
        elif pilihan == "8":
            sistem.tampilkan_antrean()
        elif pilihan == "0":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
