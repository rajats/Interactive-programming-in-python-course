#credits introduction to interactive programming in python, Kevin Byiers
#press r to restart
#you need to have pygame module installed
#import modules
#controlls: 
#Right paddle:UP LEFT DOWN RIGHT
#Left paddle:W A S D
import pygame

# pygame specific locals/constants
from pygame.locals import *

# some resource related warnings
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# initializations
pygame.init()

# a bit similar to CodeSkulptor frame creation -- we'll call the window the canvas
canvas = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pong")

# need to create fonts and colour objects in PyGame
fontObj3 = pygame.font.Font(pygame.font.match_font('timesnewroman'), 32)

gold_color = pygame.Color(255, 215, 0)
white_color = pygame.Color(255, 255, 255)
red_color = pygame.Color(255, 0, 0)
blue_color = pygame.Color(0, 0, 255)

# ------------------------Begin Your CodeSkulptor Port-------------------------

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
# not needed HALF_PAD_WIDTH = PAD_WIDTH / 2
# not needed HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel=[0,0]
paddle1_pos=160  #height/2 - pad height/2
paddle2_pos=160
paddle1_vel=0
paddle2_vel=0
score1=0
score2=0

# paddle acceleration constant -- cover the open court in one second (5.33 pixels per draw)
PADDLE_ACCELERATION = 6

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH / 2 , HEIGHT / 2]
    if(right):
        ball_vel[0]=(random.randrange(120, 240))/60
        ball_vel[1]=-(random.randrange(60, 180))/60
        #negative for ball movement to be upward
    else:
        ball_vel[0]=-(random.randrange(120, 240))/60
        ball_vel[1]=-(random.randrange(60, 180))/60
	      

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel # these are numbers
    global score1, score2  # these are ints
    score1=0
    score2=0 
    paddle1_pos=160
    paddle2_pos=160
    paddle1_vel=0
    paddle2_vel=0
    ball_vel=[0,0]
    ball_init(RIGHT)
	


def draw_handler(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    # clear canvas -- fill canvas with uniform colour, then draw everything below.
    # this removes everything previously drawn and refreshes 
    canvas.fill((0, 0, 0))
    
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos + paddle1_vel >=0 and paddle1_pos + PAD_HEIGHT + paddle1_vel <= HEIGHT):
        paddle1_pos += paddle1_vel
    if(paddle2_pos + paddle2_vel >=0 and paddle2_pos + PAD_HEIGHT + paddle2_vel <= HEIGHT):
        paddle2_pos += paddle2_vel     
    
    # draw mid line and gutters
    #canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") is replaced by
    pygame.draw.line(canvas, white_color, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(canvas, white_color, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, white_color, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)

    # draw paddles            
    pygame.draw.polygon(canvas, red_color, [[0, paddle1_pos],[PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) + PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]], 0) 
    pygame.draw.polygon(canvas, red_color, [[WIDTH, paddle2_pos],[WIDTH - PAD_WIDTH, paddle2_pos],[WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]], 0)    
	

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # top/bottom boundary
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[1] >= HEIGHT -1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]

    # gutter right  
    if(ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) ):
        #pad width is added so that ball spawns from gutter or reflects from paddle
        if(ball_pos[1]>=paddle1_pos and ball_pos[1]<=PAD_HEIGHT + paddle1_pos):
            #condition for reflection from paddle, draw figure to undersatnd it
            ball_vel[0] = -(ball_vel[0] + ball_vel[0]*0.1)
            ball_vel[1] = ball_vel[1] + ball_vel[1]*0.1
            #increasing velocity by 10 perecent
        else:
            ball_init(RIGHT);
            score2 +=1
	
	# gutter left    
    elif(ball_pos[0] >= WIDTH - PAD_WIDTH -1 -BALL_RADIUS):
        if(ball_pos[1]>=paddle2_pos and ball_pos[1]<=PAD_HEIGHT + paddle2_pos):
            ball_vel[0] = -(ball_vel[0] + ball_vel[0]*0.1)
            ball_vel[1] = ball_vel[1] + ball_vel[1]*0.1
        else:
            ball_init(LEFT);
            score1 +=1
    

            
    # draw ball and scores
    #canvas.draw_text(str(score1), (125, 60), 35, "White")
    canvas.blit(fontObj3.render(str(score1), True, white_color), (125, 25))    
    #canvas.draw_text(str(score2), (450, 60), 35, "White")
    canvas.blit(fontObj3.render(str(score2), True, white_color), (450, 25))      

    #canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    pygame.draw.circle(canvas, blue_color, [int(ball_pos[0]), int(ball_pos[1])], BALL_RADIUS)
    
    # update the display
    pygame.display.update()


def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #if simplegui.KEY_MAP["w"] == key:
    if pygame.K_w == key:        
        paddle1_vel -= PADDLE_ACCELERATION
    #elif simplegui.KEY_MAP["s"] == key:
    elif pygame.K_s == key:        
        paddle1_vel += PADDLE_ACCELERATION
    #elif simplegui.KEY_MAP["up"] == key:
    elif pygame.K_UP == key:        
        paddle2_vel -= PADDLE_ACCELERATION
    #elif simplegui.KEY_MAP["down"] == key:
    elif pygame.K_DOWN == key:        
        paddle2_vel += PADDLE_ACCELERATION
    # added in to restart -- instead of a button    
    elif pygame.K_r == key:
        init()
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    #if simplegui.KEY_MAP["w"] == key:
    if pygame.K_w == key:    
        paddle1_vel += PADDLE_ACCELERATION
    #elif simplegui.KEY_MAP["s"] == key:
    elif pygame.K_s == key:         
        paddle1_vel -= PADDLE_ACCELERATION
    #elif simplegui.KEY_MAP["up"] == key:
    elif pygame.K_UP == key:         
        paddle2_vel += PADDLE_ACCELERATION
    #elif simplegui.KEY_MAP["down"] == key:
    elif pygame.K_DOWN == key:         
        paddle2_vel -= PADDLE_ACCELERATION 

init()

# ------------------------CodeSkulptor Port Ends-------------------------

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
                pass
                # just respond to left mouse clicks
                #if pygame.mouse.get_pressed()[0]:
                    #mc_handler(pygame.mouse.get_pos())
                
            elif event.type == pygame.KEYUP:
                keyup(event.key)

            elif event.type == pygame.KEYDOWN:
                keydown(event.key)
            
                
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
