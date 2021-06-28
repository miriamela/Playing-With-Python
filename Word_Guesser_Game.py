import random


LEXICON_FILE = "TestLexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def main():
    guesses = INITIAL_GUESSES
    intro()
    word, displayed_word = get_word()
    play_game(word, displayed_word, guesses)


def intro():
    print("Welcome to Guess the Word Game!")
    print("Are you ready?!")


def get_word():
    all_words = []
    with open(LEXICON_FILE) as f:
        for line in f:
            line = line.rstrip()
            all_words.append(line)
    number = random.randint(0, len(all_words)-1)
    displayed_word = displaying_word(all_words[number])
    return all_words[number], displayed_word


def displaying_word(word):
    word = list(word)
    display = []
    for i in range(len(word)):
        display.append("-")
    displayed_word = "".join(display)
    return displayed_word


def play_game(word, displayed_word, guesses):  # play
    while guesses > 0 and displayed_word != word:
        print("The world now looks like this: " + str(displayed_word))
        print("You have " + str(guesses) + " guesses left")
        letter = input("Type a single letter here, then press enter: ")
        displayed_word, guesses = check_guess(  # check the guess and change the hyphen's word accordingly
            letter, displayed_word, word, guesses)
    if guesses == 0:
        print("Sorry, you lost. The secret word was: " + word)


def check_guess(letter, displayed_word, word, guesses):
    letter = letter.upper()
    if letter in word:
        displayed_word = modifying_displayed_word(letter, word, displayed_word)
        print("That guess is correct.")
        if displayed_word == word:
            print("Congratulations, the word is: " + word)
        return displayed_word, guesses
    else:
        guesses = guesses - 1
        print("There are no " + letter + "'s in the word")
        return displayed_word, guesses


def modifying_displayed_word(letter, word, displayed_word):
    displayed_word = list(displayed_word)
    for i in range(len(word)):
        if word[i] == letter:
            displayed_word[i] = letter
    displayed_word = "".join(displayed_word)
    return displayed_word


if __name__ == "__main__":
    main()
