# Bir sözlük , sırasız değistirilebilir ve endekslenmis bir koleksiyondur. Tekrarlayan üyeler içermez.

# Öğrenci bilgi sistemi
ogrenci_bilgileri = {
    '101': {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'not': 90},
    '102': {'ad': 'Ayşe', 'soyad': 'Demir', 'not': 85},
    '103': {'ad': 'Mehmet', 'soyad': 'Kaya', 'not': 95},
}

# Öğrenci bilgilerini ekrana yazdırma fonksiyonu
def ogrenci_bilgilerini_yazdir(ogrenci_id):
    ogrenci = ogrenci_bilgileri.get(ogrenci_id)
    if ogrenci:
        print(f"Öğrenci ID: {ogrenci_id}")
        print(f"Adı: {ogrenci['ad']}")
        print(f"Soyadı: {ogrenci['soyad']}")
        print(f"Notu: {ogrenci['not']}")
    else:
        print(f"{ogrenci_id} numaralı öğrenci bulunamadı.")

# Test etmek için öğrenci ID'sini belirleyelim
test_ogrenci_id = '102'

# Fonksiyonu çağıralım
ogrenci_bilgilerini_yazdir(test_ogrenci_id)

