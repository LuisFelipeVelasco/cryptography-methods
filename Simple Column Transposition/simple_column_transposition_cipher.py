import pyperclip ,math,spanish_detector as Sp

def main():
    User_Action=input("Do you want Decrypte (D) or Encrypte (C)? or Break(B) ")
    Message=input("Type your message to Encrypte/Decrypte/Break ")
    Message=Reset_Message(Message)
    Output=""
    if (User_Action!="B"): key=int(input("Type the key: "))
    if (User_Action=="C"): Output= splitWordIntoParts(Encrypt(Message,key,Output))
    if (User_Action=="D"): Output= DesEncrypt(Message,key,Output)
    if (User_Action=="B"): Output=Break(Message,Output)
    else : print("Type a correct value ")
    print("") 
    print(Output)
    pyperclip.copy(Output) 


def Reset_Message(Message):
    Latin_Alphabet="abcdefghijklmnopqrstuvwxyz"
    Final_Message=""
    for caracter in Message.lower():
        if caracter in Latin_Alphabet:
            Final_Message+=caracter
    return Final_Message

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

def splitWordIntoParts(Output):
    Number_Of_Caracteres_Joined=int(input("How many words do you want to join together in the message? "))  
    Number_Of_Spaces=1
    List_Of_Output=list(Output)
    while(Number_Of_Spaces<=int(len(Output)/Number_Of_Caracteres_Joined)):
        Position_Of_Space=((Number_Of_Caracteres_Joined+1)*Number_Of_Spaces)-1
        List_Of_Output.insert(Position_Of_Space," ")
        Number_Of_Spaces+=1
    Output="".join(List_Of_Output)
    return Output

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

def ResetMessageToDesencrypt(Message,Number_of_Columns,key):
    Number_of_Empty_Cells=(Number_of_Columns*key) - len(Message)
    Number_of_Cells_Between_Spaces=Number_of_Columns-1
    List_Of_Message=list(Message)
    for i in range(len(Message), (len(Message)-1)-((Number_of_Empty_Cells-1)*Number_of_Cells_Between_Spaces), -Number_of_Cells_Between_Spaces):
        List_Of_Message.insert(i," ")    
    Message="".join(List_Of_Message)
    return Message  

def Break(Message,Output):
    lexic_value=0
    current_lexic_value=0
    is_Greater_Then_The_Current_Lexic_Value=True
    key=2
    while (current_lexic_value<=0.5 or  is_Greater_Then_The_Current_Lexic_Value==True):
        Output=" "
        Output=DesEncrypt(Message,key,Output)
        lexic_value=len(Sp.Detect_Number_Of_Words_In_Spanish(Output))/len(Output)
        if lexic_value<current_lexic_value: 
            is_Greater_Then_The_Current_Lexic_Value=False
        else: 
            current_lexic_value=lexic_value
            Posible_Output=Output
        key+=1
    return Posible_Output


main()
