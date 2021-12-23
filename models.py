"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything
that you interact with on the screen is model: the ship, the laser bolts, and
the aliens.

Just because something is a model does not mean there has to be a special
class for it. Unless you need something special for your extra gameplay
features, Ship and Aliens could just be an instance of GImage that you move
across the screen. You only need a new class when you add extra features to
an object. So technically Bolt, which has a velocity, is really the only model
that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens. That is
because there are a lot of constants in consts.py for initializing the
objects, and you might want to add a custom initializer.  With that said,
feel free to keep the pass underneath the class definitions if you do not want
to do that.

You are free to add even more models to this module.  You may wish to do this
when you add new features to your game, such as power-ups.  If you are unsure
about whether to make a new class or not, please ask on Piazza.

Adam Issah, abi6
December 6, 2021
"""
from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other
# than consts.py.  If you need extra information from Gameplay, then it should
# be a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


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
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

# Making Alien a subclass of GSprite just so I get the BLUE version of the third alien variant


class OPiece(object):

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

    def canDrop(self):
        return all([block.bottom > 0 for block in self.blocks])


class Bolt(GRectangle):
    """
    A class representing a laser bolt.

    Laser bolts are often just thin, white rectangles. The size of the bolt
    is determined by constants in consts.py. We MUST subclass GRectangle,
    because we need to add an extra (hidden) attribute for the velocity of
    the bolt.

    The class Wave will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with
    no setters for the velocities.  That is because the velocity is fixed and
    cannot change once the bolt is fired.

    In addition to the getters, you need to write the __init__ method to set
    the starting velocity. This __init__ method will need to call the __init__
    from GRectangle as a  helper.

    You also MIGHT want to create a method to move the bolt.  You move the
    bolt by adding the velocity to the y-position.  However, the getter
    allows Wave to do this on its own, so this method is not required.
    """
    # INSTANCE ATTRIBUTES:
    # Attribute _velocity: the velocity in y direction
    # Invariant: _velocity is an int or float

    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO SET THE VELOCITY
    def __init__(self, x, top, bottom, width, height, velocity, fillcolor):
        super().__init__(x=x, top=top, bottom=bottom, width=width, height=height,
                         fillcolor=fillcolor)
        self.velocity = velocity
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

    def isPlayerBolt(self):
        """ Return True if bolt was shot by ship object, else False """
        if self.velocity > 0:
            return True
        return False

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE
