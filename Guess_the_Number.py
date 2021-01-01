###Working Code###
import simpleguitk
import random
import math

rem_guess = 0  #Called for Remaining guess
secret_number = 0 #Secret or Computer guess Number
user_num = 0 #Entered User Number
n_rang = 0 #Range of number

def input_guess(guess):
    global rem_guess
    global user_num
    global secret_number
    #print(guess)
    user_num = int(guess)

    rem_guess = rem_guess - 1
    
    print ("Guess Was:",user_num)
    print ("Number of remaining guesses is", rem_guess)
    
    if rem_guess > 0:
        if secret_number > user_num:
            print ("Higher")
        elif secret_number < user_num:
            print ("Lower")
        elif secret_number == user_num:
            print ("Correct")
    else:
        print ("You ran out of guesses. The number was", secret_number)
def range100():
    global rem_guess
    global secret_number
    global n_rang
    n_rang = 100
    new_game()
    rem_guess = 7
    print ("New game. Range is from 0 to",n_rang)
    print ("Number of remaining guesses is",rem_guess)
def range1000():
    global rem_guess
    global secret_number
    global n_rang
    n_rang = 1000
    new_game()
    #secret_number = random.randrange(0, 1000)
    rem_guess = 10
    print ("New game. Range is from 0 to",n_rang)
    print ("Number of remaining guesses is",rem_guess)
def new_game():
    global secret_number
    global user_num
    secret_number = random.randrange(0, n_rang)
    #print (secret_number)
    
frame = simpleguitk.create_frame("Guess The Number",200,200)
frame.add_button('Range is (1 - 100)',range100,200)
frame.add_button('Range is (1-1000)',range1000,200)
frame.add_input('Input guess',input_guess,120)

#new_game()
range100()

frame.start()
