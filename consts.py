"""
Constants for Tetris

This module global constants for the game Tetris.
"""
import enum
### WINDOW CONSTANTS (all coordinates are in pixels) ###

#: the width of the game display
GAME_WIDTH  = 900
#: the height of the game display
GAME_HEIGHT = 900

BLOCK_LENGTH = 30

class ORIENTATION(enum.Enum):
    North = 1
    East = 2
    South = 3
    West = 4

