student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("What word would you like transcribed? ").upper()
    try:
        phonetic_list = [dict_alphabet[letter] for letter in user_word]
    except KeyError:
        print("Please enter a letter.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
