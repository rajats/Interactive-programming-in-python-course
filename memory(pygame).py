#credits introduction to interactive programming in python, Kevin Byiers
#press r to restart
#you need to have pygame module installed
# import modules
import os
import pygame

# pygame specific locals/constants
from pygame.locals import *

# some resource related warnings
# -- comment out for compatibility between Python versions
#if not pygame.font: print('Warning, fonts disabled')
#if not pygame.mixer: print('Warning, sound disabled')

# initializations
pygame.init()

# a bit similar to CodeSkulptor frame creation -- we'll call the window the canvas
canvas = pygame.display.set_mode((900, 100))
pygame.display.set_caption("Memory")


# need to create fonts and colour objects in PyGame
fontObj2 = pygame.font.Font(pygame.font.match_font('timesnewroman'), 18)
fontObj3 = pygame.font.Font(pygame.font.match_font('timesnewroman'), 50)

gold_color = pygame.Color(255, 215, 0)
white_color = pygame.Color(255, 255, 255)
green_color = pygame.Color(0, 128, 0)
red_color = pygame.Color(255, 0, 0)
# ------------------------Begin Your CodeSkulptor Port-------------------------


import random

# new for this port -- no label in PyGame, so use global and draw text
score = "Moves = 0" 
height=100
width=800
deck1=[]
deck2=[]
deck_of_cards=[]
exposed=[]
state=0
turns=0
index1=-1
index2=-1

# helper function to initialize globals
def init():
    global deck1, deck2, deck_of_cards,exposed,turns,state
    state=0
    turns=0
    deck1=range(0,8)
    deck2=range(0,8)
    deck_of_cards=deck1 + deck2
    exposed=[False] * 16
    #making all values in list as false
    random.shuffle(deck_of_cards)
    score = "Moves = " + str(turns)
  
# define event handlers
def mc_handler(pos):
    # add game state logic here
    global state, turns, index1, index2, score
    clicked=list(pos)
    #integer division dividing by 50 since each card has width of 50
    # we had to simulate control area, so we need to offset
    # card calculation by 2 and ignore clicks in control area.
    index = clicked[0] // 50 - 2
    if not exposed[index]:
        if state == 0:
            state = 1
            index1 = index
            exposed[index1]=True
        
        elif state == 1:
            state = 2
            index2 = index 
            exposed[index2] = True
            turns += 1
            score = "Moves = " + str(turns) 
        else:
            state = 1
            if(deck_of_cards[index1] != deck_of_cards[index2]):
                #if both cards are not paired flipping them back
                #so that they are hidden
                exposed[index1]=False
                exposed[index2]=False
            index1 = index
            exposed[index1]=True          


def draw_handler(canvas):

    # clear canvas -- fill canvas with uniform colour, then draw everything below.
    # this removes everything previously drawn and refreshes 
    canvas.fill((0, 0, 0))
    incr=100
    for number in range(0,16):
        pygame.draw.polygon(canvas, green_color, [[incr,0],[incr+50,0],[incr+50,100],[incr,100]], 5)
        if(exposed[number]):
            pygame.draw.polygon(canvas, red_color, [[incr,0],[incr+50,0],[incr+50,100],[incr,100]], 0)
            #canvas.draw_text(str(deck_of_cards[number]),[incr, 65],50,"White")
            text_label = fontObj3.render(str(deck_of_cards[number]), True, white_color)
            canvas.blit(text_label, (incr, 25))
        incr += 50

    # add in the text for our simulated control area -- score and keymap
    text_score = fontObj2.render(score, True, white_color)
    text_key = fontObj2.render("R = Restart", True, white_color)
    canvas.blit(text_score, (8, 60))
    canvas.blit(text_key, (8, 20))
    
    # update the display
    pygame.display.update()

# keydown handler -- use a keypress instead of button
def kd_handler(key):
    if pygame.K_r == key:
        init()

# start first game on run
init()

# call this function to start everything
# could be thought of as the implemntation of the CodeSkulptor frame .start() method.
def main():
    # initialize loop until quit variable
    running = True
    
    # create our FPS timer clock
    clock = pygame.time.Clock()    

#---------------------------Frame is now Running-----------------------------------------
    
    # doing the infinte loop until quit -- the game is running
    while running:
        
        # event queue iteration
        for event in pygame.event.get():
            
            # window GUI ('x' the window)
            if event.type == pygame.QUIT:
                running = False

            # input - key and mouse event handlers
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                # just respond to left mouse clicks
                if pygame.mouse.get_pressed()[0]:
                    mc_handler(pygame.mouse.get_pos())
                    
            elif event.type == pygame.KEYDOWN:
                kd_handler(event.key)

         
        # the call to the draw handler
        draw_handler(canvas)
        
        # FPS limit to 60 -- essentially, setting the draw handler timing
        # it micro pauses so while loop only runs 60 times a second max.
        clock.tick(60)
        
#-----------------------------Frame Stops------------------------------------------

    # quit game -- we're now allowed to hit the quit call
    pygame.quit ()

# this calls the 'main' function when this script is executed
# could be thought of as a call to frame.start() of sorts
if __name__ == '__main__': main() 
