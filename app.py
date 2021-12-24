from consts import *
from game2d import *
from wave import *
from models import *
import random
import pprint


class Pytrix(GameApp):

    def start(self):
        self.time = 0
        self.piece = self.pick_a_piece()
        self.last_keys = ()
        self.lines = []
        self.background = GRectangle(
            x=GAME_WIDTH/2, y=GAME_HEIGHT/2, width=GAME_WIDTH, height=GAME_HEIGHT, fillcolor='black')
        self.board = [[None for i in range(GAME_WIDTH//30)]
                      for j in range(GAME_HEIGHT//30)]
        grid(self)

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
        print(self.piece)
        self.time += dt
        move(self)
        if self.piece.canDrop(collapse_board(self)):
            if self.time > 0.8:
                for item in self.piece.blocks:
                    item.y -= BLOCK_LENGTH
                self.time = 0
                self.piece.current_y -= BLOCK_LENGTH
        else:
            for block in self.piece.blocks:
                row = GAME_HEIGHT//BLOCK_LENGTH - (block.top//BLOCK_LENGTH)
                column = block.left//BLOCK_LENGTH
                self.board[int(row)][int(column)] = block
            self.piece = self.pick_a_piece()
            self.clearRows()

        
        pp = pprint.PrettyPrinter()
        pp.pprint(self.board)
        print('\n')

    def draw(self):
        self.background.draw(self.view)
        for line in self.lines:
            line.draw(self.view)
        for row in self.board:
            for item in row:
                if item is not None:
                    item.draw(self.view)
        for item in self.piece.blocks:
            item.draw(self.view)
    
    def clearRows(self):
        new_board = []
        for row in self.board:
            full = all([item is not None for item in row])
            if full:
                for above_row in new_board:
                    for above_item in above_row:
                        if above_item is not None:
                            above_item.y -= BLOCK_LENGTH
            else:
                new_board.append(row)
        rows_to_add = len(self.board) - len(new_board)
        for _ in range(rows_to_add):
            new_board.insert(0,[None for _ in range(GAME_WIDTH//BLOCK_LENGTH)])
        self.board = new_board

# Helper functions


def move(self):
    if 'right' in self.input.keys and self.piece.canMoveRight(collapse_board(self)) and self.last_keys == ():
        for item in self.piece.blocks:
            item.x += BLOCK_LENGTH
        self.piece.current_x += BLOCK_LENGTH
    if 'left' in self.input.keys and self.piece.canMoveLeft(collapse_board(self)) and self.last_keys == ():
        for item in self.piece.blocks:
            item.x -= BLOCK_LENGTH
        self.piece.current_x -= BLOCK_LENGTH
    if 'down' in self.input.keys and self.piece.canDrop(collapse_board(self)) and self.last_keys == ():
        for item in self.piece.blocks:
            item.y -= BLOCK_LENGTH
        self.piece.current_y -= BLOCK_LENGTH
    if 'up' in self.input.keys and self.last_keys == ():
        if (self.piece.canRotate(collapse_board(self), self.piece.get_next_orientation())):
            self.piece.rotate()

    self.last_keys = self.input.keys


def grid(self):
    vert_lines = GAME_WIDTH//30
    horz_lines = GAME_HEIGHT//30

    for i in range(vert_lines):
        self.lines.append(GPath(points=(30*(i), 0, 30*(i), GAME_HEIGHT),
                                linewidth=1,
                                linecolor="gray"))
    for i in range(int(horz_lines)):
        self.lines.append(GPath(points=(0, 30*(i+1), GAME_WIDTH, 30*(i+1)),
                                linewidth=1,
                                linecolor="gray"))


def collapse_board(self):
    return [item for row in self.board for item in row if item is not None]
