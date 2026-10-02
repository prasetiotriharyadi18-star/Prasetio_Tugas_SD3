class StackUndo:
    """Menyimpan riwayat tindakan dengan prinsip LIFO."""

    def __init__(self):
        self.riwayat = []

    def push(self, aksi):
        self.riwayat.append(aksi)

    def pop(self):
        if not self.riwayat:
            return None
        return self.riwayat.pop()

    def kosong(self):
        return len(self.riwayat) == 0
