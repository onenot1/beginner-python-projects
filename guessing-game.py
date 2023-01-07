
import random
import nltk.corpus

nltk.download('wordnet')
all_words = nltk.corpus.treebank.words()


def start_game():
    random_word_index = random.randint(0, len(all_words))
    secret_word = all_words[random_word_index]

    print("admin access, secret word is: " + secret_word)

    guess = ""
    while guess != str.lower(secret_word):
        guess_input = input("Your word is: " + str(len(secret_word)) + " characters long.\nGuess the word:")
        guess = guess_input
        if str.lower(guess) == str.lower(secret_word):
            return
        elif str.lower(guess) == str.lower(secret_word[0:len(guess)]):
            print("\"" + guess_input + "\" was close. Try again.\n\n")
        elif str.lower(guess) != str.lower(secret_word):
            print("\"" + guess_input + "\" was wrong. Please try again.\n\n")
    print("Good job! The word was: " + secret_word + "\n\n")


while True:
    start_game()

