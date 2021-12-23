
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

    def canMoveLeft(self):
        return all([block.left > 0 for block in self.blocks])

    def canMoveRight(self):
        return all([block.right < GAME_WIDTH for block in self.blocks])


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


class SPiece(Piece):
    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2+(BLOCK_LENGTH/2), y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)+(BLOCK_LENGTH/2), y=GAME_HEIGHT-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2+3*BLOCK_LENGTH/2, y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
            Block(x=(GAME_WIDTH/2)-(BLOCK_LENGTH/2), y=GAME_HEIGHT-3*BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2)
        ]


class LPiece(Piece):
    def __init__(self):
        self.blocks = [
            Block(x=GAME_WIDTH/2+(BLOCK_LENGTH/2), y=GAME_HEIGHT-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2+(BLOCK_LENGTH/2), y=GAME_HEIGHT-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2+(BLOCK_LENGTH/2), y=GAME_HEIGHT-5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
            Block(x=GAME_WIDTH/2+3*(BLOCK_LENGTH/2), y=GAME_HEIGHT-5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
        ]


class JPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT):
        self.blocks = [
            Block(x=init_x+BLOCK_LENGTH/2, y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
            Block(x=(init_x)+(3*BLOCK_LENGTH/2), y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
            Block(x=init_x-BLOCK_LENGTH/2, y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
            Block(x=(init_x)+(3*BLOCK_LENGTH/2), y=init_y-(3*BLOCK_LENGTH/2),
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2)
        ]


class ZPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT):
        self.blocks = [
            Block(x=init_x-BLOCK_LENGTH/2, y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=init_x+BLOCK_LENGTH/2, y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=(init_x+BLOCK_LENGTH/2), y=init_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
            Block(x=(init_x)+(3*BLOCK_LENGTH/2), y=init_y-(3*BLOCK_LENGTH/2),
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
        ]


class TPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT):
        self.blocks = [
            Block(x=init_x-BLOCK_LENGTH/2, y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
            Block(x=init_x+BLOCK_LENGTH/2, y=init_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
            Block(x=(init_x+BLOCK_LENGTH/2), y=init_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
            Block(x=(init_x)+(3*BLOCK_LENGTH/2), y=init_y-BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2)
        ]
