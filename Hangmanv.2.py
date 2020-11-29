import random 
import time

def getWord():
    wordsArray = open("words.txt").read().splitlines()
    word = random.choice(wordsArray)
    return "aeiou"

def visuals(word, currGuess, allGuess, life, initial):
    
    underscores = [' _ '] * len(word)
    underscoresFormatted = ''
    isCorrect = False

    #Check if Guess is in Word
    for index, character in enumerate(word):
        for guess in allGuess:
            if guess == word[index]:
                underscores[index] = guess
                isCorrect = True
    
    #Print Output
    if initial:

        print(initial)
        initial = False
        print(initial)
    elif isCorrect:
        print("Correct Guess. Life Remaining:", life, 
        "Incorrect Guesses:", allGuess)
    else:
        print("Incorrect Guess. Life Remaining:", life, "Incorrect Guesses:", allGuess)
    
    #Format Underscores
    for underscore in underscores:
        underscoresFormatted += underscore
    return underscoresFormatted

#visuals(getWord(), 'b', 'q', 8)

def game(word):
    win = False
    initial = True
    guess =''
    allGuess = ''
    correctGuess = ''
    incorrectGuess = ''
    life = 8
    print("Welcome to Hangman!")
    player1 = input("Enter your name to begin: ")
    print("Hello", player1, "\nLoading...")
    print(visuals(word, guess, allGuess, life, initial))
    while not win:
        guess = input("Guess a Letter: ")
        valid = False
        while not valid:
            if len(guess) != 1:
            	print("Invalid Input.")
            	guess = input("Guess a Letter: ")
            else:
           		allGuess += guess
           		print("Guesses so far:", allGuess)
           		valid = True
           		print(visuals(word, guess, allGuess, life, initial))

game(getWord())







