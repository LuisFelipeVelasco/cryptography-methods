Alfabeto_Latino="abcdefghijklmnopqrstuvwxyz "
Alfabeto_Cifrado="ZYXWVUTSRQPONMLKJIHGFEDCBA "

Mensaje=input("Digite su mensaje a cifrar/descifrar ")
NuevoMensaje=""

for Caracter in Mensaje.lower():
    if Caracter in Alfabeto_Latino:
        Cifra=Alfabeto_Cifrado[Alfabeto_Latino.index(Caracter)]
        NuevoMensaje+=Cifra

print(NuevoMensaje)