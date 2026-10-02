class HashTableMahasiswa:
    """Menyimpan dan mencari data mahasiswa berdasarkan NIM."""

    def __init__(self):
        self.data = {}

    def tambah(self, mahasiswa):
        nim = mahasiswa["nim"]
        if nim in self.data:
            return False
        self.data[nim] = mahasiswa
        return True

    def cari(self, nim):
        return self.data.get(nim)

    def hapus(self, nim):
        return self.data.pop(nim, None)
