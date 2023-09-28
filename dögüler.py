# Bir for döngüsü, bir dizi (liste, tuple, sözlük , küme veya bir dize) üzerine yenilemek için kullanılır.

kisiler = ['Yusuf', 'Yasin', 'Ali', 'Mustafa' ]

# Basit bir for döngüsü
for kisi in kisiler:
  print(f'Geçerli Kişi: {kisi}')

# Break (döngüyü kırma)
for kisi in kisiler:
  if kisi == 'Ali':
    continue
    print(f'Geçerli kişi: {kisi}')

# Contiune (Devam et) 
for kisi in kisiler:
  if kisi == 'Ali':
    continue
    print(f'Geçerli kişi: {kisi}')

#Range
for i in range(len(kisiler)):
  print(kisiler[i])

for i in range(0, 11):
  print(f'sayı: {i}' ) 

# While döngüleri ,bir koşul doğru olduğu sürece belirli bir dizi ifadeyi çalıştırır.

sayac = 0
while sayac < 10:
  print(f'Sayac: {sayac}')
  sayac += 1
