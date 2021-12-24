
from consts import *
from game2d import *
from consts import *


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
        self.visible = True

    def __repr__(self):
        return f"{self.bottom}"


class Piece(object):
      def __init__(self, init_x, init_y):
            self.current_x = init_x
            self.current_y = init_y

      def canDrop(self, done):
            return all([block.bottom > 0 for block in self.blocks]) and not any([any([block.bottom == done_block.top and block.left == done_block.left and block.right == done_block.right for done_block in done]) for block in self.blocks])

      def canMoveLeft(self, done):
            return all([block.left > 0 for block in self.blocks]) and not any([any([block.left == done_block.right and block.top == done_block.top and block.bottom == done_block.bottom for done_block in done]) for block in self.blocks])

      def canMoveRight(self, done):
            return all([block.right < GAME_WIDTH for block in self.blocks]) and not any([any([block.right == done_block.left and block.top == done_block.top and block.bottom == done_block.bottom for done_block in done]) for block in self.blocks])

      def canRotate(self, done, tentative_blocks):
            return all([block.bottom >= 0 and block.left >= 0 and block.right <= GAME_WIDTH for block in tentative_blocks]) and not any([any([done_block.x == block.x and done_block.y == block.y for done_block in done]) for block in tentative_blocks])

      def rotate(self):
        if self.orientation == ORIENTATION.West:
            self.blocks = self.get_next_orientation()
            self.orientation = ORIENTATION.North
        elif self.orientation == ORIENTATION.North:
            self.blocks = self.get_next_orientation()
            self.orientation = ORIENTATION.East
        elif self.orientation == ORIENTATION.East:
            self.blocks = self.get_next_orientation()
            self.orientation = ORIENTATION.South
        elif self.orientation == ORIENTATION.South:
            self.blocks = self.get_next_orientation()
            self.orientation = ORIENTATION.West
      
      def __repr__(self):
            return f"{self.__class__.__name__}: ({self.current_x}, {self.current_y}), {self.orientation}"


class OPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
        self.blocks = [
            Block(x=init_x - BLOCK_LENGTH/2, y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2),
            Block(x=init_x + BLOCK_LENGTH/2, y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2),
            Block(x=init_x - BLOCK_LENGTH/2, y=init_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2),
            Block(x=init_x + BLOCK_LENGTH/2, y=init_y - 3*BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='blue', linecolor='black', linewidth=2)
        ]

    def get_next_orientation(self):
          return self.blocks


class IPiece(Piece):
      def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
        self.blocks = [
            Block(x=init_x + (3*BLOCK_LENGTH/2), y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
            Block(x=init_x + (BLOCK_LENGTH/2), y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
            Block(x=init_x - BLOCK_LENGTH/2, y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
            Block(x=init_x - 3*(BLOCK_LENGTH/2), y=init_y - BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2)
        ]

      def get_next_orientation(self):
            if self.orientation == ORIENTATION.West:
                  return [
                  Block(x=self.current_x + (3*BLOCK_LENGTH/2), y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x + (BLOCK_LENGTH/2), y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - 3*(BLOCK_LENGTH/2), y=self.current_y - BLOCK_LENGTH/2,
                        width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2)
                  ]
            elif self.orientation == ORIENTATION.North:
                  return [
                  Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 7*BLOCK_LENGTH/2,
                        width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2)
                  ]
            elif self.orientation == ORIENTATION.East:
                  return [
                  Block(x=self.current_x + (3*BLOCK_LENGTH/2), y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x + (BLOCK_LENGTH/2), y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - 3*(BLOCK_LENGTH/2), y=self.current_y - BLOCK_LENGTH/2,
                        width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2)
                  ]
            elif self.orientation == ORIENTATION.South:
                  return [
                  Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                        height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2),
                  Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 7*BLOCK_LENGTH/2,
                        width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='green', linecolor='black', linewidth=2)
                  ]


class SPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
        self.blocks = [
            Block(x=init_x + BLOCK_LENGTH/2, y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
            Block(x=init_x + BLOCK_LENGTH/2, y=init_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
            Block(x=init_x + 3*BLOCK_LENGTH/2, y=init_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
            Block(x=init_x - BLOCK_LENGTH/2, y=init_y - 3*BLOCK_LENGTH/2,
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2)
        ]

    def get_next_orientation(self):
        if self.orientation == ORIENTATION.West:
            return [
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2)
            ]

        elif self.orientation == ORIENTATION.North:
            return [
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2)
            ]

        elif self.orientation == ORIENTATION.East:
            return [
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2)
            ]

        elif self.orientation == ORIENTATION.South:
            return [
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='red', linecolor='black', linewidth=2)
            ]


class LPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
        self.blocks = [
            Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
            Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
            Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
            Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2)
        ]

    def get_next_orientation(self):
        if self.orientation == ORIENTATION.West:
            return [
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2)
            ]
        elif self.orientation == ORIENTATION.North:
            return[
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2)
            ]
        elif self.orientation == ORIENTATION.East:
            return [
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2)
            ]
        elif self.orientation == ORIENTATION.South:
            return  [
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y - 5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y - BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='purple', linecolor='black', linewidth=2)
            ]


class JPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
        self.blocks = [
            Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
            Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
            Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                  height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
            Block(x=self.current_x - (BLOCK_LENGTH/2), y=self.current_y+(BLOCK_LENGTH/2),
                  width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2)
        ]

    def get_next_orientation(self):
        if self.orientation == ORIENTATION.West:
            return[
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x - (BLOCK_LENGTH/2), y=self.current_y+(BLOCK_LENGTH/2),
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2)]

        elif self.orientation == ORIENTATION.North:
            return [
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-5*BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2)
            ]

        elif self.orientation == ORIENTATION.East:
            return [
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + 3*BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + (3*BLOCK_LENGTH/2), y=self.current_y-(3*BLOCK_LENGTH/2),
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2)
            ]

        elif self.orientation == ORIENTATION.South:
            return[
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x - BLOCK_LENGTH/2, y=self.current_y-5*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2),
                Block(x=self.current_x + BLOCK_LENGTH/2, y=self.current_y-5*BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='gray', linecolor='black', linewidth=2)
            ]


class ZPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
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

    def get_next_orientation(self):
        if self.orientation == ORIENTATION.West:
            return [
                Block(x=self.current_x+3*BLOCK_LENGTH/2, y=self.current_y+BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-(BLOCK_LENGTH/2),
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
            ]
        elif self.orientation == ORIENTATION.North:
            return [
                Block(x=self.current_x-BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-(3*BLOCK_LENGTH/2),
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
            ]
        elif self.orientation == ORIENTATION.East:
            return[
                Block(x=self.current_x+3*BLOCK_LENGTH/2, y=self.current_y+BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-(BLOCK_LENGTH/2),
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
            ]
        elif self.orientation == ORIENTATION.South:
            return [
                Block(x=self.current_x-BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-(3*BLOCK_LENGTH/2),
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='brown', linecolor='black', linewidth=2)
            ]


class TPiece(Piece):
    def __init__(self, init_x=GAME_WIDTH/2, init_y=GAME_HEIGHT, orientation=ORIENTATION.North):
        super().__init__(init_x, init_y)
        self.orientation = orientation
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

    def get_next_orientation(self):
        if self.orientation == ORIENTATION.West:
            return [
                Block(x=self.current_x-BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y+BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2)]
        elif self.orientation == ORIENTATION.North:
            return [
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2 + BLOCK_LENGTH, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2)]
        elif self.orientation == ORIENTATION.East:
            return[
                Block(x=self.current_x-BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x)+(3*BLOCK_LENGTH/2), y=self.current_y-BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2)]
        elif self.orientation == ORIENTATION.South:
            return [
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2 + BLOCK_LENGTH, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=self.current_x+BLOCK_LENGTH/2, y=self.current_y-BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x+BLOCK_LENGTH/2), y=self.current_y-3*BLOCK_LENGTH/2, width=BLOCK_LENGTH,
                      height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2),
                Block(x=(self.current_x)-(BLOCK_LENGTH/2), y=self.current_y-BLOCK_LENGTH/2,
                      width=BLOCK_LENGTH, height=BLOCK_LENGTH, fillcolor='yellow', linecolor='black', linewidth=2)
            ]
