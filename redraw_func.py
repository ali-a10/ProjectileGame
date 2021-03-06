from typing import List
import pygame
from Ball import *
from Net import *
from Shooter import Shooter
from User import User

pygame.init()

# window
win_width = 1000
win_length = 520
window = pygame.display.set_mode((win_width, win_length))
pygame.display.set_caption("Make the Shot Game")

player = User()
ball = Ball(60, 300)
net = Net(800, 150)
shooter = Shooter(20, win_length - 178)
bg = pygame.transform.scale(pygame.image.load('images/court1.png'), 
(1000, 500))
net_xboundary = 770
net_yboundary = 75
score_font = pygame.font.SysFont('arial', 25, True, True)


def redraw_window(time: float, shot: List[int]) -> None:
    window.blit(bg, (0, 70))
    pygame.draw.line(window, (255, 255, 255), (net_xboundary, 0), 
                    (net_xboundary, win_length))

    shooting_png = shooter.nextPNG()
    window.blit(shooting_png[0], (20, win_length - shooting_png[0].get_height()
    - shooting_png[1]))

    if shooting_png[0] == shooter.listof_pngs[2]:
        ball.in_air = True
    
    if not ball.in_air:
        shooter.is_shooting = True

    if ball.in_air:
        if ball.is_scored:
            pass
        else:
            if shooting_png[0] == shooter.listof_pngs[0]:
                shooter.is_shooting = False
                if ball.x > ball.starting_x + 20:
                    ball.shoot(time, shot[1], math.pi/shot[0])  
                    window.blit(ball.ball_png, (ball.x, ball.y))
            
            else:
                ball.shoot(time, shot[1], math.pi/shot[0])
                window.blit(ball.ball_png, (ball.x, ball.y))

            if ball.y + ball.diameter < 74:
                window.blit(pygame.transform.scale(pygame.image.load(
                    'images/arrow.png'), (45, 55)), (ball.x, 80))

            
    # top box
    pygame.draw.rect(window, (58, 58, 58), (0, 0, win_width, 69))
    # top box's border
    pygame.draw.rect(window, (255, 255, 255), (2, 2, win_width - 4, 70), 5) 

    # score
    score_text = score_font.render('Score = ' + str(player.score), 1, 
    (255, 255, 255))
    window.blit(score_text, (660, 20))
    high_text = score_font.render('High Score = ' + str(player.high_score),
    1, (255, 255, 255))
    window.blit(high_text, (825, 20))
    
    window.blit(pygame.transform.scale(pygame.image.load("images/ball2.png"), 
    (55, 55)), (50, 10))
    window.blit(pygame.transform.scale(pygame.image.load("images/ball2.png"), 
    (55, 55)), (125, 10))
    window.blit(pygame.transform.scale(pygame.image.load("images/ball2.png"), 
    (55, 55)), (200, 10))

    for i in range(player.lives):
        window.blit(pygame.transform.scale(pygame.image.load(
                    "images/xmark.png"), (55, 55)), (50 + i*75, 10))

    window.blit(net.net_png, (net.x, net.y))

    pygame.display.update()