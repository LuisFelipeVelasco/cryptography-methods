
def Detect_Number_Of_Words_In_Spanish(user_text):
    file_path = "L:\Proyectos Ing.Sistemas\Proyectos programacion pyton\Ejercicios Libro Criptografia Sin Secretos Con Python\Spanish_Dictionary.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    lenght_of_user_text=len(user_text)
    list_of_user_words_in_Spanish=[]
    i = 0
    while i < lenght_of_user_text - 4:
        final_character = 4
        while final_character <= 20 and (final_character + i) <= lenght_of_user_text:
            word = user_text[i:i + final_character]

            if word in words:
                list_of_user_words_in_Spanish.append(word)
                i += final_character   
                break

            final_character += 1
        else:
            i += 1     
    return "".join(list_of_user_words_in_Spanish)

