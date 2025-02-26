import turtle  # Import the Turtle library for graphics
import random  # Import the Random library for generating food positions

# Set the screen dimensions to full-screen mode
WIDTH = turtle.window_width()  # Screen width
HEIGHT = turtle.window_height()  # Screen height
FOOD_SIZE = 15  # Food size (75% of a snake segment, which is 20)
DELAY = 100  # Delay between moves (ms)

# Dictionary defining movement directions (coordinate changes)
offsets = {
    "up": (0, 20),  # Up: add 20 to the Y coordinate
    "down": (0, -20),  # Down: subtract 20 from the Y coordinate
    "left": (-20, 0),  # Left: subtract 20 from the X coordinate
    "right": (20, 0)  # Right: add 20 to the X coordinate
}

# Initialize global variables
snake = []  # List containing the snake segments
snake_direction = "up"  # Initial direction is up
food_pos = ()  # Food position
pen = None  # Pen for drawing the snake
food = None  # Food object
screen = None  # Game screen
score = 0  # Player's score
score_pen = None  # Pen for displaying the score

# Function to reset the game
def reset():
    global snake, snake_direction, food_pos, pen, food, score
    snake.clear()  # Clear the snake segments
    snake = [[0, 0], [0, 20], [0, 40]]  # Reinitialize the snake with 3 segments
    snake_direction = "up"  # Set the default direction to up
    food_pos = get_random_food_pos()  # Generate a new position for the food
    food.goto(food_pos)  # Place the food on the screen
    score = 0  # Reset the score
    update_score()  # Update the score display
    move_snake()  # Start the game

# Function to move the snake
def move_snake():
    global snake_direction, score

    new_head = snake[-1].copy()  # Create a copy of the snake's head
    new_head[0] += offsets[snake_direction][0]  # Modify X position
    new_head[1] += offsets[snake_direction][1]  # Modify Y position

    # Check if the snake collides with itself
    if new_head in snake:
        game_over()
        return

    snake.append(new_head)  # Add the new head position
    if not food_collision():  # If it doesn't eat, remove the last segment
        snake.pop(0)

    # Allows "exiting" the screen and reappearing on the opposite side (screen wrapping)
    if snake[-1][0] > WIDTH / 2:  
        snake[-1][0] = -WIDTH / 2 + 10
    elif snake[-1][0] < -WIDTH / 2:  
        snake[-1][0] = WIDTH / 2 - 10
    elif snake[-1][1] > HEIGHT / 2:  
        snake[-1][1] = -HEIGHT / 2 + 10
    elif snake[-1][1] < -HEIGHT / 2:  
        snake[-1][1] = HEIGHT / 2 - 10

    pen.clearstamps()  # Clear all previous stamps
    for index, segment in enumerate(snake):
        if index == len(snake) - 1:  
            pen.color("blue")  # Change the snake's head to blue
        else:
            pen.color("yellow")  # The body remains yellow
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()
    turtle.ontimer(move_snake, DELAY)  # Re-call the function after DELAY milliseconds

# Checks if the snake eats the food
def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < FOOD_SIZE:  # Check distance to food
        food_pos = get_random_food_pos()
        food.goto(food_pos)  # Relocate food
        score += 1  # Increase the score
        update_score()  # Update the score display
        return True
    return False

# Generate a random position for food
def get_random_food_pos():
    x = random.randint(int(-WIDTH / 2 + FOOD_SIZE), int(WIDTH / 2 - FOOD_SIZE))
    y = random.randint(int(-HEIGHT / 2 + FOOD_SIZE), int(HEIGHT / 2 - FOOD_SIZE))
    return (x, y)

# Calculates the distance between two points
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Euclidean distance formula
    return distance

# Functions to control the snake's direction
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Update the score on the screen
def update_score():
    score_pen.clear()
    score_pen.goto(0, HEIGHT / 2 - 40)  # Position the score at the top
    score_pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Display the GAME OVER message and allow restart
def game_over():
    pen.goto(0, 0)
    pen.color("red")
    pen.write(f"GAME OVER\nScore: {score}\nPRESS ENTER OR SPACE TO CONTINUE", 
              align="center", font=("Arial", 24, "normal"))
    screen.onkey(restart_game, "space")  # Space to restart
    screen.onkey(restart_game, "Return")  # Enter to restart

# Restart the game
def restart_game():
    reset()
    pen.clear()  # Clear the GAME OVER message

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Draw the border
border_pen = turtle.Turtle()
border_pen.penup()
border_pen.goto(-WIDTH / 2, HEIGHT / 2)
border_pen.pendown()
border_pen.pencolor("white")
border_pen.pensize(3)
for _ in range(2):
    border_pen.forward(WIDTH)
    border_pen.right(90)
    border_pen.forward(HEIGHT)
    border_pen.right(90)
border_pen.hideturtle()

# Setup the pen for drawing the snake
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("yellow")

# Setup the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Setup the score pen
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.color("white")
score_pen.hideturtle()

# Set up controls
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Initialize the game
reset()
turtle.done()
