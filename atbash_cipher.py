"""
Atbash Cipher
A classical substitution cipher that replaces each letter with its
corresponding letter from the reversed alphabet.
The same algorithm is used for both encryption and decryption.

"""
alphabet="abcdefghijklmnopqrstuvwxyz "
cipher_alphabet="ZYXWVUTSRQPONMLKJIHGFEDCBA "

message=input("Typer the text to crypt/decrypt: ")
output=""

# Iterate over each character in the message and substitute it
# with the character at the same index in the cipher alphabet

for character in message.lower():
    if character in alphabet:
        cipher=cipher_alphabet[alphabet.index(character)]
        output+=cipher

print(output)