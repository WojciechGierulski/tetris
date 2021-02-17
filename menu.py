import pygame
from params import Params, Colors
import sys
from game import Game


class MenuDrawer:
    def __init__(self, screen):
        self.screen = screen

    def draw_start_screen(self):
        self.screen.fill(Colors.black)
        self.draw_centered_text("Press space to play")

    def draw_centered_text(self, text, color=(255, 255, 255)):
        text = Params.FONT_BIG.render(text, True, color)
        self.screen.blit(text, (
            Params.WIN_SIZE[0] // 2 - text.get_width() // 2, Params.WIN_SIZE[1] // 2 - text.get_height() // 2))



class Menu:
    def __init__(self):
        self.run = False
        self.screen = Params.SCREEN
        self.drawer = MenuDrawer(self.screen)
        self.game = Game()

    def reset_game(self):
        self.game = Game()

    def wait_for_space(self):
        self.run = True
        while self.run:

            Params.CLOCK.tick(Params.FPS)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.run = False

    def start_app(self):
        self.drawer.draw_start_screen()
        pygame.display.update()
        self.wait_for_space()

        while True:
            result = self.game.run_game()
            if result == "loose":
                self.drawer.draw_centered_text("You lost, press space to play again", Colors.red)
                pygame.display.update()
                self.wait_for_space()
                self.reset_game()
            elif result == "restart":
                self.reset_game()


menu = Menu()
menu.start_app()
