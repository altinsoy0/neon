# ıf/else koşulları, bir şeyin doğru veya yanlış olması durumunha bağlı karşılaştırmak için kullanılır

a = 11
b = 12

#karşılaştırma Operatörleri (==,  !=, >, <, >=, <=) - Değerleri karşılaştırmak için kullanılır

# Basit bir if
if a > b: 
  print(f'{a} {b}\'dan büyüktür')

# If/else 
if a > b: 
  print(f'{a} {b}\'dan büyüktür ')
else:
  print(f'{b} {a}\'dan büyüktür ')

#elif
if a > b: 
  print(f'{a} {b}\'dan büyüktür ')
elif a == b:
  print(f'{a} {b}\'e eşittir')
else:
   print(f'{b} {a}\'dan büyüktür')

# İç içe geçmiş if
if a > 2:
  if a <= 10:
    print(f"{a} 2\ 'den büyük ve 10'a küçüktür")

#Mantıksal operatörler (and, or. not) - Koşullu ifadeleri birleştirmek için kulllanılır

#and 
if a > 2 or and a <=: 
  print(f"{a} 2'den büyük ve 10'a küçüktür ")

# or
if a > 2 or  
