"""
This is the main driver file responsible for handling user inputs and displaying the current game state objects.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512                # 400 is another good option, for larger board needs better quality images
DIMENSION = 8                       # Dimensions of the chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15                        # For animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called only once in the main to avoid lagging.
'''

def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wP']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"))
    # Note: an image can be accessed by e.g. "IMAGES['wP']"

'''
The main driver for the code, which will handle user input and update the graphics.
'''

def main()
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() #Only do this once
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
               running = False

        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()