# you need to have tkinter package to run this code
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simpleguitk as simplegui


# initialize global variables used in your code
player_guess=0
secret_number=0
max_range=7
#max range for shifting between two ranges
flag=0
#flag for continuing game in the range of previous game


# helper function to start and restart the game
def new_game():
    global secret_number
    if (max_range == 7):
        print " "
        print "New Game. Range is from 0 to 100"
        print "Number of remaining guesses  7"
        secret_number= random.randrange(0,100)
        #print secret_number
    else:
        print " "
        print "New Game. Range is from 0 to 1000"
        print "Number of remaining guesses  10"
        secret_number= random.randrange(0,1000)
        #print secret_number
        
    
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global max_range
    global flag
    max_range=7
    flag=0
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global max_range
    global flag
    max_range=10
    flag=1
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global player_guess
    global secret_number
    global max_range
    global flag
    player_guess=int (guess)
    print " "
    print "Guess was ",player_guess
    
    if (max_range >= 1):
        #decreasing number of guesses left with each guess
        max_range -= 1
        print "Number of remaining guesses ",max_range
        if(max_range == 0):
            if(player_guess == secret_number):
                print "Correct!"
                if(flag == 1):
                    range1000()
                else:
                    range100()
            else:
                print "You ran out of guesses. The number was ",secret_number
                if(flag == 1):
                    range1000()
                else:
                    range100()
        else:
            if (player_guess > secret_number):
                print "Lower"
    
            elif (player_guess < secret_number):
                print "Higher"
    
            elif (player_guess == secret_number):
                print "Correct!"
                if(flag == 1):
                    range1000()
                else:
                    range100()
        
    
 
# create frame
f= simplegui.create_frame("", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 100)
f.add_button("Range is [0,1000)", range1000, 100)
f.add_input("Enter a guess", input_guess,100)



# call new_game and start frame
new_game()
f.start()

# always remember to check your completed program against the grading rubric