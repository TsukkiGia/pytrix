"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in
the Alien Invaders game.  Instances of Wave represent a single wave. Whenever
you move to a new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on
screen. These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or
models.py. Whether a helper method belongs in this module or models.py is
often a complicated issue.  If you do not know, ask on Piazza and we will
answer.

Adam Issah, abi6
December 6, 2021
"""
from game2d import *
from consts import *
from models import *
import random, time

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

# helpers
def makeAlienList():
    """ Returns a 2d list of alien objects """
    alien_array = [[] for i in range(ALIEN_ROWS)]
    order = list(range(ALIEN_ROWS))

    x = ALIEN_H_SEP + ALIEN_WIDTH/2
    y = GAME_HEIGHT - (ALIEN_CEILING +
        (ALIEN_ROWS-1)*ALIEN_HEIGHT +
        ALIEN_HEIGHT/2 +
        (ALIEN_ROWS-1)*ALIEN_V_SEP)

    dy = ALIEN_V_SEP + ALIEN_HEIGHT
    dx = ALIEN_H_SEP + ALIEN_WIDTH

    cap = 2
    row_num = 0
    type = 0

    for k in order:
        row_num += 1

        if row_num > cap:
            type += 1
            cap += 2

        for j in range(ALIENS_IN_ROW):
            alien_array[k].append(Alien(x = x,
                            y = y,
                            width = ALIEN_WIDTH,
                            height = ALIEN_HEIGHT,
                            type = (type%len(ALIEN_IMAGES)),
                            format = (4, 2)))
            x += dx
        y += dy
        x = ALIEN_H_SEP + ALIEN_WIDTH/2

    return alien_array


def makeShip():
    """ Returns a Ship object """

    return Ship(x = GAME_WIDTH/2,
                bottom = SHIP_BOTTOM,
                width = SHIP_WIDTH,
                height = SHIP_HEIGHT,
                source = SHIP_SPRITE,
                format = (2, 4))


def makeDLine():
    """ Returns a Defense Line (DLine) object """

    return GPath(points = (0,
                 DEFENSE_LINE,
                 GAME_WIDTH, DEFENSE_LINE),
                 linewidth = 2,
                 linecolor = "yellow")


def determineLeftmost(alien_brigade, self):
    """ Returns the leftmost Alien object in the alien brigade """

    leftmost = randomAliveAlien(self)
    for row in alien_brigade:
        for alien in row:
            if alien is not None:
                if alien.x < leftmost.x:
                    leftmost = alien

    return leftmost


def determineRightmost(alien_brigade, self):
    """ Returns the rightmost Alien object in the alien brigade """

    rightmost = randomAliveAlien(self)
    for row in alien_brigade:
        for alien in row:
            if alien is not None:
                if alien.x > rightmost.x:
                    rightmost = alien

    return rightmost

#
def existingBolt(self, bolts):
    """ Returns true if there is a player bolt still on screen """
    for bolt in bolts:
        if bolt.isPlayerBolt():
            return True
    return False


def rightMovement(self):
    """ Handles movement to the right and initials movement to the left when
        rightmost alien reaches the edge of the screen
    """
    rightmost = determineRightmost(self._aliens, self)
    if rightmost.right > GAME_WIDTH - ALIEN_H_SEP:
        for row in self._aliens:
            for alien in row:
                if alien is not None:
                    alien.y -= ALIEN_V_WALK
        self._direction = 1
    else:
        for row in self._aliens:
            for alien in row:
                if alien is not None:
                    alien.x += ALIEN_H_WALK


def leftMovement(self):
    """ Handles movement to the left and initials movement to the right when
        rightmost alien reaches the edge of the screen
    """
    leftmost = determineLeftmost(self._aliens, self)
    if leftmost.left < ALIEN_H_SEP:
        for row in self._aliens:
            for alien in row:
                if alien is not None:
                    alien.y -= ALIEN_V_WALK
        self._direction = 0
    else:
        for row in self._aliens:
            for alien in row:
                if alien is not None:
                    alien.x -= ALIEN_H_WALK


def randomAliveAlien(self):
    """ Returns a random alive alien from the alien brigade """

    available_columns = []
    for i in range(len(self._aliens[0])):
        for row in self._aliens:
            if row[i] is not None:
                available_columns.append(i)

    random_column = random.choice(available_columns)

    available_rows = []
    for j in range(len(self._aliens)):
        if self._aliens[j][random_column] is not None:
            available_rows.append(j)

    random_row = random.choice(available_rows)

    return self._aliens[random_row][random_column]


def randomAliveAlienToShoot(self):
    """ Returns a random alive alien at the bottom of it's column from the alien brigade """

    available_columns = []
    for i in range(len(self._aliens[0])):
        for row in self._aliens:
            if row[i] is not None:
                available_columns.append(i)

    random_column = random.choice(available_columns)

    for i in range(ALIEN_ROWS-1, -1, -1):
        if self._aliens[i][random_column] is not None:
            return self._aliens[i][random_column]


def shipDown(self):
    """ Returns True if alien bolt collides with ship and removes bolt from _bolts"""
    for bolt in self._bolts:
        if self._ship is not None and self._animator is None:
            if self._ship.collides(bolt):
                # Sound(self._soundList[0]).play()
                self._bolts.remove(bolt)
                return True


def alienDown(self):
    """ Handles alien death by making alien None if it collides with a player bolt """
    for bolt in self._bolts:
        for i in range(len(self._aliens)):
            for j in range(len(self._aliens[0])):
                if self._aliens[i][j] is not None:
                    if self._aliens[i][j].collides(bolt):
                        self._aliens[i][j] = None
                        Sound(self._soundList[3]).play()
                        self._bolts.remove(bolt)


def aliensAnnihilated(self):
    """ Returns True if all items in self._aliens are None """
    for row in self._aliens:
        for alien in row:
            if alien is not None:
                return False
    return True


def aliensBreach(self):
    """ Returns True if an alien's bottom attribute < DEFENSE_LINE """
    if not aliensAnnihilated(self):
        for row in self._aliens:
            for alien in row:
                if alien is not None:
                    if alien.bottom < DEFENSE_LINE:
                        return True
        return False


def shipMovements(self, input, dt):
    """ Checks for key presses to moves self._ship or shoot bolts
        Parameter input: the input attribute from GameApp class
        Parameter dt: the amount of time since the last frame
    """
    self._time += dt
    if self._animator is not None:
        pass

    elif self._ship is not None:
        if input.is_key_down('left'):
                if self._ship.left < 0:
                    self._ship.left= 0
                else:
                    self._ship.x -= SHIP_MOVEMENT
        if input.is_key_down('right'):
                if self._ship.right > GAME_WIDTH:
                    self._ship.right = GAME_WIDTH
                else:
                    self._ship.x += SHIP_MOVEMENT

        if input.is_key_down("spacebar") and not existingBolt(self, self._bolts):
            self._bolts.append(Bolt(x=self._ship.x,
                                    top = self._ship.top + BOLT_HEIGHT,
                                    bottom = self._ship.top,
                                    width = BOLT_WIDTH,
                                    height = BOLT_HEIGHT,
                                    velocity = BOLT_SPEED,
                                    fillcolor = "red"))
            Sound(self._soundList[1]).play()


def alienMovements(self):
    """ Handles back and forth / vertical movement of aliens """
    if self._time > ALIEN_SPEED:
        try:
            if self._direction == 0:
                rightMovement(self)

            if self._direction == 1:
                leftMovement(self)

        except:
            pass

        self.steps += 1
        self._time = 0


def boltMovements(self):
    """ Handles player and alien bolt animation and removes offscreen bolts"""
    for bolt in self._bolts:
        # removal
        if bolt.bottom > GAME_HEIGHT:
            self._bolts.remove(bolt)
        if bolt.top < 0:
            self._bolts.remove(bolt)

        #  distinguishing between shooters
        if bolt.isPlayerBolt():
            bolt.y += BOLT_SPEED
        else:
            bolt.y -= BOLT_SPEED


def alienFire(self):
    """ Creates an alien bolt every _alien_fireRate interval """
    if self.steps == self._alien_fireRate:
        try:
            random_alien = randomAliveAlienToShoot(self)
            self._bolts.append(Bolt(x=random_alien.x,
                                    top = random_alien.bottom,
                                    bottom = random_alien.bottom - BOLT_HEIGHT,
                                    width = BOLT_WIDTH,
                                    height = BOLT_HEIGHT,
                                    velocity = -BOLT_SPEED,
                                    fillcolor = "green"))
            Sound(self._soundList[2]).play()
            self.steps = 0
        except:
            pass


def animate_shipDown(self, dt):
    """ Coroutine that handles ship detonation animation"""
    time = 0

    animating = True
    while animating:
        dt = (yield)

        time += dt
        fraction_passed = time/DEATH_SPEED
        frame_check = fraction_passed * 7

        self._ship.frame = round(frame_check)

        if self._ship.frame > 7:
            animating = False


def handleAnimation(self, dt):
    """ Triggers and handles the animation coroutine for exploding ship """
    if shipDown(self):
        # Sound(self._soundList[0]).play()

        self._animator = animate_shipDown(self, dt)
        next(self._animator)

    if self._animator is not None:
        try:
            self._animator.send(dt)
        except:
            self._animator = None

            self._ship = None
            self._afterblast = True
            self._bolts.clear()

def keepScore(self):
    """ Updates the _score attribute after an alien dies/becomes None """
    total = 0

    for row in self._aliens:
        for alien in row:
            if alien is not None:
                total += 1
    self._score = SCORE_PER_ALIEN*((ALIENS_IN_ROW*ALIEN_ROWS)-total)

def checkFailure(self):
    """ Checks if game failure/win conditions are met """
    if aliensAnnihilated(self):
        self._winLoseThemes[0].play()
        self.aliens_annihilated = True

    if aliensBreach(self):
        self._winLoseThemes[1].play()
        self.aliens_breach = True

    if self._lives == 0:
        self._winLoseThemes[1].play()



class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts
    on screen. It animates the laser bolts, removing any aliens as necessary.
    It also marches the aliens back and forth across the screen until they are
    all destroyed or they reach the defense line (at which point the player
    loses). When the wave is complete, you  should create a NEW instance of
    Wave (in Invaders) if you want to make a new wave of aliens.

    If you want to pause the game, tell this controller to draw, but do not
    update.  See subcontrollers.py from Lecture 24 for an example.  This
    class will be similar to than one in how it interacts with the main class
    Invaders.

    All of the attributes of this class ar to be hidden. You may find that
    you want to access an attribute in class Invaders. It is okay if you do,
    but you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter
    and/or setter for any attribute that you need to access in Invaders.
    Only add the getters and setters that you need for Invaders. You can keep
    everything else hidden.

    """
    # HIDDEN ATTRIBUTES:
    # Attribute _ship: the player ship to control
    # Invariant: _ship is a Ship object or None
    #
    # Attribute _aliens: the 2d list of aliens in the wave
    # Invariant: _aliens is a rectangular 2d list containing Alien objects or None
    #
    # Attribute _bolts: the laser bolts currently on screen
    # Invariant: _bolts is a list of Bolt objects, possibly empty
    #
    # Attribute _dline: the defensive line being protected
    # Invariant : _dline is a GPath object
    #
    # Attribute _lives: the number of lives left
    # Invariant: _lives is an int >= 0
    #
    # Attribute _time: the amount of time since the last Alien "step"
    # Invariant: _time is a float >= 0s
    #
    # You may change any attribute above, as long as you update the invariant
    # You may also add any new attributes as long as you document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    #
    # Attrbute _direction: the current movement direction of the alien brigade
    # Invariant: _direction is a int in [0, 1], 0 means right, 1 means left
    #
    # Attrbute _alien_fireRate: the number of steps until an alien can fire a bolt
    # Invariant: _alien_fireRate is a int between 1 and BOLT_RATE
    #
    # Attrbute steps: the number of alien steps since last alien bolt was fired
    # Invariant: steps is an int between 1 and _alien_fireRate
    #
    # Attrbute _animator: A coroutine for perfoming an animation sequence
    # Invariant: _animator is a generator or None
    #
    # Attrbute aliens_annihilated: Tells if all aliens are dead or not
    # Invariant: aliens_annihilated is a boolean
    #
    # Attrbute aliens_breach: Tells if an alien is below defense line
    # Invariant: aliens_breach is a boolean
    #
    # Attrbute _soundList: List of game sounds
    # Invariant: _soundList a non_empty list
    #
    # Attrbute _score: player score
    # Invariant: _score is an int
    #
    # Attribute _winLoseThemes: sounds that play if you win or lose
    # Invariant: _winLoseThemes list of Sound objects
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getAliens(self):
        """ Return self._aliens (the array of alien objects) """
        return self._aliens


    def getShipStateA(self):
        """ Returns True if self._ship is None else False """
        if self._animator is not None and self._afterblast == True:
            pass
        elif self._ship == None:
            return True
        return False

    def getLives(self):
        """ Returns self._lives (how many lives the player has left) """
        return self._lives


    def getAnnihilation(self):
        """ Returns self.aliens_annihilated (a boolean telling if all aliens are None or not) """
        return self.aliens_annihilated


    def getBreach(self):
        """ Returns self._aliens_breach (a boolean telling if the aliens have breached the defense line) """
        return self.aliens_breach

    def getScore(self):
        """ Return the score of the player """
        return self._score

    def setShip(self):
        """ created a new ship object and assigns it to self._ship """
        if self._ship == None:
            self._ship = makeShip()

    def setLives(self, i):
        """ deducts i amount of lives from self._lives """
        self._lives -= i

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        """ Initilizer for Wave object """
        self._aliens = makeAlienList()
        self._ship = makeShip()
        self._dline = makeDLine()
        self._bolts = []
        self._time = 0
        self._direction = 0
        self._alien_fireRate = random.randint(1,10)
        self.steps = 0
        self._animator = None
        self._lives = 3
        self.aliens_annihilated = False
        self.aliens_breach = False
        self._afterblast = False
        self._soundList = [BLAST, SHIP_PEW, ALIEN_PEW, POP]
        self._gameBackground = GImage(x=GAME_WIDTH/2,
                                      y=GAME_HEIGHT/2,
                                      width = 3*GAME_WIDTH/2,
                                      height = GAME_HEIGHT,
                                      source = GAME_BACKGROUND)
        self._score = 0
        self._winLoseThemes = [Sound("Win.mp3"), Sound("Lose.mp3")]

    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, input, dt, lastkeys):
        """ Update function for wave animation frames """
        # self._time += dt
        shipMovements(self, input, dt)
        alienMovements(self)
        boltMovements(self)
        alienFire(self)
        alienDown(self)
        handleAnimation(self, dt)
        checkFailure(self)
        keepScore(self)

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self, view):
        """ Draw function for wave frames """
        self._gameBackground.draw(view)

        GLabel(text="Lives: {}            Score: {}".format(self._lives, self._score),
                            font_size=50,
                            font_name = 'Arcade.ttf',
                            x = GAME_WIDTH/2,
                            y = GAME_HEIGHT - GAME_HEIGHT/15,

                            linecolor="yellow").draw(view)


        if self._aliens is not None:
            for row in self._aliens:
                for alien in row:
                    if alien is not None:
                        alien.draw(view)

        for bolt in self._bolts:
            bolt.draw(view)

        self._dline.draw(view)

        if self._ship is not None:
            self._ship.draw(view)

    # HELPER METHODS FOR COLLISION DETECTION
