from collections import deque


class QueueProses:
    """Mengelola antrean pemrosesan dengan prinsip FIFO."""

    def __init__(self):
        self.antrean = deque()

    def tambah(self, nim):
        self.antrean.append(nim)

    def proses(self):
        if not self.antrean:
            return None
        return self.antrean.popleft()

    def tampilkan(self):
        if not self.antrean:
            print("Antrean masih kosong.")
            return

        print("\n=== DAFTAR ANTREAN ===")
        for nomor, nim in enumerate(self.antrean, start=1):
            print(f"{nomor}. NIM: {nim}")
