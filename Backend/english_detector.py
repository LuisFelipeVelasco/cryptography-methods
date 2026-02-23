
#Read the english_dictionary.txt and make a list of all the words in the file
#Take each possible word of the user_text and check if is in the list of english_words
#Return a string with the words in the user_text that are in english
import os 

def Detect_Number_Of_Words_In_English(user_text):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "english_dictionary.txt")   
    with open(file_path, "r", encoding="utf-8") as f:
        dictionary = f.read()
    dictionary=dictionary.split()
    lenght_of_user_text=len(user_text)
    list_of_user_words_in_English=[]
    starting_position_of_word_to_check = 0
    starting_position_of_last_word_to_check=lenght_of_user_text-4
    maximum_number_of_characters_in_a_word=20
    while starting_position_of_word_to_check <= starting_position_of_last_word_to_check: 
        quantity_of_characters_of_word_to_check = 4
        while quantity_of_characters_of_word_to_check <= maximum_number_of_characters_in_a_word and (quantity_of_characters_of_word_to_check + starting_position_of_word_to_check) <= lenght_of_user_text:
            word = user_text[starting_position_of_word_to_check:starting_position_of_word_to_check + quantity_of_characters_of_word_to_check]
            print(word)
            if word in dictionary:
                list_of_user_words_in_English.append(word)
                starting_position_of_word_to_check += quantity_of_characters_of_word_to_check
                break

            quantity_of_characters_of_word_to_check += 1
        else:
            starting_position_of_word_to_check += 1     
    return "".join(list_of_user_words_in_English)

