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
        self.direction = 'down'
        
        self.canvas = tk.Canvas(self.window, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        
        # Initial Snake positions
        self.snake_coords = [[0, 0], [0, 20], [0, 40]]
        self.squares = []
        
        for x, y in self.snake_coords:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="green")
            self.squares.append(square)

        self.food_coords = [random.randint(0, (WIDTH//SPACE_SIZE)-1) * SPACE_SIZE, 
                            random.randint(0, (HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE]
        self.food = self.canvas.create_oval(self.food_coords[0], self.food_coords[1], 
                                            self.food_coords[0] + SPACE_SIZE, 
                                            self.food_coords[1] + SPACE_SIZE, fill="red")
    
if __name__ == "__main__":
    game = SnakeGame()
    game.window.mainloop()