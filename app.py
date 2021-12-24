from consts import *
from game2d import *
from wave import *
from models import *
import random
import pprint


class Pytrix(GameApp):

    def start(self):
        self.state = STATE_ACTIVE
        self.number_of_lines = 0
        self.level = 1
        self.time = 0
        self.piece = self.pick_a_piece()
        self.last_keys = ()
        self.lines = []
        self.background = GRectangle(
            x=BOARD_WIDTH/2, y=GAME_HEIGHT/2, width=BOARD_WIDTH, height=GAME_HEIGHT, fillcolor='black')
        self.board = [[None for i in range(BOARD_WIDTH//30)]
                      for j in range(GAME_HEIGHT//30)]
        self.scorepane = GRectangle(
            x=3*BOARD_WIDTH/2, y=GAME_HEIGHT/2, width=BOARD_WIDTH, height=GAME_HEIGHT, fillcolor='gray')
        self.text = None
        self.score = 0
        self.lines_cleared = 0
        self.next_piece = self.pick_a_piece(
            3*GAME_WIDTH/4, GAME_HEIGHT/5)
        self.next_piece_window = GRectangle(
            x=3*GAME_WIDTH/4, y=GAME_HEIGHT/5 - BLOCK_LENGTH, width=6*BLOCK_LENGTH, height=4*BLOCK_LENGTH, fillcolor='black')

        grid(self)

    def pick_a_piece(self, init_x=BOARD_WIDTH/2, init_y=GAME_HEIGHT):
        number = random.randint(0, 6)
        prefixes = {0:"O",1:"L",2:"Z",3:"I",4:"J",5:"T",6:"S"}
        return eval(f"{prefixes[number]}Piece({init_x}, {init_y})")

    def update(self, dt):
        if self.state == STATE_ACTIVE:
            print(self.piece)
            self.time += dt
            adjusted_speed = BASE_SPEED / (self.level)
            if 's' in self.input.keys and self.last_keys == ():
                self.state = STATE_PAUSED

            move(self)
            if self.piece.canDrop(collapse_board(self)):
                if self.time > adjusted_speed:
                    for item in self.piece.blocks:
                        item.y -= BLOCK_LENGTH
                    self.time = 0
                    self.piece.current_y -= BLOCK_LENGTH
            else:
                if self.time > adjusted_speed:
                    for block in self.piece.blocks:
                        row = GAME_HEIGHT//BLOCK_LENGTH - \
                            (block.top//BLOCK_LENGTH)
                        column = block.left//BLOCK_LENGTH
                        self.board[int(row)][int(column)] = block

                    self.time = 0
                    self.clearRows()

                    self.piece = eval(
                        f"{self.next_piece.__class__.__name__}()")
                    self.next_piece = self.pick_a_piece(
                        3*GAME_WIDTH/4, GAME_HEIGHT/5)

                    # self.next_piece.current_x, self.next_piece.current_y =
                    if top_out(self, collapse_board(self), self.piece.blocks):
                        self.state = STATE_END

            pp = pprint.PrettyPrinter()
            pp.pprint(self.board)
            print('\n')
            print(self.state, self.last_keys, self.input.keys)
            print('\n')

        elif self.state == STATE_PAUSED:
            if 's' in self.input.keys and self.last_keys == ():
                self.state = STATE_ACTIVE

        elif self.state == STATE_END:
            self.text = GLabel(text="Game\nOver",
                               font_size=50,
                               font_name='Arcade.ttf',
                               x=GAME_WIDTH/4,
                               y=GAME_HEIGHT/2,
                               linecolor="green")
        self.last_keys = self.input.keys

    def draw(self):
        self.background.draw(self.view)

        for line in self.lines:
            line.draw(self.view)

        for row in self.board:
            for item in row:
                if item is not None:
                    item.draw(self.view)
        if not top_out(self, collapse_board(self), self.piece.blocks):
            for item in self.piece.blocks:
                item.draw(self.view)

        self.scorepane.draw(self.view)
        GLabel(text=f"Score:\n{self.score}\n\nLines:\n{self.lines_cleared}\n\nLevel:\n{self.level}",
               font_size=50,
               font_name='Arcade.ttf',
               x=3*GAME_WIDTH/4,
               y=3*GAME_HEIGHT/5,
               linecolor="yellow").draw(self.view)

        self.next_piece_window.draw(self.view)

        for item in self.next_piece.blocks:
            item.draw(self.view)

        if top_out(self, collapse_board(self), self.piece.blocks) and self.text is not None:
            self.text.draw(self.view)

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
        self.lines_cleared += rows_to_add

        if rows_to_add == 1:
            self.score += 100*self.level
        elif rows_to_add == 2:
            self.score += 300 * self.level
        elif rows_to_add == 3:
            self.score += 500*self.level
        elif rows_to_add == 4:
            self.score += 800*self.level

        self.number_of_lines += rows_to_add
        self.level = (self.number_of_lines // LEVELS_TO_UPGRADE) + 1
        for _ in range(rows_to_add):
            new_board.insert(
                0, [None for _ in range(BOARD_WIDTH//BLOCK_LENGTH)])
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

    if 'spacebar' in self.input.keys and self.last_keys == ():
        while self.piece.canDrop(collapse_board(self)):
            for item in self.piece.blocks:
                item.y -= BLOCK_LENGTH
            self.piece.current_y -= BLOCK_LENGTH


def grid(self):
    vert_lines = BOARD_WIDTH//30
    horz_lines = GAME_HEIGHT//30

    for i in range(vert_lines):
        self.lines.append(GPath(points=(30*(i), 0, 30*(i), GAME_HEIGHT),
                                linewidth=1,
                                linecolor="gray"))
    for i in range(int(horz_lines)):
        self.lines.append(GPath(points=(0, 30*(i+1), BOARD_WIDTH, 30*(i+1)),
                                linewidth=1,
                                linecolor="gray"))


def collapse_board(self):
    return [item for row in self.board for item in row if item is not None]


def top_out(self, done, tentative_blocks):
    if any([any([done_block.x == block.x and done_block.y == block.y for done_block in done]) for block in tentative_blocks]):
        self.state = STATE_END
        return True
    return False

