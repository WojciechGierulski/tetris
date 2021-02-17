import pygame
import sys
from params import Params, Colors


class Animations:

    def __init__(self):
        self.animation_speed = 1  # the lower number the faster animation
        self.run = False
        self.variables = {"explosion_width": 0, "explosion_height": 0,
                          "max_explosion_width": 10 * Params.SQUARE_SIZE + 9 * Params.LINE_WIDTH,
                          "max_explosion_height": Params.SQUARE_SIZE, "frame_nr": self.animation_speed,
                          "width_gain_speed": 20, "height_gain_speed": 4, "animation_nr": 1}

    def draw_frame(self, screen, row_nr):
        if "x_middle" not in self.variables:
            self.variables["x_middle"] = Params.WIN_SIZE[0] // 2
        if "y_row" not in self.variables:
            self.variables["y_row"] = Params.WIN_SIZE[1] - (
                    Params.SQUARE_SIZE * (20 - row_nr - 0.5) + Params.LINE_WIDTH * (20 - row_nr))

        if self.variables["frame_nr"] == self.animation_speed:
            self.variables["frame_nr"] = 0

            if self.variables["animation_nr"] == 1:
                self.variables["explosion_width"] = min(
                    self.variables["explosion_width"] + self.variables["width_gain_speed"],
                    self.variables["max_explosion_width"])
                self.variables["explosion_height"] = min(
                    self.variables["explosion_height"] + self.variables["height_gain_speed"],
                    self.variables["max_explosion_height"])
        else:
            self.variables["frame_nr"] += 1

        pygame.draw.rect(screen, Colors.white, (
            self.variables["x_middle"] - self.variables["explosion_width"] // 2,
            self.variables["y_row"] - self.variables["explosion_height"] // 2,
            self.variables["explosion_width"], self.variables["explosion_height"]))

    def check_if_done(self, clear_row_function, row_nr):
        if self.variables["explosion_width"] == self.variables["max_explosion_width"]:
            clear_row_function(row_nr)
            return True

        return False

    def reset(self):
        self.variables["explosion_width"] = 0
        self.variables["explosion_height"] = 0
        self.variables["frame_nr"] = self.animation_speed
        self.variables.pop("x_middle", None)
        self.variables.pop("y_row", None)

    def play_row_delete_animation(self, screen, row_nr, clear_row_function, game):
        self.run = True
        while self.run:
            Params.CLOCK.tick(Params.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

            if not self.check_if_done(clear_row_function, row_nr):
                game.draw_game(game.screen)
                self.draw_frame(screen, row_nr)
            else:
                self.reset()
                self.run = False

            pygame.display.update()


animation_player = Animations()
