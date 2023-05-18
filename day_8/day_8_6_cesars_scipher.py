
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")
  
def decript(text, shift):
  decipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    decipher_text += alphabet[new_position]
  print(f"The decode text is {decipher_text}")

if direction =='encode':
    encrypt(text,shift)
else:
    decript(text,shift)