# template for "Stopwatch: The Game"

import simpleguitk

# define global variables

interval = 100
count = 0
total_stops = 0
succes_stops = 0
stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_sec = (t) % 10
    sec = int(t / 10) % 10
    minutes = int(t / 600) % 600
    ten_min = int(t / 100) % 6
    string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return string
pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global count, stop
    stop = False
    timer.start()
    
def Stop():
    global total_stops, succes_stops, stop
    if stop == False :
        if count % 10 == 0 and count != 0 :
            succes_stops += 1
            total_stops += 1
        elif count != 0 :
            total_stops += 1
    stopped = True
    timer.stop()
    
def Reset():
    global count, succes_stops, total_stops
    count = 0
    stop = True
    total_stops = 0
    succes_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1

# define draw handler
def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (90, 175), 42, "white")
    canvas.draw_text(str(succes_stops) + '/' + str(total_stops), (245,45), 24, "white")
    
# Create a frame 
frame = simpleguitk.create_frame("Stopwatch game", 300, 300)

# Register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simpleguitk.create_timer(interval, tick)

# Start the frame animation
frame.start()
Reset()

# Please remember to review the grading rubric
