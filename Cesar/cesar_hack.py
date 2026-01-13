Alfabeto_Latino="abcdefghijklmnopqrstuvwxyz"

Criptograma=input("Digite el mensaje Cifrado ")
Salida=""
Clave=1

print("Criptograma: " , Criptograma)
while (Clave<=len(Alfabeto_Latino)):
      
    for Caracter in Criptograma.lower():
        if Caracter in Alfabeto_Latino:
            Posicion_Caracter=Alfabeto_Latino.find(Caracter)
            Posicion_Caracter= (Posicion_Caracter - Clave) % len(Alfabeto_Latino)
            Salida+=Alfabeto_Latino[Posicion_Caracter]
        else :
            Salida+=Caracter
    print("Clave ", Clave , " : ", Salida)
    Salida=""
    Clave+=1
