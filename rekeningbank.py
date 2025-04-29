class rekeningbank :
    def __init__(self,saldo_awal):
        self.__saldo = saldo_awal #saldo bersifat privat

    def lihat_saldo(self):
        print(f"saldo anda saat ini: Rp{self.__saldo}")

    def tambah_saldo(self,jumlah):
        # self.__saldo = self,__saldo + jumlah
        self.__saldo += jumlah
        print(f"jumlah saldo seluruhnya Rp{self.__saldo}")

rb = rekeningbank(10000)
rb.lihat_saldo()
rb.tambah_saldo(5000)
