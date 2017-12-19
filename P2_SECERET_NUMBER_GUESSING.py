'''
Write a guessing game where the user has to guess a secret number
After every guess the program tells the user if their number was too large or too smal
At the end the number of tries needed should be printed
Guess of the same number count as only one guess
'''

#
#IMPORTING, GETTING A MYSTERY NUMBER, & INPUT

import random
#RAND NUMB GEN LIBRARY & THE random() FUNCT IS CALLED FROM LIBRARY random WITH A .
mystery_number = int(1000 * random.random())
#random PRODUCES FLOATING POINT, * BY UPPER BOUND & CONVERT TO INTEGER
guess = int(input("Guess a number!"))
#SPECIFY THE INPUT AS AN INTEGER OR IT WILL BE A STRING

#
#COMPAIRING MYSTERY NUMBER TO USER GUESSES

while mystery_number != guess:
#IF THE GUESS IS NOT CORRECT IF STATEMENT BELOW WILL TEST IF NUMBER IS TOO SMALL

    if mystery_number > guess:
        print("Guess was too small.")
        guess = int(input("Guess a another number!"))
    elif mystery_number < guess:
        #CODE WORKS WITH IF, ELIF USED TO SKIP CHEKING THE NUMBER AGAIN
        print("Guess was too big.")
        guess = int(input("Guess a another number!"))

if mystery_number == guess:
    print("You are correct!")
#STATEMENT WONT PRINT UNLESS ITS RIGHT ON FIRST TRY IF THIS IS AT BEGINNING