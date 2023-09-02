import turtle
import random
import sys
from tkinter import messagebox

# Variables
p1_score = 0
p2_score = 0
ball_x = 0
ball_y = 0
ball_dx = 0
ball_dy = 0
player_speed = 6.5
is_moving_up_p1 = False
is_moving_down_p1 = False
is_moving_up_p2 = False
is_moving_down_p2 = False
game_start = False

# The player function. This for the pong.
def player(x_pos):
    player = turtle.Turtle()
    player.color("white")
    player.shape("square")
    player.speed(0)
    player.penup()
    player.goto(x_pos,-20)

    # Stretch the square to make it larger
    stretch_wid = 4  # Change this value to adjust the width of the square
    stretch_len = 1  # Change this value to adjust the length of the square
    player.shapesize(stretch_wid, stretch_len)

    return player

# This function makes the player move up.
def move_up_p1():
    global is_moving_up_p1, is_moving_down_p1
    is_moving_up_p1 = True
    is_moving_down_p1 = False

# This function makes the player move down.
def move_down_p1():
    global is_moving_down_p1, is_moving_up_p1
    is_moving_down_p1 = True
    is_moving_up_p1 = False

# This function makes the second player move up.
def move_up_p2():
    global is_moving_up_p2, is_moving_down_p2
    is_moving_up_p2 = True
    is_moving_down_p2 = False

# This function makes the second player move down.
def move_down_p2():
    global is_moving_down_p2, is_moving_up_p2
    is_moving_down_p2 = True
    is_moving_up_p2 = False

def ball():
    global ball_dx, ball_dy
    
    # Ball setup
    ball = turtle.Turtle()
    ball.color("red")
    ball.shape("circle")
    ball.speed(0)
    ball.penup()
    ball_x, ball_y = 0, 0
    ball_dx, ball_dy = random.choice([-8, 8]), random.choice([-8, 8])  # Random initial direction
    ball.goto(ball_x, ball_y)

    return ball

# Create a turtle object for Player 1's score display
score_pen_p1 = turtle.Turtle()
score_pen_p1.hideturtle()
score_pen_p1.speed(0)

# Create a turtle object for Player 2's score display
score_pen_p2 = turtle.Turtle()
score_pen_p2.hideturtle()
score_pen_p2.speed(0)

# Shows the score on the screen.
def show_score(turtle, x_pos, score):
    turtle.clear()
    turtle.color("white")
    turtle.penup()
    turtle.goto(x_pos, 150)
    font = ("comic sans", 75, "normal") # I choose comic sans because I think it is funny lol.
    turtle.write(score, align="center", font=font)\
    
# Function to hide the message
def hide_message():
    message.clear()

# Function to start the game
def start_game():
    global game_start, p1_score, p2_score, ball_x, ball_y, ball_dx, ball_dy

    # Initialize game variables
    if not game_start:
        p1_score = 0
        p2_score = 0
        ball_x = 0
        ball_y = 0
        ball_dx = random.choice([-8, 8])
        ball_dy = random.choice([-8, 8])
        game_start = True

    # Call update_screen() to start the game loop
    update_screen()

     # Unbind the "Return" key to prevent starting the game multiple times
    turtle.onkeypress(None, "Return")  # Use "Return" for the Enter key

    # Hide the message
    hide_message()

def end_game():
    global ball_x, ball_y, ball_dx, ball_dy
    
    ball_x, ball_y = 0, 0
    ball_dx, ball_dy = 0, 0 

    if p1_score > p2_score:
        messagebox.showinfo("Game over!", "Player 1 wins!")
    elif p1_score == p2_score:
        messagebox.showinfo("Game over!", "Both players tie!")
    else:
        messagebox.showinfo("Game over!", "Player 2 wins!")

    sys.exit()

# Function to update the screen
def update_screen():
    # Player Movement 
    if is_moving_up_p1:
        y = player_turtle.ycor()
        y += player_speed
        if y > 200:  # Upper bound of the player's movement
            y = 200
        player_turtle.sety(y)
    elif is_moving_down_p1:
        y = player_turtle.ycor()
        y -= player_speed
        if y < -200:  # Lower bound of the player's movement
            y = -200
        player_turtle.sety(y)

    if is_moving_up_p2:
        y = player_turtle_2.ycor()
        y += player_speed
        if y > 200:  # Upper bound of the second player's movement
            y = 200
        player_turtle_2.sety(y)
    elif is_moving_down_p2:
        y = player_turtle_2.ycor()
        y -= player_speed
        if y < -200:  # Lower bound of the second player's movement
            y = -200
        player_turtle_2.sety(y)

    # Ball movement & score
    global ball_x, ball_y, ball_dx, ball_dy, p1_score, p2_score
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with top and bottom walls
    if ball_y > 250 or ball_y < -250:
        ball_dy *= -1

    # Check for collisions with players
    if (player_turtle.xcor() - 20) < ball_x < (player_turtle.xcor() + 20):
        if (player_turtle.ycor() - 40) <= ball_y <= (player_turtle.ycor() + 40):
            if ball_dx > 0:  # Check if the ball is moving towards the player
                ball_dx *= -1
                ball_x = player_turtle.xcor() - 20 - 1  # Move the ball slightly to the left of the player's edge
            else:  # Ball is moving away from the player
                ball_dx *= -1
                ball_x = player_turtle.xcor() + 20 + 1  # Move the ball slightly to the right of the player's edge

    if (player_turtle_2.xcor() - 20) < ball_x < (player_turtle_2.xcor() + 20):
        if (player_turtle_2.ycor() - 40) <= ball_y <= (player_turtle_2.ycor() + 40):
            if ball_dx < 0:  # Check if the ball is moving towards the player
                ball_dx *= -1
                ball_x = player_turtle_2.xcor() + 20 + 1  # Move the ball slightly to the right of the player's edge
            else:  # Ball is moving away from the player
                ball_dx *= -1
                ball_x = player_turtle_2.xcor() - 20 - 1  # Move the ball slightly to the left of the player's edge
            
    if ball_x > 430:
        p1_score += 1
        #show_score(-100, p1_score)
        
         # Reset position.
        ball_x = 0
        ball_y = 0

        # Random direction.
        ball_dx = random.choice([-8, 8])
        ball_dy = random.choice([-8, 8])
        
    elif ball_x < -430:
        p2_score += 1
        #show_score(100, p2_score)
        
        # Reset position.
        ball_x = 0
        ball_y = 0
        # Random direction.
        ball_dx = random.choice([-8, 8])
        ball_dy = random.choice([-8, 8])

    # Update ball position on the screen
    pong_ball.goto(ball_x, ball_y)
    
    # Update and display Player 1's score
    show_score(score_pen_p1, -100, p1_score)

    # Update and display Player 2's score
    show_score(score_pen_p2, 100, p2_score)

    pong_window.update()  # Update the screen
    pong_window.ontimer(update_screen, 40)  # Repeat the function after 50 milliseconds
   
# Call the player function first
player_turtle  = player(-415)
player_turtle_2 = player(410)

# Call the ball function to create the ball.
pong_ball = ball()

# Call the show_score function to show the player's score.
#show_score(100, p1_score)
#show_score(-100, p2_score)

# Set up the key binding
turtle.listen()

# Player 1's movement
turtle.onkeypress(move_up_p1, "w")  # Press 'w' to move the player up
turtle.onkeypress(move_down_p1, "s")  # Press 's' to move the player up

# Player 2's movement
turtle.onkeypress(move_up_p2, "Up")  # Press the up arrow key to move the second player up
turtle.onkeypress(move_down_p2, "Down")  # Press the down arrow key to move the second player down

# Bind the Enter key press to the start_game function
turtle.onkeypress(start_game, "Return")  # Use "Return" for the Enter key

turtle.onkeypress(end_game, "BackSpace")  # This ends the game

# Message
message = turtle.Turtle()
# Set the turtle shape to "blank" to hide the cursor
message.shape("blank")
message.color("white")
message.penup()
message.goto(0, 150)
font = ("comic sans", 25, "normal") # I choose comic sans because I think it is funny lol.
message.write("Press enter to start the game.", align="center", font=font)

# Create the window down here.
pong_window = turtle.Screen()
pong_window.bgcolor("black")
pong_window.title("Pong")
pong_window.setup(width = 858, height = 525)
pong_window.cv._rootwindow.resizable(False, False)
pong_window.tracer(0)


# Start the update_screen function
# update_screen()

# Start the game
turtle.done()

pong_window.mainloop()
