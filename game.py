import pygame
from params import Params
import logic
from game_drawer import GameDrawer1
import sys
pygame.font.init()




class Game:

    def __init__(self):
        self.screen = Params.SCREEN
        self.run = False
        self.drawer = GameDrawer1
        self.logic = logic.GameLogic()

    def draw_game(self, screen):
        self.drawer.draw_background(screen)
        self.drawer.draw_grid(self.screen)
        self.drawer.draw_block(self.logic.actual_block, self.screen)
        self.drawer.draw_dead_blocks(self.screen, self.logic.board, self.logic.color_board)
        self.drawer.draw_next_shape(self.screen, self.logic.next_block)

    def update_game_logic(self):
        if self.logic.check_defeat():
            self.run = False

        self.logic.update_game(self)

    def run_game(self):
        self.run = True

        while self.run:
            return_value = "loose"
            Params.CLOCK.tick(Params.FPS)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.logic.move_left(self.logic.actual_block)
                    if event.key == pygame.K_RIGHT:
                        self.logic.move_right(self.logic.actual_block)
                    if event.key == pygame.K_SPACE:
                        self.logic.rotate(self.logic.actual_block)
                    if event.key == pygame.K_r:
                        self.run = False
                        return_value = "restart"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.logic.speed_up()

            self.update_game_logic()
            self.draw_game(self.screen)

            pygame.display.update()

        return return_value
