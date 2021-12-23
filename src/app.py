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


# PRIMARY RULE: Invaders can only access attributes in wave.py via getters/setters
# Invaders is NOT allowed to access anything in models.py

class Invaders(GameApp):
    """
    The primary controller class for the Alien Invaders application

    This class extends GameApp and implements the various methods necessary
    for processing the player inputs and starting/running a game.

        Method start begins the application.

        Method update either changes the state or updates the Play object

        Method draw displays the Play object and any other elements on screen

    Because of some of the weird ways that Kivy works, you SHOULD NOT create
    an initializer __init__ for this class.  Any initialization should be done
    in the start method instead.  This is only for this class.  All other
    classes behave normally.

    Most of the work handling the game is actually provided in the class Wave.
    Wave should be modeled after subcontrollers.py from lecture, and will
    have its own update and draw method.

    The primary purpose of this class is to manage the game state: which is
    when the game started, paused, completed, etc. It keeps track of that in
    an internal (hidden) attribute.

    For a complete description of how the states work, see the specification
    for the method update.

    Attribute view: the game view, used in drawing
    Invariant: view is an instance of GView (inherited from GameApp)

    Attribute input: user input, used to control the ship or resume the game
    Invariant: input is an instance of GInput (inherited from GameApp)
    """
    # HIDDEN ATTRIBUTES:
    # Attribute _state: the current state of the game represented as an int
    # Invariant: _state is one of STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE,
    # STATE_PAUSED, STATE_CONTINUE, or STATE_COMPLETE
    #
    # Attribute _wave: the subcontroller for a single wave, managing aliens
    # Invariant: _wave is a Wave object, or None if there is no wave currently
    # active. It is only None if _state is STATE_INACTIVE.
    #
    # Attribute _text: the currently active message
    # Invariant: _text is a GLabel object, or None if there is no message to
    # display. It is onl None if _state is STATE_ACTIVE.
    #
    # You may have new attributes if you wish (you might want an attribute to
    # store any score across multiple waves). But you must document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    #
    # Attribute _background: the background of the application
    # Invariant: _background is a GRectangle
    #
    # Attribute lastkeys: the number of keys pressed in the previous frame
    # Invariant: lastkeys is an integer >= 0
    #
    # Attribute _shipImage: an image of the ship
    # Invariant: _shipImage is a GImage
    #
    # Attribute _Title: The title of the game
    # Invariant: _Title is a GLabel
    #
    # Attribute _theme: the theme song of the game
    # Invariant: _theme is a Sound object
    #
    # Attribute _wavetheme: the song that plays during a wave
    # Invariant: _wavetheme is a Sound object


    # DO NOT MAKE A NEW INITIALIZER!

    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which
        you should not override or change). This method is called once the
        game is running. You should use it to initialize any game specific
        attributes.

        This method should make sure that all of the attributes satisfy the
        given invariants. When done, it sets the _state to STATE_INACTIVE and
        create a message (in attribute _text) saying that the user should press
        to play a game.
        """
        # IMPLEMENT ME


        # self.square = GImage(x=GAME_WIDTH/2, y=GAME_HEIGHT/2, width=60, height=60, source=SHIP_IMAGE)
        # self.boxes = []
        self.time = 0
        self.piece = OPiece()
        self.last_keys = ()


        #Welcome Screen




    def update(self,dt):
        self.time += dt

        # self.boxes.append(GRectangle(x=self.square.x, y=self.square.y, width=30, height=30, fillcolor = 'green'))
        # print(self.input.keys)
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


        for item in self.piece.blocks:
            if item.bottom > 0:
                if self.time > 0.8:
                    for item in self.piece.blocks:
                        item.y -= BLOCK_LENGTH
                    self.time = 0
            else:
                self.piece.blocks[0].bottom = BLOCK_LENGTH
                self.piece.blocks[1].bottom = BLOCK_LENGTH
                self.piece.blocks[2].bottom = 0
                self.piece.blocks[3].bottom = 0



    def draw(self):

        # IMPLEMENT ME
        # dark background

        # for item in self.boxes:
        #     item.draw(self.view)
        # print(len(self.piece.blocks))
        for item in self.piece.blocks:
            item.draw(self.view)
            # print(item)
        # self.square.draw(self.view)

    # HELPER METHODS FOR THE STATES GO HERE
