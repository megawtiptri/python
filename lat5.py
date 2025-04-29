class segitiga :
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
         luas = 0.5 * self.alas * self.tinggi
         print("luas segitiga" , luas)
s1 = segitiga(10, 20)
s1.luas()