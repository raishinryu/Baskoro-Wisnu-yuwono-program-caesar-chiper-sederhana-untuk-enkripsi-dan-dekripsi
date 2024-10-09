# Fungsi untuk enkripsi
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Fungsi untuk dekripsi
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Program utama
def main():
    while True:
        choice = input("Pilih (1) Enkripsi atau (2) Dekripsi: ")
        text = input("Masukkan teks: ")
        shift = int(input("Masukkan nilai shift: "))

        if choice == '1':
            print("Hasil enkripsi:", caesar_cipher_encrypt(text, shift))
        elif choice == '2':
            print("Hasil dekripsi:", caesar_cipher_decrypt(text, shift))

        if input("Coba lagi? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
