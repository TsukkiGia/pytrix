
from consts import *
from game2d import *


class Block(GRectangle):

    def __init__(self, x, y, width, height, fillcolor, linecolor, linewidth, angle=0):
        super().__init__(x=x,
                         y=y,
                         width=width,
                         height=height,
                         fillcolor=fillcolor,
                         linecolor=linecolor,
                         linewidth=linewidth,
                         angle=angle)

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


class IPiece(Piece):
    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2+(3*BLOCK_LENGTH/2), y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH/2), y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2-BLOCK_LENGTH/2, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)-3*(BLOCK_LENGTH/2), y=GAME_HEIGHT-BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2)
        ]


class ZPiece(Piece):
    pass


class LPiece(Piece):
    pass


class JPiece(Piece):
    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH), y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2-BLOCK_LENGTH, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH), y=GAME_HEIGHT-(3*BLOCK_LENGTH/2),
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
        ]


class ZPiece(Piece):
    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2-BLOCK_LENGTH, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2), y=GAME_HEIGHT-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH), y=GAME_HEIGHT-(3*BLOCK_LENGTH/2),
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
        ]


class TPiece(Piece):
    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2-BLOCK_LENGTH, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2), y=GAME_HEIGHT-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH), y=GAME_HEIGHT-BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2)
        ]
