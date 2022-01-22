from typing import Tuple
import pygame
from Ball import *
from Net import *

pygame.init()

# window
win_width = 1000
win_length = 520
window = pygame.display.set_mode((win_width, win_length))
pygame.display.set_caption("Make the Shot Game")

###  MAKE a SHOOTER CLASS?

ball = Ball(60, 300)
net = Net(800, 150)
bg = pygame.transform.scale(pygame.image.load('images/courtbg.png'), (1000, 520))


def redraw_window(shot_time: Tuple[int], time: float) -> None:
    window.blit(bg, (0, 0))
    window.blit(net.net_png, (net.x, net.y))

    ball.shoot(time, 65, math.pi/4)  #USE /3, /4, /6 
    # print(time, ball.x, ball.y)
    window.blit(ball.ball_png, (ball.x, ball.y))

    # top box
    pygame.draw.rect(window, (255, 215, 0), (0, 0, win_width, 69))
    # top box's border
    pygame.draw.rect(window, (255, 255, 255), (2, 2, win_width - 4, 70), 5)    
    pygame.display.update()