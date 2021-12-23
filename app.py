from consts import *
from game2d import *
from wave import *
from models import *
import random


class Pytrix(GameApp):

    def start(self):
        self.time = 0
        self.piece = self.pick_a_piece()
        self.last_keys = ()
        self.done = []

    def pick_a_piece(self):
        number = random.randint(0, 6)
        if number == 0:
            return OPiece()
        if number == 1:
            return LPiece()
        if number == 2:
            return ZPiece()
        if number == 3:
            return IPiece()
        if number == 4:
            return JPiece()
        if number == 5:
            return TPiece()
        if number == 6:
            return SPiece()

    def update(self, dt):
        self.time += dt
        move(self)
        if self.piece.canDrop():
            if self.time > 0.8:
                for item in self.piece.blocks:
                    item.y -= BLOCK_LENGTH
                self.time = 0
                self.piece.current_y -= BLOCK_LENGTH
        else:
            for item in self.piece.blocks:
                self.done.append(item)
            self.piece = self.pick_a_piece()

    def draw(self):
        for item in self.done:
            item.draw(self.view)
        for item in self.piece.blocks:
            item.draw(self.view)

# Helper functions


def move(self):
    if 'right' in self.input.keys and self.piece.canMoveRight() and self.last_keys == ():
        for item in self.piece.blocks:
            item.x += BLOCK_LENGTH
        self.piece.current_x += BLOCK_LENGTH
    if 'left' in self.input.keys and self.piece.canMoveLeft() and self.last_keys == ():
        for item in self.piece.blocks:
            item.x -= BLOCK_LENGTH
        self.piece.current_x -= BLOCK_LENGTH
    if 'down' in self.input.keys and self.piece.canDrop() and self.last_keys == ():
        for item in self.piece.blocks:
            item.y -= BLOCK_LENGTH
        self.piece.current_y -= BLOCK_LENGTH

    self.last_keys = self.input.keys
