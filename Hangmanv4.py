import random 
import time

def getWord():
    wordsArray = open("words.txt").read().splitlines()
    word = random.choice(wordsArray)
    return word

def validateGuess(guess, allGuess):
    while True:
        if guess in allGuess:
            print("You already guessed this letter. Guessed Letters:", allGuess)
            return False
        elif len(guess) != 1:
            print("Invalid input.")
            return False
        elif guess.isdigit():
            print("Invalid input.")
            return False
        else:
            return True

def checkGuess (guess, word):
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

def difficulty():
    print("Easy - E\nMedium - M\nHard - H\nImpossible - I")
    difficulty = input("Choose difficulty: ").lower()
    while True:
        if difficulty == 'e':
            return 15
        elif difficulty == 'm':
            return 12
        elif difficulty == 'h':
            return 6
        elif difficulty == 'i':
            return 3
        else:
            print("Invalid Input.")
            difficulty = input("Choose difficulty: ").lower()

def gameLogic(word):
    allGuess = ''
    incorrect = ''
    guess = ''
    life = difficulty()
    while life > 0:
        print(visuals(allGuess, word))
        while True:
            guess = input("Guess a Letter: ").lower()

            #Validate Guess
            if validateGuess(guess, allGuess):
                break
        
        #Correct Guess
        if checkGuess(guess, word):
            allGuess += guess
            print("Correct!\nIncorrect Guesses:", incorrect, "Remaining Life:", life)
            if visuals(allGuess, word) == word:
                print("You won!")
                return True

        #Incorrect Guess
        else:
            incorrect += guess
            allGuess += guess
            life -= 1
            print("Incorrect.\nIncorrect Guesses:", incorrect, "Remaining Life:", life)
    print("You lost!")
    print("The word was",word.strip(),".")

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
        print("Game:", count, "Wins:", win, "Losses:", loss)
        if gameLogic(getWord()):
            win += 1
        else:
            loss += 1
        if playAgain(win, loss, player1):
            pass
        else:
            break

def playAgain(win, loss, player1):
    while True:
        userInput = input("Play Again? (Y/N): ").lower()
        if userInput == 'y':
            print("Ok,",player1,". Let's play again!")
            print("Loading...")
            time.sleep(2)
            return True
        elif userInput == 'n':
            print("You won", win, ("time" if win == 1 else "times"), "and lost", loss, ("time." if loss == 1 else "times."),"\nThanks for playing!")
            return False
        else:
            print("Invalid Input.")
            pass

gameMenu()