import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(data.to_dict())

#1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(phonetic_dict)

#. Create a list of the phonetic code words from a word that the user inputs:
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)

word = ""
def generate_phonetic():
    word = input("Entre a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

# word = ""
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(output_list)
#
# generate_phonetic()
#
# if word != word.isalnum():
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#     except:
#         print("Sorry, only letters in the alphabet please.")


