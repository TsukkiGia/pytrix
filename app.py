"""
Primary module for Alien Invaders

This module contains the main controller class for the Alien Invaders app.
There is no need for any additional classes in this module.  If you need
more classes, 99% of the time they belong in either the wave module or the
models module. If you are unsure about where a new class should go, post a
question on Piazza.

Adam Issah, abi6
December 6, 2021
"""
from consts import *
from game2d import *
from wave import *
from models import *

class Pytrix(GameApp):

    def start(self):
        self.time = 0
        self.piece = OPiece()
        self.last_keys = ()
        self.done = []

        # Welcome Screen

    def update(self, dt):
        self.time += dt
        if 'right' in self.input.keys and self.last_keys == ():
            for item in self.piece.blocks:
                item.x += BLOCK_LENGTH
        if 'left' in self.input.keys and self.last_keys == ():
            for item in self.piece.blocks:
                item.x -= BLOCK_LENGTH
        if 'down' in self.input.keys and self.last_keys == ():
            for item in self.piece.blocks:
                item.y -= BLOCK_LENGTH

        self.last_keys = self.input.keys
        if self.piece.canDrop():
            if self.time > 0.8:
                for item in self.piece.blocks:
                    item.y -= BLOCK_LENGTH
                self.time = 0
        else:
            self.piece.blocks[0].bottom = BLOCK_LENGTH
            self.piece.blocks[1].bottom = BLOCK_LENGTH
            self.piece.blocks[2].bottom = 0
            self.piece.blocks[3].bottom = 0
            for item in self.piece.blocks:
                self.done.append(item)
            self.piece = OPiece()

    def draw(self):
        for item in self.done:
            item.draw(self.view)
        for item in self.piece.blocks:
            item.draw(self.view)
