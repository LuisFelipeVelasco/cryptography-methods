
#Read the english_dictionary.txt and make a list of all the words in the file
#Take each possible word of the user_text and check if is in the list of english_words
#Return a string with the words in the user_text that are in english

def Detect_Number_Of_Words_In_English(user_text):
    file_path = "english_dictionary.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    lenght_of_user_text=len(user_text)
    list_of_user_words_in_English=[]
    i = 0
    while i <= lenght_of_user_text - 4: 
        final_character = 4
        while final_character <= 20 and (final_character + i) <= lenght_of_user_text:
            word = user_text[i:i + final_character]

            if word in words:
                list_of_user_words_in_English.append(word)
                i += final_character   
                break

            final_character += 1
        else:
            i += 1     
    return "".join(list_of_user_words_in_English)

