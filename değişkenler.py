# ıf/Else koşulları, bir şeyin doğru veya yanlış olmasına bağlı olarak bir şey yapmayı kararlaştırmak için kullanılır.

def kredi_hesapla(mevduat, gelir):
    # Kredi hesaplama koşulları
    if mevduat > 10000:
        if gelir > 50000:
            kredi_miktari = 0.5 * gelir
            print(f"Yüksek mevduat ve yüksek geliriniz var. Kredi miktarınız: {kredi_miktari}")
        else:
            print("Yüksek mevduatınız var ancak geliriniz yetersiz.")
    elif mevduat > 5000:
        if gelir > 30000:
            kredi_miktari = 0.3 * gelir
            print(f"Orta mevduat ve orta geliriniz var. Kredi miktarınız: {kredi_miktari}")
        else:
            print("Orta mevduatınız var ancak geliriniz yetersiz.")
    else:
        print("Mevduat yetersiz. Kredi başvurusu reddedildi.")

# Test etmek için mevduat ve gelir değerlerini belirleyelim
test_mevduat = 12000
test_gelir = 60000

# Fonksiyonu çağıralım
kredi_hesapla(test_mevduat, test_gelir)

