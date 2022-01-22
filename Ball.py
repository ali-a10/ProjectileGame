import math
from typing import Tuple
import pygame

class Ball:
    def __init__(self, x: int, y: int) -> None:
        self.starting_x = x
        self.starting_y = y
        self.x = x
        self.y = y
        self.ball_png = pygame.image.load('images/ball.png')
        self.diameter = self.ball_png.get_height()
        self.in_air = False
        self.is_scored = False
        self.counter = 0

    def shoot(self, time: float, power: int, angle) -> None:#Tuple[int]:  #whats the type for angle
        x_velocity = math.cos(angle) * power
        y_velocity = math.sin(angle) * power
        distance_X = x_velocity * time
        distance_Y = (y_velocity * time) + ((-4.9 * (time)**2)/2)
        self.x = round(distance_X + self.starting_x)
        self.y = round(self.starting_y - distance_Y)
        if self.y + self.diameter > 520:  # if ball hits the ground (520 = win_length)
            self.in_air = False
            self.x = self.starting_x
            self.y = self.starting_y
        # make if statement for if ball is scored

