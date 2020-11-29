import random 
import time

def getWord():
    wordsArray = open("words.txt").read().splitlines()
    word = random.choice(wordsArray)
    return "aeiou"

def visuals(word, currGuess, allGuess, life, initial):
    win = False
    underscores = [' _ '] * len(word)
    underscoresFormatted = ''
    isCorrect = False
    incorrectGuess = ''

    #Check if Guess is in Word
    for index, character in enumerate(word):
        for guess in allGuess:
            if guess == word[index]:
                underscores[index] = guess
                isCorrect = True
    
    #Format Underscores
    for underscore in underscores:
        underscoresFormatted += underscore
    
    #Print Output
    if initial:
        print("Welcome to Hangman!")
        player1 = input("Enter your name to begin: ")
        print("Hello", player1, "\nLoading...")
        time.sleep(3)
        print(underscoresFormatted)
    elif isCorrect:
        print("Correct Guess. Life Remaining:", life, 
        "Incorrect Guesses:", allGuess)
        print(underscoresFormatted)
    else:
        #incorrectGuess += guess
        print("Incorrect Guess. Life Remaining:", life, "Incorrect Guesses:", incorrectGuess)
        print(underscoresFormatted)
    

    if underscoresFormatted == word:
        time.sleep(3)
        print("You won!")
        win = True
    return win 

#visuals(getWord(), 'b', 'q', 8)

def game(word):
    
    initial = True
    guess = ''
    life = 8
    allGuess = ''

    visuals(word, guess, allGuess, life, initial)
    initial = False
    guess = input("Guess a Letter: ").lower()

    #True Until Win
    while True:
        guess = input("Guess a Letter: ").lower()
        #Validate User Input
        valid = False
        while not valid:
            if len(guess) != 1:
                print("Invalid Input.")
                guess = input("Guess a Letter: ").lower()
            else:
                valid = True
                
        visuals(word, guess, allGuess, life, initial)
           	    
                #if visuals(word, guess, allGuess, life, initial):
                #    guess = input("Play again? (Y/N): ").lower()
                    

game(getWord())







