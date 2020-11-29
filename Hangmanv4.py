
import random 
import time

def getWord():
    wordsArray = open("words.txt").read().splitlines()
    word = random.choice(wordsArray)
    return "aeiou"

def validateGuess(guess, allGuess, word):
    while True:
        if len(guess) != 1:
            print("Invalid input.")
            guess = input("Guess a Letter: ").lower()
        elif guess in allGuess:
            print("You already guessed this letter.")
            guess = input("Guess a Letter: ").lower()
        else:
            allGuess += guess
            break
    if guess in word:
        return True
    else:
        return False

def visuals(allGuess, word):
    underscores = [' _ '] * len(word)
    underscoresFormatted = ''

    for index, character in enumerate(word):
        for guess in allGuess:
            if guess == word[index]:
                underscores[index] = guess
    
    for underscore in underscores:
        underscoresFormatted += underscore

    return underscoresFormatted

def gameLogic(word):
    allGuess = ''
    incorrect = ''
    guess = ''
    life = 8
    while life > 0:
        print(visuals(allGuess, word))
        guess = input("Guess a Letter: ").lower()
        if validateGuess(guess, allGuess, word):
            print("Correct. Incorrect Guesses:", incorrect, "Remaining Life:", life)
            allGuess += guess
            if visuals(allGuess, word) == word:
                print("You won!")
                return True
        else:
            incorrect += guess
            life -= 1
            print("Incorrect. Incorrect Guesses:", incorrect, "Remaining Life:", life)
    print("You Lost!")



def gameMenu():
    print("Welcome to Hangman!")
    player1 = input("Enter your name to begin: ")
    print("Hello", player1, "\nLoading...")
    time.sleep(3)
    count = 0
    win = 0
    loss = 0
    while True:
        count += 1
        print("Game", count, "Wins:", win, "Losses:", loss)
        if gameLogic(getWord()):
            win += 1
        else:
            loss += 1
        userInput = input("Play Again? (Y/N): ").lower()
        if userInput == 'y':
            pass
        elif userInput == 'n':
            print("You won", win, ("time" if win == 1 else "times"), "and lost", loss, ("time" if loss == 1 else "times"), "Thanks for playing!")
            break
        else:
            print("Invalid Input.")



gameMenu()
