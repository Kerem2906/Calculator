Sayı1 = float(input("Lütfen İstediğiniz Sayıyı Giriniz :"))
Sayı2 = float(input("Lütsen İkinci Sayıyı Giriniz :"))

İşlem = input("Lütfen İstediğiniz İşlemi '+' , '-' , '*' veya '/' ile Gösteriniz :")

if İşlem in ('x' , 'X' , '*'):
   Sonuç = Sayı1 * Sayı2
   print(Sonuç)
elif İşlem == '+':
   Sonuç = Sayı1 + Sayı2
   print(Sonuç)
elif İşlem == '-':
   Sonuç = Sayı1 - Sayı2
   print(Sonuç)
elif İşlem == '/':
   Sonuç = Sayı1 / Sayı2
   print(Sonuç)
else:
   print("Lütfen Geçerli Bir İşlem Giriniz")