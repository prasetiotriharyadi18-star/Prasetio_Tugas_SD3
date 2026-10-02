class ArrayMahasiswa:
    """Mengelola data mahasiswa secara berurutan menggunakan list."""

    def __init__(self):
        self.data = []

    def tambah(self, mahasiswa):
        self.data.append(mahasiswa)

    def cari_indeks(self, nim):
        for indeks, mahasiswa in enumerate(self.data):
            if mahasiswa["nim"] == nim:
                return indeks
        return -1

    def hapus(self, nim):
        indeks = self.cari_indeks(nim)
        if indeks == -1:
            return None, -1
        return self.data.pop(indeks), indeks

    def pulihkan(self, mahasiswa, indeks):
        self.data.insert(indeks, mahasiswa)

    def tampilkan(self):
        if not self.data:
            print("Belum ada data mahasiswa.")
            return

        print("\n=== DAFTAR MAHASISWA ===")
        for nomor, mahasiswa in enumerate(self.data, start=1):
            print(
                f"{nomor}. NIM: {mahasiswa['nim']} | "
                f"Nama: {mahasiswa['nama']} | "
                f"Jurusan: {mahasiswa['jurusan']}"
            )
