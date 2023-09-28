# Bir aınıf nesneleri oluşturmak için bir şablondur. Bir nesnenin ilişkilendirilmiş özellikleri ve metodları kullanma 
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.durum = 'Durdurulmuş'

    def calistir(self):
        self.durum = 'Çalışıyor'
        print(f"{self.marka} {self.model} çalıştırıldı.")

    def durdur(self):
        self.durum = 'Durdurulmuş'
        print(f"{self.marka} {self.model} durduruldu.")

    def durumu_goster(self):
        print(f"{self.marka} {self.model} durumu: {self.durum}")

# Araba sınıfından bir örnek oluşturma
araba1 = Araba(marka='Toyota', model='Corolla', yil=2020)

# Arabayı çalıştıralım
araba1.calistir()

# Arabanın durumunu gösterelim
araba1.durumu_goster()

# Arabayı durduralım
araba1.durdur()

# Arabanın güncellenmiş durumunu gösterelim
araba1.durumu_goster()
