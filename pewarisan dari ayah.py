class ayah:
    sifat = "penyayang"
    warnakulit = "sawo matang,"
    bentukhidung = "mancung,"
    bentukmata = "sipit,"

    def turunan(self):
         print("sifat yang diturunkan dari ayah")

class Saya(ayah):
    def turunan(self):
        print(f"saya mewarisi bentukmata {self.bentukmata} dari ayah")

class adik(ayah):
    def turunan(self):
        print(f"adik mewarisi bentukhidung{self.bentukhidung} dari ayah")

ay = ayah()
ay.turunan()
sa = Saya()
sa.turunan()
ad = adik()
ad.turunan()


     