# 🐍 Simple Snake Game in Python

This is a classic implementation of the **Snake game** in Python using the built-in **Turtle graphics library**.  
The player controls a snake that moves in a fixed direction, consumes food to grow, and wraps around the screen when reaching the edges.

---

## 🎮 Gameplay Features

✅ Move using arrow keys

✅ Eat food to grow

✅ Food spawns randomly

✅ Score increases with each food eaten

✅ Screen wrapping: the snake reappears on the opposite side

✅ Game Over if the snake hits itself

✅ Press **Enter** or **Space** to restart after Game Over

---

## 🧠 Code Structure Overview

### 📦 Imports
- `turtle` – Used for drawing all graphical elements.
- `random` – Used for generating random food positions.

---

### ⚙️ Initialization

- `WIDTH`, `HEIGHT` – Full screen dimensions.
- `FOOD_SIZE` – Diameter of food (smaller than snake segment).
- `DELAY` – Movement delay in milliseconds (100ms).
- `offsets` – Dictionary for direction control (up/down/left/right).

---

### 📌 Global Variables

- `snake` – List of segments representing the snake's body.
- `snake_direction` – Current movement direction.
- `food_pos` – Position of the food.
- `pen`, `food`, `screen`, `score_pen` – Turtle objects for rendering.
- `score` – Integer score tracker.

---

## 🔄 Game Functions

### 🔁 `reset()`
- Resets snake to initial position.
- Resets food and score.
- Starts movement loop.

### 🐍 `move_snake()`
- Moves snake in current direction.
- Checks collision with self.
- Checks for food collision.
- Implements screen wrapping.
- Redraws the snake segments.

### 🍎 `food_collision()`
- Checks if head is close enough to food.
- If true: update score, reposition food, and grow snake.

### 🎯 `get_random_food_pos()`
- Returns a valid random position inside the screen boundaries.

### 📏 `get_distance(pos1, pos2)`
- Calculates Euclidean distance between two points.

### ⬆️⬇️⬅️➡️ Direction Controls
- `go_up()`, `go_down()`, `go_left()`, `go_right()`  
  Update direction, preventing 180° turn into itself.

### 🧮 `update_score()`
- Updates score display at top of screen.

### 💀 `game_over()`
- Stops movement.
- Displays **GAME OVER** message.
- Binds **Enter** and **Space** to restart.

### 🔄 `restart_game()`
- Clears screen and restarts game from scratch.

---

## 🖥️ Graphical Setup

### 📺 Screen Setup
- Full-screen window
- Title and background color
- Turn off automatic animation for smoother updates

### 🎨 Drawing the Border
- A white rectangle is drawn using a `Turtle` to frame the game area

### 🟨 Snake and 🍎 Food
- Snake segments are drawn using stamps (square shape)
- Food is a red circle, scaled smaller than the snake

### 🎯 Score
- Displayed at the top of the screen using a hidden turtle

---

## 🎮 Controls

- `Arrow Keys` – Move the snake
- `Space` or `Enter` – Restart after game over

---

## ▶️ How to Run

No external libraries required. Just use Python 3:

```bash
python SnakeGame.py
```
## 👨‍💻 Author
Made with 🐍 and ❤️ in Python Turtle by CristiC7.

Feel free to fork, suggest improvements, or use this code as a learning resource.


