
from consts import *
from game2d import *

class Block(GRectangle):

    def __init__(self, x, y, width, height, fillcolor, linecolor, linewidth):
        super().__init__(x=x,
                         y=y,
                         width=width,
                         height=height,
                         fillcolor=fillcolor,
                         linecolor=linecolor,
                         linewidth=linewidth)

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.bottom}"


class Piece(object):
    def canDrop(self):
        return all([block.bottom > 0 for block in self.blocks])

class OPiece(Piece):

    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2-BLOCK_LENGTH/2, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH/2), y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2-BLOCK_LENGTH/2, y=GAME_HEIGHT-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH/2), y=GAME_HEIGHT-3*BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2)
        ]

class IPiece(object):
    pass


class ZPiece(object):
    pass

class LPiece(object):
    pass
