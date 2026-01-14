
"""
Simple Columnar Transposition Cipher

The columnar transposition cipher is a classical encryption
method used historically before modern cryptography.
It does not change the letters of the message, but instead
rearranges their positions using a matrix structure.

How it works (simple explanation):
- The plaintext is written row by row into a table (matrix).
- The number of columns is determined by a numeric key.
- The encrypted text is produced by reading the table
column by column from top to bottom.

"""


import math,english_detector as en

def main():
    User_Action=input("Do you want Decrypt (D) or Encrypt (C)? or Break(B)?: ")
    Message=input("Type your message to Encrypt/Decrypt/Break ")
    Message=Reset_Message(Message)
    Output=""
    if (User_Action!="B"): key=int(input("Type the key: "))
    if (User_Action=="C"): Output= splitWordIntoParts(Encrypt(Message,key,Output))
    if (User_Action=="D"): Output= DesEncrypt(Message,key,Output)
    if (User_Action=="B"): Output=Break(Message,Output)
    else : print("Type a correct value ")
    print("") 
    print(Output)

#Verify if the each character of the message is in the alphabet
#If one character is not in the alphabet , is ommited 

def Reset_Message(Message):
    Alphabet="abcdefghijklmnopqrstuvwxyz"
    Final_Message=""
    for caracter in Message.lower():
        if caracter in Alphabet:
            Final_Message+=caracter
    return Final_Message

# Key = Number_Of_Columns
# Build the ciphertext column by column.
# Start with the first character, then take characters at positions:
# i, i + key, i + 2*key... simulating a vertical read of each column.
# Once a column is completed, move to the next column and repeat
# until all columns are processed.

def Encrypt(Message,key,Output):
    Number_of_Rows=math.ceil(len(Message)/key)
    Row=0
    Column=1
    while(Column<=key):
        for i in range(Row,Number_of_Rows*key,key):
            if i<len(Message):Output+=Message[i]
        Row+=1
        Column+=1
    return Output

# Divide the text into parts of the same lenght (Defined by the user) that are separated by spaces 

def splitWordIntoParts(Output):
    Number_Of_Caracteres_Joined=int(input("How many words do you want to join together in the message?: "))  
    Number_Of_Spaces=1
    List_Of_Output=list(Output)
    while(Number_Of_Spaces<=int(len(Output)/Number_Of_Caracteres_Joined)):
        Position_Of_Space=((Number_Of_Caracteres_Joined+1)*Number_Of_Spaces)-1
        List_Of_Output.insert(Position_Of_Space," ")
        Number_Of_Spaces+=1
    Output="".join(List_Of_Output)
    return Output

# Key= Number_Of_Rows
# Call the function ResetMessageToDesencrypt() to:
# Distribuite the encrypt message as a text rewrite it in a matrix
# Build the text column by column
# Start with the first character, then take characters at positions:
# i, i + Number_Of_Columns, i + 2*Number_Of_Columns... simulating a vertical read of each column.
# Once a column is completed, move to the next column and repeat
# until all columns are processed. 

def DesEncrypt(Message,key,Output):
    Number_of_Columns=math.ceil(len(Message)/key)   
    Message=ResetMessageToDesencrypt(Message,Number_of_Columns,key)      
    Row=0
    Column=1    
    while(Column<=Number_of_Columns):
        for i in range(Row,Number_of_Columns*key,Number_of_Columns):
            if i<len(Message):Output+=Message[i]
        Row+=1
        Column+=1
    Output=Reset_Message(Output)
    return Output

#Rewrite the encrypted message  by inserting
#spaces in positions corresponding to empty cells
#Simulating that the text is being writing in a matrix

def ResetMessageToDesencrypt(Message,Number_of_Columns,key):
    Number_of_Empty_Cells=(Number_of_Columns*key) - len(Message)
    Number_of_Cells_Between_Spaces=Number_of_Columns-1
    List_Of_Message=list(Message)
    for i in range(len(Message), (len(Message)-1)-((Number_of_Empty_Cells-1)*Number_of_Cells_Between_Spaces), -Number_of_Cells_Between_Spaces):
        List_Of_Message.insert(i," ")    
    Message="".join(List_Of_Message)
    return Message  

# Attempts to break the columnar transposition cipher by testing
# different keys and evaluating how "English-like" the result is.
#
# The process stops when:
# - The lexical value exceeds 0.5
# - A larger key produces a worse lexical score
#
# The best candidate is returned as the most probable plaintext.

def Break(Message,Output):
    lexic_value=0
    current_lexic_value=0
    is_Greater_Then_The_Current_Lexic_Value=True
    key=2
    while (current_lexic_value<=0.5 or  is_Greater_Then_The_Current_Lexic_Value==True):
        Output=" "
        Output=DesEncrypt(Message,key,Output)
        lexic_value=len(en.Detect_Number_Of_Words_In_English(Output))/len(Output)
        if lexic_value<current_lexic_value: 
            is_Greater_Then_The_Current_Lexic_Value=False
        else: 
            current_lexic_value=lexic_value
            Posible_Output=Output
        key+=1
    return Posible_Output


main()
