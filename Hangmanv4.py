
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
        else:
            allGuess += guess
            break
    print("All Guesses: ", allGuess)
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

    print(underscoresFormatted)

def gameLogic(word):
    allGuess = ''
    incorrect = ''
    guess = ''
    while True:
        visuals(allGuess, word)
        guess = input("Guess a Letter: ").lower()
        if validateGuess(guess, allGuess, word):
            print("Correct")
            allGuess += guess
        else:
            incorrect += guess
            print("Incorrect. Incorrest Guesses:", incorrect)

gameLogic(getWord())
