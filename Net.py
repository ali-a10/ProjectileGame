from re import X


import pygame

class Net:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.net_png = pygame.transform.scale(pygame.image.load(
            'images/rim.png'), (83, 65))
        self.height = self.net_png.get_height()
        self.width = self.net_png.get_width()


    def get_rim_line(self) -> None:
        ''' this is the line that the ball can go in from
        first element of the tuple is the start of line 
        second element of the tuple is the end of line '''
        return ((self.x+6, self.y), 
        (self.x + self.net_png.get_width() - 6, self.y))
