# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:35:50 2020

@author: Linh Tran
"""

import random

# Hangman figures
hanger = ['''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''', '''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']

# this getFood() method will generate a random secret word for Food Topic
def getFood():  
    food = 'molasses prosciutto cantaloupes hazelnuts apple ginger cream watermelons flour snapper chives coconuts potatoes raisins celery'.split()
    foodIndex = random.randint(0, len(food) - 1) # get the index of a list by randomizing the position between 0 to the length of a list
    return food[foodIndex]

# this getAnimal() method will generate a random secret word for Animal Topic
def getAnimal():
    animal = 'kangaroo steer elk deer rat buffalo orangutan seal alligator crab alpaca octopus reindeer crocodile frog woodchuck'.split()
    animalIndex = random.randint(0, len(animal) - 1)
    return animal[animalIndex]

# this getSport() method will generate a random secret word for Sport Topic
def getSport():
    sport = 'soccer snowboarding skateboarding weightlifting wrestling basketball lacrosse tennis football volleyball racing bobsleigh surfing'.split()
    sportIndex = random.randint(0, len(sport) - 1)
    return sport[sportIndex]

def chooseTopic():
   answer = '' 
   # Keep prompting a user for input if the input is not a letter or the input is not a, b, or c
   while not answer.isalpha() or not (answer == 'a' or answer == 'b' or answer == 'c') :
        print("Choose your topic to play: ")
        print("a. Food")
        print("b. Sport")
        print("c. Animal")
        answer = input("Your choice: ").lower()
        # If answer is a letter and it is a, b, or c. Call the method corresponding with a letter.
        #   if answer is a, then call getFood() to get word
        #   if answer is b, then call getSport() to get word
        #   if answer is c, then call getAnimal() to get word
        # Else: print a message of not being appropriate. Enter a loop again for prompting a user for input
        if len(answer) == 1 and (answer == 'a' or answer == 'b' or answer == 'c') :
            if answer == 'a':
                word = getFood()
            if answer == 'b':
                word = getSport()
            if answer == 'c':
                word = getAnimal()
        else:
            print("Your answer is not appropriate. Please choose again:")    
              
   return word         

def displayboard(secret_word):
    blanks_secret = '☆' * len(secret_word)
    print(blanks_secret)
    print("The word you have to guess has " + str(len(blanks_secret)) + " letters.")

def play_game(name):
    playAgain = 'yes' # initialize playAgain to enter a loop
    while playAgain == "yes":  # Will get a value playAgain at the end of a loop by calling play_again(). If playAgain is "yes", re-enter a loop. If "no", exit a loop
        tries = 6   # initialzie the tries back to 6 when start a new game
        incorrect = 0
        correct_letters = ''
        guessedLetters = ''
        secret_word = chooseTopic() # ask for choosing topic and get a secret word
        blanks = '☆' * len(secret_word) # create empty strings with * with the length of a secret word
        displayboard(secret_word)
        while tries > 0:    # keep playing as long as the tries is greater than 0. If it is 0, exit a loop, display "YOU LOST" message
            print(f'You have {tries} tries left!')
            letter_choice = input('Please Enter a Letter: ').lower() # prompt user for guessing letter
            # If the letter_choice is a letter then execute the following codes
            # Else exit the if statement, re-enter the loop for prompting the letter_choice again. Tries will not be decreased here.
            if letter_choice.isalpha():
                 while len(letter_choice) != 1: # If the letter_choice contains more than 2 letters, ask for input again until user type 1 letter, it will exit the loop
                     print("\nIt has to be 1 letter") 
                     letter_choice = input('Please Enter a Letter Again: ').lower()
                     
                # If the input letter is NOT in guessedLetters
                # ELSE print "This letter has been chosen", exit the if-else statement, re-enter for loop again for prompting user for letter_choice. TRIES won't be decreased here
                 if not letter_choice in guessedLetters:
                    if letter_choice in secret_word : # check if a letter_choice exists in a secret word
                        print('\nGREAT! You guessed a RIGHT letter!')
                        correct_letters = correct_letters + letter_choice # add a letter_choice to correct_letters
                        guessedLetters += letter_choice # add a letter_choice to the guessedLetters to check the duplicated input letter_choice
                        for i in range(len(secret_word)):  # Replace blanks with correctly guessed letters.
                            if secret_word[i] in correct_letters: # check if a letter in secret word appears in the correct_Letters
                                 blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
                        print(blanks)   # print the current word user has guessed so far
                    else:
                            print('\nOPPS! You guessed the WRONG letter. Please try again!')
                            guessedLetters += letter_choice  # store a letter to guessedLetters to check the duplicated input
                            incorrect = incorrect + 1
                            draw_hangman(incorrect)
                            tries = tries - 1 # GUESS WRONG, minus the tries
                 else :
                    if (letter_choice in guessedLetters): # check if the input has typed before. If not, re-enter the loop. If yes, print out the message
                        blanks = '*' * len(secret_word)
                        print('\nYou Have Chosen This Letter. Try Again!')   
                        
            else: 
                   print ('\nYou Did Not Enter a Letter! Please Try Again.')
                    # check if word is completed, or not a letter
                    
            if secret_word == blanks : # if the blanks is revealed, print "WON"
                print('\nWINNER!!! GREAT JOB!!!')
                print(hanger[6])
                print('The secret word is: ', secret_word)
                break    

        if (tries == 0):         
            print('\nSORRY! You have exausted all the possible trials!')
            print('Here is the word: ', secret_word)
            
        playAgain = play_again()
    end_game(name)

def draw_hangman (incorrect):
    # Print out the hangman on the console.
    if incorrect == 1:
        print(hanger[0])
    elif incorrect == 2 :
        print(hanger[1])
    elif incorrect == 3:
            print(hanger[2])
    elif incorrect == 4:
        print(hanger[3])
    elif incorrect == 5:
        print(hanger[4])
    elif incorrect == 6:
        print(hanger[5])
    else:
        print("-------")

def rule_game(name):
    print ( f"\n{name}, you must enter a letter at a time in order to play!")
    print("\nYou are allowed to try 6 times!\n")

def play_again():
    answer = ''
    while not (answer == "yes" or answer == "no"):
        answer = input('Would you like to play again? yes/no: ').lower()
    return answer

def end_game(name):
   print('\nThis is the end.')
   print(f'\nThank you for playing with us, {name}!')
   print('\nIs playing Hangman offensive? Do you think there is an other altenative? Let us know in your feedback.')

def main():
    name = input('Hello! Welcome to HangMan game. Please enter your name: ')
    rule_game(name)
    play_game(name)

main()

# DO NOT DECREMENTS THE TRIES WHEN:
# - The input is not appropriate (2 more letters or not a alpha letter )
# - The input has already typed (The correct letter or the wrong letter )