import random
import time

def getWord():
    wordsArray = open("words.txt").read().splitlines()
    word = random.choice(wordsArray)
    return "aeiou"


def visuals(word, guess, allGuess, life):
    initial = 0
    underscores = [' _ '] * len(word)
    underscoresFormatted = ''
    isCorrect = 0
    for index, character in enumerate(word):
        for guess in allGuess:
            if guess == word[index]:
                underscores[index] = guess
                isCorrect += 1
    if isCorrect > 0:
        print("Correct Guess. Life Remaining:", life)
    elif initial == 0:
        pass
    elif underscoresFormatted == word:
        print("You won!")
    else:
        print("Inc Test")
    for underscore in underscores:
        underscoresFormatted += underscore
    initial += 1
    return underscoresFormatted

    
def game(word):
    Play = True
    print("Welcome to Hangman!")
    player1 = input("Enter your name to begin: ")
    print("Hello", player1, "\nLoading...")
    time.sleep(0)
    
    guess = ''
    guesses = ''
    life = 8
    
    while life > 0:
        fail = 0
        gameCount = 0
        gameCount += 1
        incorrectGuesses = ''
        allGuess = ''
        print("\n\nGame", gameCount)
        print("Life Remaining: ", life)
        print("The word has", len(word), "letters.")
        print(visuals(word, guess, allGuess, life))
        guess = input("Guess a Letter: ")
        
        allGuess = ''
        allGuess += guess
        #for letter in guess:
        while life > 0:
            #Correct Guess 
            if guess in word:
                #print("Correct Guess. Life Remaining:", life, guess)
                print(visuals(word, guess, allGuess, life))
                guess = input("Guess a Letter: ")
                while True:
                    if len(guess) != 1:
                        print("Invalid Input.")
                        guess = input("Guess a Letter: ")
                    else:
                        break
                allGuess += guess
                
            #Incorrect Guess
            else:
                life -= 1 
                incorrectGuesses += guess + ' '
                allGuess += guess
                print("Incorrect Guess. Life Remaining: ", life)
                print("Incorrect Guesses: ", incorrectGuesses)
                print(visuals(word, guess, allGuess, life))
                guess = input("Guess a Letter: ")
                while True:
                    if len(guess) != 1:
                        print("Invalid Input.")
                        guess = input("Guess a Letter: ")
                    else:
                        break


        if fail == 0:
            print("You Win") 
            print("The word is: ", word) 
            break
    
        guess = input("Guess a Letter: ")
        

        guesses += guess 
        
        if guess not in word:
            life -= 1

            print("Wrong")
            
            # this will print the number of
            # life left for the user
            print("You have", + life, 'more guesses')
            
            
            if life == 0:
                print("You Lose")

game(getWord())
