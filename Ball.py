import math
from typing import Tuple
import pygame

class Ball:
    def __init__(self, x, y) -> None:
        self.starting_x = x
        self.starting_y = y
        self.x = x
        self.y = y
        self.ball_png = pygame.image.load('images/ball.png')
        self.diameter = self.ball_png.get_height()

    def shoot(self, time: float, power: int, angle) -> None:#Tuple[int]:  #whats the type for angle
        x_velocity = math.cos(angle) * power
        y_velocity = math.sin(angle) * power
        distance_X = x_velocity * time
        distance_Y = (y_velocity * time) + ((-4.9 * (time)**2)/2)

        # self.x += round(distance_X)
        # self.y -= round(distance_Y)
        self.x = round(distance_X + self.starting_x)
        self.y = round(self.starting_y - distance_Y)
        # return (round(distance_X + self.x), round(self.y - distance_Y))
