import random
import wrong
print("Welcome to Hangman game!")

print("Type 'exit' to end the game, or press Enter to contine.")

fin = open("./words.txt")
words = fin.read().split()
while True:
    word = random.choice(words)
    length = len(word)

    print(f'Guess the word with {len(word)} letters')

    letters = []
    for i in range(length):
        letters.append("_")

    print(" ".join(letters))
    wrong_guesses = 0
    while True:


        guess = input("\nGuess a letter: ")

        if guess in word:
            for i in range(length):
                if guess == word[i]:
                    letters[i] = guess


        if guess not in word:
            print(wrong.a[wrong_guesses])
            wrong_guesses += 1

        print(" ".join(letters))

        if "_" not in letters:
            print("You won")
            break

        if wrong_guesses >= length:
            print("You Lost")
            break


    close_page = input("Write 'exit' if you want to close the game or press 'ENTER' if you want to play again: ")
    if close_page == "exit":
        break
    else:
        pass




