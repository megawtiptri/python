class lingkaran:
    phi = 3.14

    def __init__(self,jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        self.luas = self.phi *self.jari_jari ** 2
        print(f"luas lingkaran : {self.luas}")
        
    def hitung_keliling(self):
        self.keliling = 2 *self.phi* self.jari_jari
        print(f"keliling lingkaran : {self.keliling}")
s1 = lingkaran(7)
s1.hitung_luas()
s1.hitung_keliling()
