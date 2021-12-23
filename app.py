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
import math
# from models import *


# PRIMARY RULE: Invaders can only access attributes in wave.py via getters/setters
# Invaders is NOT allowed to access anything in models.py

class Pytrix(GameApp):

    def start(self):

        # IMPLEMENT ME

        # self.square = GImage(x=GAME_WIDTH/2, y=GAME_HEIGHT/2, width=60, height=60, source=SHIP_IMAGE)
        # self.boxes = []
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
            # self.square.x += 1
        if 'left' in self.input.keys and self.last_keys == ():
            # self.square.x -= 1
            for item in self.piece.blocks:
                item.x -= BLOCK_LENGTH
        if 'up' in self.input.keys and self.last_keys == ():
            # self.square.y += 1
            for item in self.piece.blocks:
                item.y += BLOCK_LENGTH
        if 'down' in self.input.keys and self.last_keys == ():
            # self.square.y -= 1
            for item in self.piece.blocks:
                item.y -= BLOCK_LENGTH

        self.last_keys = self.input.keys
        print(len(self.done))
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

        # IMPLEMENT ME
        # dark background

        # for item in self.boxes:
        #     item.draw(self.view)
        # print(len(self.piece.blocks))
        for item in self.done:
            item.draw(self.view)
        for item in self.piece.blocks:
            item.draw(self.view)
            # print(item)
        # self.square.draw(self.view)

    # HELPER METHODS FOR THE STATES GO HERE
