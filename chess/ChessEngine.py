"""
Responsible for storing all the information about the current state of the chess game.
Also responsible for determining the possible/valid moves at the current game state.
Maintain a history of the made moves (Logging moves).
"""

class GameState():
    def __init__(self):
        # Board is an 8x8 2d np array, each element is a 2 char string
        # First character represents the color of the piece 'b' or 'w'
        # Second character represents the type of the piece 'R', 'N', 'B', 'Q', 'K', 'P'
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]

        self.whiteToMove = True
        self.moveLog = []
