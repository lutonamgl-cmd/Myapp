import turtle

# --- 1. Setup and Variables ---
a = 0
b = 0

screen = turtle.Screen()
screen.bgcolor("black")

# FORCE the window to come to the front and listen to inputs
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.attributes('-topmost', 1)
root.attributes('-topmost', 0)

# Turtle for the red button
button_turtle = turtle.Turtle()
button_turtle.speed(0)
button_turtle.hideturtle()

# Turtle for the green spiral art
art_turtle = turtle.Turtle()
art_turtle.speed(0)
art_turtle.pencolor("red")
art_turtle.hideturtle()

# --- 2. Button Click Function ---
def start_spiral_art(x, y):
    global a, b
    
    # We check distance to (0,0) since that's the absolute center of our red button
    # Increased the distance check to 25 pixels so it's much easier to click!
    if art_turtle.distance(x, y) < 25:
        # 1. Make the red circle disappear instantly
        button_turtle.clear()
        
        # 2. Turn off the click listener so you can't double-click it
        screen.onclick(None)
        
        # 3. Start drawing from the exact middle
        art_turtle.penup()
        art_turtle.goto(0, 0) 
        art_turtle.pendown()
        art_turtle.showturtle()
        
        # 4. Your original drawing loop
        while True:
            art_turtle.forward(a)
            art_turtle.right(b)
            a += 3
            b += 1
            if b == 200:
                break
                
        art_turtle.hideturtle()

# --- 3. Draw the Red Circle in the Middle ---
button_turtle.penup()
button_turtle.goto(0, -15) # Moves down so circle centers perfectly at 0,0
button_turtle.pendown()

button_turtle.color("red")
button_turtle.begin_fill()
button_turtle.circle(15)   
button_turtle.end_fill()

# --- 4. Activation ---
# Listen for the click across the screen
screen.onclick(start_spiral_art)

screen.mainloop()
