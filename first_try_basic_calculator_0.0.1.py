Sayı1 = float(input("Lütfen İstediğiniz Sayıyı Giriniz :"))
Sayı2 = float(input("Lütsen İkinci Sayıyı Giriniz :"))

İşlem = input("Lütfen İstediğiniz İşlemi '+' , '-' , '*' veya '/' ile Gösteriniz :")

if İşlem == 'x' or İşlem == 'X' or İşlem == '*':
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
elif İşlem != '-' or İşlem != '*' or İşlem != '+' or İşlem != 'X' or İşlem != 'x' or İşlem != '/':
   print("Lütfen Geçerli Bir İşlem Giriniz")
