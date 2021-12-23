from consts import *
from game2d import *
from wave import *
from models import *


class Pytrix(GameApp):

    def start(self):
        self.time = 0
        self.piece = LPiece()
        self.last_keys = ()
        self.done = []

    def update(self, dt):
        self.time += dt
        move(self)
        if self.piece.canDrop():
            if self.time > 0.8:
                for item in self.piece.blocks:
                    item.y -= BLOCK_LENGTH
                self.time = 0
        else:
            for item in self.piece.blocks:
                self.done.append(item)
            self.piece = OPiece()

    def draw(self):
        for item in self.done:
            item.draw(self.view)
        for item in self.piece.blocks:
            item.draw(self.view)
    
## Helper functions
def move(self):
    if 'right' in self.input.keys and self.piece.canMoveRight() and self.last_keys == ():
        for item in self.piece.blocks:
            item.x += BLOCK_LENGTH
    if 'left' in self.input.keys and self.piece.canMoveLeft() and self.last_keys == ():
        for item in self.piece.blocks:
            item.x -= BLOCK_LENGTH
    if 'down' in self.input.keys and self.piece.canDrop() and self.last_keys == ():
        for item in self.piece.blocks:
            item.y -= BLOCK_LENGTH

    self.last_keys = self.input.keys
