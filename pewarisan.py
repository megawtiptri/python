class Hewan:
    def suara(self):
      print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
      print("Meong")

h = Hewan()
h.suara()
k = Kucing()
k.suara()