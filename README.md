# Simple-Snake-Game-in-Python
This is an implementation of the game Snake in Python using the Turtle library. The game lets you control a snake that moves in a fixed direction, eats food to grow, and can pass through the edge of the screen, reappearing on the opposite side (screen wrapping).

Description of the main code components:

● Import libraries:
 
turtle - used to draw the graphical elements of the game. 

Random - used to generate random food positions. 

● Initializing game parameters:
 
WIDTH, HEIGHT - screen dimensions;

FOOD_SIZE - food size; 

DELAY - delay between snake moves (100ms); 

offsets - dictionary defining the coordinate changes for each direction. 

● Defining global variables:
 
snake - list that holds the snake body segments; 

snake_direction - current direction of movement; 

food_pos - position of food on the screen; 

pen, food, screen - Turtle objects to draw the snake, food, and screen; 

score, score_pen - player's score and the tool to display it. 


Game functionality:

● Game reset (reset()):

Reset the position of the snake and food. 

Resets the score and restarts the game.

● Move snake (move_snake()):

Calculates the new head position.

Check if the snake hits its own body → end game.

If the snake doesn't eat the food, the last body part is discarded.

Implement screen wrapping: if the snake exits the screen, it reappears on the opposite side.

Redraw the snake.

● Food collision (food_collision()):

If the snake touches the food, it is moved to a random position.

Increase the score and refresh the display.

● Generate random food position (get_random_food_pos()):

Calculates a random position on the screen, taking into account its size.

● Calculate the distance between two points (get_distance()):

Use the Euclidean distance formula to check if the snake has touched the food.

● Direction control (go_up(), go_down(), go_left(), go_right()):

Updates the direction of movement, avoiding sudden changes (e.g. can't go directly from "up" to "down").

● Update score (update_score()):

Displays the current score at the top of the screen.

● End game (game_over()):

Displays the message "GAME OVER".

Press Enter or Space to resume the game.

● Restart game (restart_game()):

Resets the game and clears the "GAME OVER" message.


Initialization and GUI:

● Setting up the screen (screen = turtle.Screen()):

Set the window size and title.

Disable animations for better performance.

● Drawing the border:

Draw a white rectangle around the screen using a Turtle.

● Creating graphic objects:

Pen - drawing snake; 

Food - drawing food; 

Score Pen (score_pen) - displaying the score. 

● Binding keys for control:

screen.onkey(go_up, "Up") - move up; 

screen.onkey(go_down, "Down") - move down; 

screen.onkey(go_left, "Left") - move left; 

screen.onkey(go_right, "Right") - move right. 

● Starting the game (reset()):

Initialize the snake, its food and its movement.

● Keep program active (turtle.done()):

Keeps the window open to continue the game.

As future improvements, the game could include sounds, obstacles or variable speeds to make it more interesting. 

#Enjoy
