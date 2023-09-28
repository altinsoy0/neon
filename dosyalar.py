# dosyalar.py

# Dosyaya yazma işlemi
def dosyaya_yaz(dosya_adi, icerik):
    with open(dosya_adi, 'w') as dosya:
        dosya.write(icerik)
    print(f"{dosya_adi} adlı dosyaya yazma işlemi tamamlandı.")

# Dosyadan okuma işlemi
def dosyadan_oku(dosya_adi):
    try:
        with open(, 'r') as dosya:
            icerik = dosya.read()
            print(f"{dosya_adi} adlı dosyanın içeriği:\n{icerik}")
    except FileNotFoundError:
        print(f"{dosya_adi} adlı dosya bulunamadı.")

# Test etmek için bir dosya adı ve içerik belirleyelim
test_dosya_adi = 'test_dosyasi.txt'
test_icerik = 'Bu dosyaya yazılan içerik.'

# Dosyaya yazma 
dosyaya_yaz(test_dosya_adi, test_icerik)

# Dosyadan okuma 
dosyadan_oku(test_dosya_adi)
