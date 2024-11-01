import os
import pandas

def code_words():
    """ It takes a word as user input and displays phonetic code words
    for the word. Phonetic code words are generated based on the words
    listed in the nato_phonetic_alphabet CSV file. """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "nato_phonetic_alphabet.csv")
    data = pandas.read_csv(filepath)
    phonetic_words_dict = {row.letter:row.code  for (_, row) in data.iterrows()}

    user_input = input("Entera word?: ").upper()
    phonetic_code_words = [phonetic_words_dict[letter] for letter in user_input]
    print(f"Phonetic code words:\n{phonetic_code_words}")


if __name__ == "__main__":
    code_words()
