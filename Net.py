from re import X


import pygame

class Net:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.net_png = pygame.transform.scale(pygame.image.load('images/net.png'), (100, round(100/0.582137161)))
        self.height = self.net_png.get_height()
        self.width = self.net_png.get_width()
