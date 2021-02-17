from params import Colors, Params
import pygame
import copy


class GameDrawer:

    def __init__(self, params):
        self.params = params

    def draw_background(self, screen):
        screen.fill(Colors.black)

    def get_spot_cords(self, x, y):
        middle = self.params.WIN_SIZE[0] // 2
        x0 = middle - 5 * (self.params.LINE_WIDTH + self.params.SQUARE_SIZE)
        y0 = self.params.WIN_SIZE[1] - 21 * self.params.LINE_WIDTH - 20 * self.params.SQUARE_SIZE

        return x0 + self.params.LINE_WIDTH + x * (
                self.params.SQUARE_SIZE + self.params.LINE_WIDTH), y0 + self.params.LINE_WIDTH + y * (
                       self.params.SQUARE_SIZE + self.params.LINE_WIDTH)

    def draw_block(self, block, screen):
        for x in range(block.size):
            for y in range(block.size):
                if x + block.row >= 0:
                    if block.type[block.rotation][x, y] == 1:
                        x0, y0 = self.get_spot_cords(y + block.col - 1, x + block.row)
                        pygame.draw.rect(screen, block.color,
                                         pygame.Rect(x0, y0, self.params.SQUARE_SIZE, self.params.SQUARE_SIZE))

    def draw_dead_blocks(self, screen, board, color_board):
        for x in range(board.shape[0]):
            for y in range(board.shape[1]):
                if board[x, y] == 1:
                    x0, y0 = self.get_spot_cords(y - 1, x)
                    pygame.draw.rect(screen, color_board[x, y], pygame.Rect(x0, y0, self.params.SQUARE_SIZE, self.params.SQUARE_SIZE))

    def draw_next_shape(self, screen, block):
        text = self.params.FONT.render('Next Shape:', True, (255, 255, 255))
        screen.blit(text, (0.74 * self.params.WIN_SIZE[0], 0.2 * self.params.WIN_SIZE[1]))
        b1 = copy.deepcopy(block)
        b1.row = 4
        b1.col = 13
        if b1.type_nr == 1:
            b1.col -= 1
        if b1.type_nr == 4:
            b1.col += 1
        self.draw_block(b1, screen)


    def draw_grid(self, screen):
        # Vertical
        middle = self.params.WIN_SIZE[0] // 2
        cursor = middle - 5 * (self.params.LINE_WIDTH + self.params.SQUARE_SIZE)
        line_height = 21 * self.params.LINE_WIDTH + 20 * self.params.SQUARE_SIZE

        for x in range(11):
            pygame.draw.line(screen, Colors.gray, (cursor, self.params.WIN_SIZE[0]),
                             (cursor, self.params.WIN_SIZE[1] - line_height),
                             self.params.LINE_WIDTH)
            cursor += self.params.LINE_WIDTH + self.params.SQUARE_SIZE

        # Horizontal
        cursor_x = middle - 5 * (self.params.LINE_WIDTH + self.params.SQUARE_SIZE)
        cursor_y = self.params.WIN_SIZE[1] - self.params.LINE_WIDTH
        line_height = 10 * self.params.LINE_WIDTH + 10 * self.params.SQUARE_SIZE

        for x in range(21):
            pygame.draw.line(screen, Colors.gray, (cursor_x, cursor_y), (cursor_x + line_height, cursor_y),
                             self.params.LINE_WIDTH)
            cursor_y -= self.params.LINE_WIDTH + self.params.SQUARE_SIZE


GameDrawer1 = GameDrawer(Params)
