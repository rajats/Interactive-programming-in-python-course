# you need to have tkinter package to run this code
# implementation of card game - Memory

import simpleguitk as simplegui
import random
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
def new_game():
    global deck1, deck2, deck_of_cards,exposed,turns,state
    state=0
    turns=0
    deck1=range(0,8)
    deck2=range(0,8)
    deck_of_cards=deck1 + deck2
    exposed=[False] * 16
    #making all values in list as false
    random.shuffle(deck_of_cards)

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,turns,index1,index2 
    clicked=list(pos)
    #integer division dividing by 50 since each card has width of 50
    index = clicked[0] // 50
    if not exposed[index]:
        if state == 0:
            state = 1
            index1 = index
            exposed[index1]=True
        
        elif state == 1:
            state = 2
            index2 = index 
            exposed[index2]=True
            turns +=1
        else:
            state = 1
            if(deck_of_cards[index1] != deck_of_cards[index2]):
                #if both cards are not paired flipping them back
                #so that they are hidden
                exposed[index1]=False
                exposed[index2]=False
            index1 = index
            exposed[index1]=True
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    incr=0
    for number in range(0,16):
        canvas.draw_polygon([[incr,0],[incr+50,0],[incr+50,100],[incr,100]],2,"white","Green")
        if(exposed[number]):
            canvas.draw_polygon([[incr,0],[incr+50,0],[incr+50,100],[incr,100]],2,"white","Red")
            canvas.draw_text(str(deck_of_cards[number]),[incr, 65],50,"White")
        incr += 50
    label.set_text("Moves = " + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns "+str(turns))
frame.add_label("Click the card to unfold it ")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric