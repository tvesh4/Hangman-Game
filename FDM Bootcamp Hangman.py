import random

with open('words.txt', 'w') as file:
    file.write("apple\nbanana\ncherry\ndragonfruit\nelderberry\n")

def getRandomWord():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    random_word = random.choice(words)
    return random_word

def playHangman():
    random_word = getRandomWord()
    word = list(random_word)
    length = len(word)
    board = ['-'] * length
    guesses = 0
    print("Word:", word)
    print("Board:", ''.join(board))

    while '-' in board:
        letter = input("Enter a letter: ")
        found = False

        for index, char in enumerate(word):
            if char == letter:
                board[index] = char
                found = True

        print("Board:", ''.join(board))
        guesses += 1

    print("Congratulations! You revealed the word in", guesses, "guesses.")

playHangman()



