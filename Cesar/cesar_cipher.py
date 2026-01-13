"""
Cesar Cipher

The Cesar cipher is one of the oldest known encryption techniques.
It is named after Julius Cesar, who reportedly used this method
to protect military messages in ancient Rome.

The cipher works by replacing each letter with another letter a fixed
number of positions away in the alphabet. For example, using a shift
of 3, the letter 'A' becomes 'D', 'B' becomes 'E', and 'Z' wraps around
to 'C'.

"""

alphabet="abcdefghijklmnopqrstuvwxyz"

user_action=input("Do you want decrypt (D) or encrypt (C)?:  ")
key=int(input("Type the key: "))

message=input("Type the message to encrypt/decrypt ")
output=""

# Iterate over each character in the message to find its position in the alphabet
# If the user chooses decryption, subtract the key from the character position
# If the user chooses encryption, add the key to the character position
# Use modulo arithmetic to wrap around the alphabet length

for character in message.lower():
        if character in alphabet:
            character_position=alphabet.find(character)
            if user_action=="C":
                  character_position= (character_position + key) % len(alphabet)
            if user_action=="D":
                  character_position= (character_position - key) % len(alphabet)
            output+=alphabet[character_position]
        else :
            output+=character

print(output)
