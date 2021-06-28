def main():
    min = 0
    max = 100
    total_guesses = 1
    print("Think about a number between 1 and 100")
    guess = (min+max)//2
    clue = input("Is your Number "+str(guess)+" ? ")
    while clue != "correct":
        if clue == "lower":
            max = guess
        elif clue == "higher":
            min = guess
        guess = (max+min)//2
        clue = input("Is your Number "+str(guess)+" ? ")
        total_guesses = total_guesses + 1
    print("")
    print("I win! It took me "+str(total_guesses)+" guesses")


if __name__ == '__main__':
    main()
