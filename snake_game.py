# I acknowledge the use of Google Gemini to create the code in this file.
import tkinter as tk
import random

# Game Constants
WIDTH = 600
HEIGHT = 400
SPACE_SIZE = 20

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Keele Snake Game")

        self.score = 0
        self.direction = 'right'
        self.game_started = False # NEW: Game starts in a waiting state

        self.label = tk.Label(self.window, text="Score:{}".format(self.score), font=('consolas', 40))
        self.label.pack()

        self.canvas = tk.Canvas(self.window, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        
        self.snake_coords = [[300, 200], [280, 200], [260, 200]]
        self.squares = []
        
        for x, y in self.snake_coords:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="green")
            self.squares.append(square)

        self.food_coords = [random.randint(0, (WIDTH//SPACE_SIZE)-1) * SPACE_SIZE, 
                            random.randint(0, (HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE]
        self.food = self.canvas.create_oval(self.food_coords[0], self.food_coords[1], 
                                            self.food_coords[0] + SPACE_SIZE, 
                                            self.food_coords[1] + SPACE_SIZE, fill="red")
        
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))
        
        # NEW: Bind Space to start the game
        self.window.bind('<space>', lambda event: self.start_game())

        # NEW: Show Start Message
        self.start_text = self.canvas.create_text(WIDTH/2, HEIGHT/2,
                                font=('consolas', 30), text="PRESS SPACE TO START", fill="white")

    def start_game(self):
        # Only start if the game isn't already running
        if not self.game_started:
            self.game_started = True
            self.canvas.delete(self.start_text) # Remove the "Press Space" message
            self.next_turn()

    def change_direction(self, new_dir):
        if new_dir == 'left' and self.direction != 'right':
            self.direction = new_dir
        elif new_dir == 'right' and self.direction != 'left':
            self.direction = new_dir
        elif new_dir == 'up' and self.direction != 'down':
            self.direction = new_dir
        elif new_dir == 'down' and self.direction != 'up':
            self.direction = new_dir

    def next_turn(self):
        x, y = self.snake_coords[0]

        if self.direction == "up": y -= SPACE_SIZE
        elif self.direction == "down": y += SPACE_SIZE
        elif self.direction == "left": x -= SPACE_SIZE
        elif self.direction == "right": x += SPACE_SIZE

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or [x, y] in self.snake_coords:
            self.game_over()
            return

        self.snake_coords.insert(0, [x, y])
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="green")
        self.squares.insert(0, square)

        if x == self.food_coords[0] and y == self.food_coords[1]:
            self.score += 1
            self.label.config(text="Score:{}".format(self.score))
            self.canvas.delete(self.food)
            self.food_coords = [random.randint(0, (WIDTH//SPACE_SIZE)-1) * SPACE_SIZE, 
                                random.randint(0, (HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE]
            self.food = self.canvas.create_oval(self.food_coords[0], self.food_coords[1], 
                                                self.food_coords[0] + SPACE_SIZE, 
                                                self.food_coords[1] + SPACE_SIZE, fill="red")
        else:
            del self.snake_coords[-1]
            self.canvas.delete(self.squares[-1])
            del self.squares[-1]

        self.window.after(100, self.next_turn)

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(WIDTH/2, HEIGHT/2,
                                font=('consolas', 70), text="GAME OVER", fill="red")

if __name__ == "__main__":
    game = SnakeGame()
    game.window.mainloop()