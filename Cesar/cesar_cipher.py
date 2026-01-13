import pyperclip

Alfabeto_Latino="abcdefghijklmnopqrstuvwxyz"

Accion_Usuario=input("Desea Descifrar (D) o Cifrar (C) ")
Clave=int(input("Digite la clave "))

Mensaje=input("Digite su mensaje a Cifrar/Descifrar ")
Salida=""

for Caracter in Mensaje.lower():
        if Caracter in Alfabeto_Latino:
            Posicion_Caracter=Alfabeto_Latino.find(Caracter)
            if Accion_Usuario=="C":
                  Posicion_Caracter= (Posicion_Caracter + Clave) % len(Alfabeto_Latino)
            if Accion_Usuario=="D":
                  Posicion_Caracter= (Posicion_Caracter - Clave) % len(Alfabeto_Latino)
            Salida+=Alfabeto_Latino[Posicion_Caracter]
        else :
            Salida+=Caracter

print(Salida)
pyperclip.copy(Salida)