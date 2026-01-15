"""
Cesar Cipher Brute-Force Decryption

This program demonstrates how an encrypted message produced using
the Cesar cipher can be broken by trying every possible key.
Because the Cesar cipher uses a very small and predictable key space,
all potential plaintexts can be generated and examined.

For example, a message encrypted with an unknown shift value can be
decrypted by testing all shifts from 1 to 25 until a readable result
appears. This technique is known as a brute-force attack.

"""
alphabet="abcdefghijklmnopqrstuvwxyz"

cryptogram=input("Type the text encrypt: ")
output=""
key=1

print("cryptogram: " , cryptogram)

# Iterate over each character in the message to find its position in the alphabet
# Subtract the current key
# Use modulo arithmetic to wrap around the alphabet length
# Repeat the process for all posible keys 

while (key<=len(alphabet)):
      
    for character in cryptogram.lower():
        if character in alphabet:
            character_Position=alphabet.find(character)
            character_Position= (character_Position - key) % len(alphabet)
            output+=alphabet[character_Position]
        else :
            output+=character
    print("key ", key , " : ", output)
    output=""
    key+=1
