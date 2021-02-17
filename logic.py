from params import Colors, Params
import random
import copy
import numpy as np
from animations import animation_player


class BlockCreator:
    types = {1, 2, 3, 4, 5, 6, 7}
    sizes = {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3}
    colors = [Colors.red, Colors.yellow, Colors.darkblue, Colors.lightblue, Colors.lightgreen, Colors.darkgreen,
              Colors.pink]

    def __init__(self):
        self.available = copy.copy(BlockCreator.types)

    def generate_block(self):
        if len(self.available) == 0:
            self.available = copy.copy(BlockCreator.types)
        color = BlockCreator.colors[random.randint(0, 6)]
        type_nr = random.sample(self.available, 1)[0]
        self.available.remove(type_nr)
        if type_nr == 1:
            type = Types.type1
        if type_nr == 2:
            type = Types.type2
        if type_nr == 3:
            type = Types.type3
        if type_nr == 4:
            type = Types.type4
        if type_nr == 5:
            type = Types.type5
        if type_nr == 6:
            type = Types.type6
        if type_nr == 7:
            type = Types.type7

        return Block(type, color, BlockCreator.sizes[type_nr], type_nr)


class Types:
    type1 = [None, None, None, None]
    type1[0] = np.array([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    type1[1] = np.array([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]])
    type1[2] = np.array([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    type1[3] = np.array([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]])

    type2 = [None, None, None, None]
    type2[0] = np.array([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
    type2[1] = np.array([[0, 1, 1], [0, 1, 0], [0, 1, 0]])
    type2[2] = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 1]])
    type2[3] = np.array([[0, 1, 0], [0, 1, 0], [1, 1, 0]])

    type3 = [None, None, None, None]
    type3[0] = np.array([[0, 0, 1], [1, 1, 1], [0, 0, 0]])
    type3[1] = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 1]])
    type3[2] = np.array([[0, 0, 0], [1, 1, 1], [1, 0, 0]])
    type3[3] = np.array([[1, 1, 0], [0, 1, 0], [0, 1, 0]])

    type4 = [None, None, None, None]
    type4[0] = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
    type4[1] = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
    type4[2] = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
    type4[3] = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

    type5 = [None, None, None, None]
    type5[0] = np.array([[0, 1, 1], [1, 1, 0], [0, 0, 0]])
    type5[1] = np.array([[0, 1, 0], [0, 1, 1], [0, 0, 1]])
    type5[2] = np.array([[0, 0, 0], [0, 1, 1], [1, 1, 0]])
    type5[3] = np.array([[1, 0, 0], [1, 1, 0], [0, 1, 0]])

    type6 = [None, None, None, None]
    type6[0] = np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]])
    type6[1] = np.array([[0, 1, 0], [0, 1, 1], [0, 1, 0]])
    type6[2] = np.array([[0, 0, 0], [1, 1, 1], [0, 1, 0]])
    type6[3] = np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0]])

    type7 = [None, None, None, None]
    type7[0] = np.array([[1, 1, 0], [0, 1, 1], [0, 0, 0]])
    type7[1] = np.array([[0, 0, 1], [0, 1, 1], [0, 1, 0]])
    type7[2] = np.array([[0, 0, 0], [1, 1, 0], [0, 1, 1]])
    type7[3] = np.array([[0, 1, 0], [1, 1, 0], [1, 0, 0]])


class Block:
    def __init__(self, type, color, size, type_nr):
        self.type = type
        self.color = color
        self.rotation = 1
        self.size = size
        self.row = -3
        self.col = 4
        self.type_nr = type_nr


class GameLogic:
    game_speed = 8  # Less means faster

    def __init__(self):
        self.board = np.zeros((23, 12))
        self.color_board = np.zeros((23, 12), dtype=(int, 3))
        self.board[20, :] = 1
        self.board[:, 0] = 1
        self.board[:, 11] = 1
        self.inner_clock = 5
        self.block_creator = BlockCreator()
        self.actual_block = self.block_creator.generate_block()
        self.next_block = self.block_creator.generate_block()

    def block_blocked(self, block):
        for x in range(block.size):
            for y in range(block.size):
                if block.type[block.rotation][x, y] == 1:
                    self.board[x + block.row, y + block.col] = 1
                    self.color_board[x + block.row, y + block.col] = block.color

        self.actual_block = self.next_block
        self.next_block = self.block_creator.generate_block()

    def move_block_down(self, block):
        block.row += 1
        b1 = copy.deepcopy(block)
        b1.row += 1
        if self.detect_collision(b1):
            return False

        return True

    def move_right(self, block):
        b1 = copy.deepcopy(block)
        b1.col += 1
        if not self.detect_collision(b1):
            block.col += 1

    def move_left(self, block):
        b1 = copy.deepcopy(block)
        b1.col -= 1
        if not self.detect_collision(b1):
            block.col -= 1

    def rotate(self, block):
        b1 = copy.deepcopy(block)
        b1.rotation += 1
        if b1.rotation == 4:
            b1.rotation = 0

        if not self.detect_collision(b1):
            block.rotation += 1
        if block.rotation == 4:
            block.rotation = 0

    def speed_up(self):
        self.inner_clock += 4

    def detect_collision(self, block):
        for row in range(block.size):
            for col in range(block.size):
                a = self.board[row + block.row, col + block.col]
                b = block.type[block.rotation][row, col]
                if a == 1 and b == 1:
                    return True
        return False

    def move_all_dead_down(self, start_row):
        for row in range(start_row, -1, -1):
            for col in range(10, 0, -1):
                if self.board[row, col] == 1:
                    self.board[row, col] = 0
                    self.board[row + 1, col] = 1
                    self.color_board[row + 1, col] = self.color_board[row, col]
                    self.color_board[row, col] = 0

    def clear_row(self, row):
        self.board[row, 1:11] = 0
        self.color_board[row, 1:11] = 0

    def check_defeat(self):
        if 1 in self.board[0, 4:7]:
            return True
        else:
            return False

    def check_full_row(self, game):
        for row in range(20):
            if 0 not in self.board[row, 1:11]:
                animation_player.play_row_delete_animation(Params.SCREEN, row, self.clear_row, game)
                self.move_all_dead_down(row)

    def update_game(self, game):
        self.check_full_row(game)

        self.inner_clock += 1
        if self.inner_clock >= GameLogic.game_speed:
            self.inner_clock = 0
            if not self.move_block_down(self.actual_block):
                self.block_blocked(self.actual_block)
