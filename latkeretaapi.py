class keretaapi:
    def __init__(self, jenis, warna,type):
        self.jenis = jenis
        self.warna = warna
        self.tipe = type
    def berjalan(self):
        print(" kereta bisa berjalan")
    def berhenti(self):
        print(" kereta bisa berhenti")
s1 = keretaapi("Kereta wisata", "putih", "eksekutif")
print(s1.jenis)
print(s1.warna)
print(s1.tipe)
s1.berjalan()
s1.berhenti()
