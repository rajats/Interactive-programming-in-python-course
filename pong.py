# you need to have tkinter package to run this code
# Implementation of classic arcade game Pong
# credits codeclinic, without tip #4 i couldn't have finished this code,thanks for
# time saving tip which helped me when i was stuck on paddles getting locked on top
# and bottom of canvas

import simpleguitk as simplegui
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

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH / 2 , HEIGHT / 2]
    if(direction == RIGHT):
        ball_vel[0]=(random.randrange(120, 240))/60
        ball_vel[1]=-(random.randrange(60, 180))/60
        #negative for ball movement to be upward
    if(direction == LEFT):
        ball_vel[0]=-(random.randrange(120, 240))/60
        ball_vel[1]=-(random.randrange(60, 180))/60


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)

def restart():
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos, score1, score2
    score1=0
    score2=0 
    paddle1_pos=160
    paddle2_pos=160
    paddle1_vel=0
    paddle2_vel=0
    ball_vel=[0,0]
    new_game()
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[1] >= HEIGHT -1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    if(ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) ):
        #pad width is added so that ball spawns from gutter or reflects from paddle
        if(ball_pos[1]>=paddle1_pos and ball_pos[1]<=PAD_HEIGHT + paddle1_pos):
            #condition for reflection from paddle, draw figure to undersatnd it
            ball_vel[0] = -(ball_vel[0] + ball_vel[0]*0.1)
            ball_vel[1] = ball_vel[1] + ball_vel[1]*0.1
            #increasing velocity by 10 perecent
        else:
            spawn_ball(RIGHT);
            score2 +=1
    elif(ball_pos[0] >= WIDTH - PAD_WIDTH -1 -BALL_RADIUS):
        if(ball_pos[1]>=paddle2_pos and ball_pos[1]<=PAD_HEIGHT + paddle2_pos):
            ball_vel[0] = -(ball_vel[0] + ball_vel[0]*0.1)
            ball_vel[1] = ball_vel[1] + ball_vel[1]*0.1
        else:
            spawn_ball(LEFT);
            score1 +=1
        
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Yellow","White")
    
    # update paddle's vertical position, keep paddle on the screen
    #code clinic tip#4
    #intially i haven't added paddle1_vel in if due to which paddle always got stuck on top
    #or bottom
    if(paddle1_pos + paddle1_vel >=0 and paddle1_pos + PAD_HEIGHT + paddle1_vel <= HEIGHT):
        paddle1_pos += paddle1_vel
    if(paddle2_pos + paddle2_vel >=0 and paddle2_pos + PAD_HEIGHT + paddle2_vel <= HEIGHT):
        paddle2_pos += paddle2_vel

    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos],[PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) + PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]],1,"Blue","Blue") 
    canvas.draw_polygon([[WIDTH, paddle2_pos],[WIDTH - PAD_WIDTH, paddle2_pos],[WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]],1,"Blue","Blue")
    
    
    # draw scores
    canvas.draw_text(str(score1),(210,100),60,"Red")
    canvas.draw_text(str(score2),(390,100),60,"Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc=6
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",restart)
frame.add_label("controls: right")
frame.add_label("up left down right")
frame.add_label("controls: left")
frame.add_label("W A S D")

# start frame
new_game()
frame.start()