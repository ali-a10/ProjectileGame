import pygame

class Ball:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        ball_png = pygame.image.load('images/ball.png')
        self.diameter = ball_png.get_height()

    def shoot(self, angle) -> None: # might add power
        pass
    