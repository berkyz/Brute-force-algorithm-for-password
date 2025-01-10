import itertools
import string

# Kullanılacak karakter kümesi
characters = string.ascii_letters + string.digits  # Küçük + büyük harfler + rakamlar

# Şifre uzunlukları
min_length = 5
max_length = 10

# Dosyaya yazma
with open("all_possible_passwords.txt", "w") as file:
    # 5 ile 10 haneli tüm kombinasyonları oluştur
    for length in range(min_length, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            # Şifreyi birleştirip dosyaya yaz
            file.write("".join(password) + "\n")
            print("".join(password))

print("Şifreler başarıyla dosyaya yazıldı!")
