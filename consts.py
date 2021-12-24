"""
Constants for Tetris

This module global constants for the game Tetris.
"""
import enum
### WINDOW CONSTANTS (all coordinates are in pixels) ###

#: the width of the game display
GAME_WIDTH = 300
#: the height of the game display
GAME_HEIGHT = 600

BLOCK_LENGTH = 30


class ORIENTATION(enum.Enum):
    North = 1
    East = 2
    South = 3
    West = 4
