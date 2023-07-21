import string

def caesar_encrypt(txt, shift):
    alphabet = string.ascii_lowercase
    encrypted_word = ''
    for letter in txt:
        if letter.lower() in alphabet:
            is_upper = letter.isupper()
            letter = letter.lower()
            idx = (alphabet.index(letter) + shift) % 26
            encrypted_letter = alphabet[idx]
            if is_upper:
                encrypted_letter = encrypted_letter.upper()
            encrypted_word += encrypted_letter
        else:
            encrypted_word += letter
    return encrypted_word

def caesar_decrypt(txt, shift):
    return caesar_encrypt(txt, -shift)

if __name__ == "__cezar_code__":
    while True:
        option = input("Enter 'e' to encrypt, 'd' to decrypt or ex to exit: ")
        if option == 'e':
            enter_txt = input("Enter a word or a sentence to code: ")
            shift_amount = int(input("Enter the shift amount: "))
            result = caesar_encrypt(enter_txt, shift_amount)
            print("Encrypted message:", result)
        elif option == 'd':
            enter_txt = input("Enter a word or a sentence to decode: ")
            shift_amount = int(input("Enter the shift amount: "))
            result = caesar_decrypt(enter_txt, shift_amount)
            print("Decrypted message:", result)
        elif option == "ex":
            break
        else:
            print("Invalid option. Please enter 'e' to encrypt, 'd' to decrypt or 'ex' to exit.")
