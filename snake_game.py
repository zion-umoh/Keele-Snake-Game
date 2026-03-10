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
        self.canvas = tk.Canvas(self.window, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.window.update()

if __name__ == "__main__":
    game = SnakeGame()
    game.window.mainloop()