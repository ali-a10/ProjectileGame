import pygame

class Ball:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.ball_png = pygame.image.load('images/ball.png')
        self.diameter = self.ball_png.get_height()

    def shoot(self, angle) -> None: # might add power
        pass
