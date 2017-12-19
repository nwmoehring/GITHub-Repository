'''
Write a guessing game where the user has to guess a secret number
After every guess the program tells the user if their number was too large or too small
At the end the number of tries needed should be printed
Guesses of the same number should count as only one guess
'''

import random
#RAND NUMBER GENERATOR LIBRARY & THE random() FUNCT IS CALLED FROM LIBRARY random WITH A .

mystery_number = int(5 * random.random())
#random PRODUCES FLOATING POINT, MULTIPLY BY UPPER BOUND & CONVERT TO INTEGER

guess = int(input("Guess a number!"))
#SPECIFY THE INPUT AS AN INTEGER OR IT WILL BE A STRING

guess_counter = [guess]
#CREATING ARRAY FOR COUNTING NUMBER OF TRIES AND POPULATING WITH FIRST GUESS

while mystery_number != guess:
#IF THE GUESS IS NOT CORRECT THE if STATEMENT BELOW WILL TEST SEE NUMBER IS TOO SMALL

    if mystery_number > guess:
        print("Guess was too small.")
        guess = int(input("Guess a another number!"))
    else:
        #CODE WORKS WITH IF AND ANOTHER TEST, ELSE USED TO SKIP CHEKING THE NUMBER AGAIN
        print("Guess was too big.")
        guess = int(input("Guess a another number!"))

    if not guess in guess_counter:
    #IF CURRENT VALUE OF GUESS IS NOT IN THE ARRAY IT WILL RUN THE CODE BELOW
        guess_counter.append(guess)
        #POPULATES ARRAY WITH CURRENT VALUE OF guess AFTER EVERY ATTEMPT

print("Congratulations, it only took you "+str(len(guess_counter))+" attempts.")
#STRING OUTPUT BROKEN UP BY THE LENGTH OF THE guess_counter ARRAY NEEDS CONCATONATORS +
#DONT NEED TO TEST IF guess IS CORRECT B/C IT ALREADY BROKE OUT OF THE while LOOP
    #ALSO CANT TEST IF guess IS CORRECT AT START B/C IT ONLY WORKS ON FIRST TRY