class Personel:
    def __init__(self, adi, departmani, calisma_yili, maas):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maas = maas


    def bilgileri_goster(self):
        print("Adı:", self.adi)
        print("Departmanı:", self.departmani)
        print("Çalışma Yılı:", self.calisma_yili)
        print("Maaş:", self.maas)

class Firma():
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            personel.bilgileri_goster()
            print()

    def maas_zammi(self, personel, zam_orani):
        for p in self.personel_listesi:
            if p == personel:
                p.maas += (p.maas * zam_orani / 100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)



personel1 = Personel("Ahmet", "Muhasebe", 2018, 5000)
personel2 = Personel("Ayşe", "İnsan Kaynakları", 2019, 4500)

firma = Firma()

firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

print("Firma Çalışanları:")
firma.personel_listele()

print("Maaş Zammı Uygulanıyor...\n")
firma.maas_zammi(personel1, 10)

print("Yeni Maaşlar:")
firma.personel_listele()

print("Bir Personel Çıkartılıyor...")
firma.personel_cikart(personel2)

print("Güncel Çalışanlar:")
firma.personel_listele()


