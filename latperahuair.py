class perahuair:
    def __init__(self, jenis, ukuran, sumbertenaga,):
        self.jenis = jenis
        self.ukuran = ukuran
        self.sumbertenaga = sumbertenaga
    def bergerak (self):
        print(" perahuair bisa bergerak di air")
    def berhenti(self):
        print(" perahuair bisa berhenti")
s1 = perahuair("perahu layar", "besar", "angin")
print(s1.jenis)
print(s1.ukuran)
print(s1.sumbertenaga)
s1.bergerak()
s1.berhenti()