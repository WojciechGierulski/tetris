import pygame
pygame.font.init()


class Params:
    WIN_SIZE = (1000, 920)
    SCREEN = pygame.display.set_mode(WIN_SIZE)
    FPS = 30
    CLOCK = pygame.time.Clock()
    SQUARE_SIZE = 38
    LINE_WIDTH = 2
    FONT = pygame.font.SysFont('Comic Sans MS', 38)
    FONT_BIG = pygame.font.SysFont('Comic Sans MS', 60)


class Colors:
    black = (0, 0, 0)
    gray = (192, 192, 192)
    red = (255, 0, 0)
    pink = (255, 20, 147)
    yellow = (255, 255, 0)
    lightblue = (0, 191, 255)
    darkblue = (0, 0, 255)
    lightgreen = (0, 255, 0)
    darkgreen = (0, 100, 0)
    white = (255, 255, 255)
