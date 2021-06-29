import random
print("Welcome to Hangman game!")

print("Type 'exit' to end the game, or press Enter to contine.")

fin = open("./words.txt")
words = fin.read().split()

word = random.choice(words)
length = len(word)

print(f'Guess the word with {len(word)} letters')

letters = []
for i in range(length):
    letters.append("_")

print(" ".join(letters))

while True:


    guess = input("\nGuess a letter: ")

    if guess in word:
        for i in range(length):
            if guess == word[i]:
                letters[i] = guess

        print(" ".join(letters))

    else:
        print("""
        --------
        |      |
        |      
        |
        |
        |
       ---
        """)
    print(" ".join(letters))



