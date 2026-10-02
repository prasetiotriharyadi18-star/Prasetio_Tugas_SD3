from array_mahasiswa import ArrayMahasiswa
from stack_undo import StackUndo
from queue_proses import QueueProses
from hash_table_mahasiswa import HashTableMahasiswa


class SistemAkademik:
    """Mengintegrasikan struktur data untuk sistem akademik."""

    def __init__(self):
        self.mahasiswa = ArrayMahasiswa()
        self.undo = StackUndo()
        self.antrean = QueueProses()
        self.indeks = HashTableMahasiswa()

    def tambah_mahasiswa(self, nim, nama, jurusan):
        if not nim or not nama or not jurusan:
            print("Semua data wajib diisi.")
            return

        if self.indeks.cari(nim) is not None:
            print("Gagal: NIM sudah terdaftar.")
            return

        data = {"nim": nim, "nama": nama, "jurusan": jurusan}
        self.mahasiswa.tambah(data)
        self.indeks.tambah(data)
        self.undo.push(("tambah", data))
        print(f"Mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan_mahasiswa(self):
        self.mahasiswa.tampilkan()

    def cari_mahasiswa(self, nim):
        data = self.indeks.cari(nim)
        if data is None:
            print("Mahasiswa tidak ditemukan.")
            return

        print("\n=== HASIL PENCARIAN ===")
        print(f"NIM     : {data['nim']}")
        print(f"Nama    : {data['nama']}")
        print(f"Jurusan : {data['jurusan']}")

    def hapus_mahasiswa(self, nim):
        if self.indeks.cari(nim) is None:
            print("Mahasiswa tidak ditemukan.")
            return

        data, indeks = self.mahasiswa.hapus(nim)
        self.indeks.hapus(nim)
        self.undo.push(("hapus", data, indeks))
        print(f"Mahasiswa {data['nama']} berhasil dihapus.")

    def batalkan(self):
        aksi = self.undo.pop()
        if aksi is None:
            print("Tidak ada tindakan yang dapat dibatalkan.")
            return

        if aksi[0] == "tambah":
            data = aksi[1]
            self.mahasiswa.hapus(data["nim"])
            self.indeks.hapus(data["nim"])
            print(f"Penambahan {data['nama']} berhasil dibatalkan.")
        elif aksi[0] == "hapus":
            data, indeks = aksi[1], aksi[2]
            self.mahasiswa.pulihkan(data, indeks)
            self.indeks.tambah(data)
            print(f"Penghapusan {data['nama']} berhasil dibatalkan.")

    def tambah_antrean(self, nim):
        if self.indeks.cari(nim) is None:
            print("NIM tidak terdaftar.")
            return

        self.antrean.tambah(nim)
        print(f"NIM {nim} berhasil masuk antrean.")

    def proses_antrean(self):
        nim = self.antrean.proses()
        if nim is None:
            print("Antrean masih kosong.")
            return

        data = self.indeks.cari(nim)
        if data is None:
            print(f"Pemrosesan dibatalkan. NIM {nim} sudah tidak terdaftar.")
            return

        print("\n=== HASIL PEMROSESAN ===")
        print(f"NIM     : {data['nim']}")
        print(f"Nama    : {data['nama']}")
        print("Status  : Berhasil diproses.")

    def tampilkan_antrean(self):
        self.antrean.tampilkan()
