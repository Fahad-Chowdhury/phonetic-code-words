import os
import pandas


def generate_phonetic(phonetic_words):
    """ It takes a word as user input and displays phonetic code words
    for the word from the 'phonetic_words' dictionary. """
    user_input = input("Entera word?: ").upper()
    try:
        phonetic_code_words = [phonetic_words[letter] for letter in user_input]
    except KeyError:
        print("Sorry! Only enter letters in the alphabet.")
        generate_phonetic(phonetic_words)
    else:
        print(f"Phonetic code words:\n{phonetic_code_words}")


def code_words():
    """ It reads phonetic code words for all the letters from 
    nato_phonetic_alphabet CSV file, and calls generate_phonetic() method to
    take a word as user input and displays phonetic code words for the word. """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "nato_phonetic_alphabet.csv")
    data = pandas.read_csv(filepath)
    phonetic_words_dict = {row.letter:row.code  for (_, row) in data.iterrows()}
    generate_phonetic(phonetic_words_dict)


if __name__ == "__main__":
    code_words()
