
import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#Encryption
print("\n---------- Decryption -----------")
plain_text = input("\nEnter a message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("\nEncrypted message : ",cipher_text)

#Decryption
print("\n---------- Decryption -----------")
cipher_text = input("\nEnter a message to decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("\nDecrypted message : ",plain_text)
