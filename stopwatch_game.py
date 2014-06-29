# you need to have tkinter package to run this code
# template for "Stopwatch: The Game"
import simpleguitk as simplegui

# define global variables
tenth_sec=0
e=0
success_counter=0
# maintains count of number of success
total_attempts=0
flag=0
stop_count=0
started=False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(tenth_sec):
    global e
    e = tenth_sec
    #value of tenth_sec stored in e so that it can be used
    #in function game()
    if (tenth_sec < 10):
        return "0" + ":" + "00" + "." + str(tenth_sec)
    elif (tenth_sec>=10):
        d=tenth_sec % 10
        c=tenth_sec // 10
        if(c <= 59):
            if(c < 10):
                # c is single digit
                return "0" + ":" + "0" + str(c) + "." + str(d)
            else: 
                # c is double digit
                return "0" + ":" + str(c) + "." + str(d)
        else:
            a=c // 60
            c=c % 60
            if(c < 10):
                return str(a) + ":" + "0" + str(c) + "." + str(d)
            else:
                return str(a) + ":" + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stop_count,started
    stop_count=0
    started=True
    timer.start()
    

def stop():
    global flag,started
    global stop_count
    timer.stop()
    flag=1
    stop_count += 1
    #keeping count of number of times stop button is clicked

def game():
    global success_counter
    global total_attempts
    global flag
    global e,started
    global stop_count
    e=e%10
    
    if (flag == 1 and stop_count == 1 and started==True):
        #if more than once stop is clicked then this
        #condition fails as stop_count exceeds 1
        if(e==0):
            success_counter += 1
        total_attempts += 1
    flag=0
    return str(success_counter) + "/" + str(total_attempts)
        
    
def reset():
    global tenth_sec
    global success_counter
    global total_attempts
    global stop_count
    global started
    started=False
    tenth_sec=0
    timer.stop()
    stop_count=0
    success_counter=0
    total_attempts=0


# define event handler for timer with 0.1 sec interval
def increment():
    global tenth_sec
    tenth_sec += 1


# define draw handler
def draw(canvas):
    global tenth_sec
    global flag
    canvas.draw_text( format(tenth_sec), [100,100], 24, "White")
    canvas.draw_text( game(), [150,20], 24, "White")
    
# create frame
f=simplegui.create_frame("",200,200)


# register event handlers
timer=simplegui.create_timer(100,increment)
f.add_button("Start",start,100)
f.add_button("Stop",stop,100)
f.add_button("Reset",reset,100)
f.set_draw_handler(draw)


# start frame
f.start()



# Please remember to review the grading rubric
