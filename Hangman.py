import random

Play = True
while Play:

    print("Welcome to Hangman!")
    name = input("Enter your name: ")
    print("Hello,", name, ". Good Luck!")
    userInput = input("Press Enter to Start")
    
    word = ["these", "are", "random", "words", "jazz"]
    currentWord = random.choice(word)

    currentGame = True
    lettersGuessed = ""
    while currentGame:
        letter = input("Guess a Letter: ")
        if input.lower() in currentWord: 
            print("Correct Guess!")
            #print(lettersGuessed+=letter)
            #if lettersGuessed = currentWord:
            currentGame = False