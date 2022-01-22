from typing import Tuple
import pygame
from Ball import *
from Net import *
from Shooter import Shooter

pygame.init()

# window
win_width = 1000
win_length = 520
window = pygame.display.set_mode((win_width, win_length))
pygame.display.set_caption("Make the Shot Game")

###  MAKE a SHOOTER CLASS?

ball = Ball(60, 300)
net = Net(800, 150)
shooter = Shooter(20, win_length - 178)
bg = pygame.transform.scale(pygame.image.load('images/court1.png'), 
(1000, 500))
net_xboundary = 770
net_yboundary = 75
score_font = pygame.font.SysFont('arial', 25, True, True)


def redraw_window(shot_time: int, time: float, score: int) -> None:
    window.blit(bg, (0, 70))
    pygame.draw.line(window, (255, 255, 255), (net_xboundary, 0), 
                    (net_xboundary, win_length))

    # rim_line = net.get_rim_line()
    shooting_png = shooter.nextPNG()
    # print(shooting_png)
    window.blit(shooting_png[0], (20, win_length - shooting_png[0].get_height()
    - shooting_png[1]))

    if shooting_png[0] == shooter.listof_pngs[2]:
        ball.in_air = True
        # print("111111111")
        
    if not ball.in_air:
        # print("22222222222")
        shooter.is_shooting = True

    if ball.in_air:  # or not scored
        if ball.is_scored:
            # window.blit(pygame.transform.scale(pygame.image.load('images/score.PNG'), 
            # (100, 70)), (ball.x, ball.y))
            pass
        else:
            if shooting_png[0] == shooter.listof_pngs[0]:
                shooter.is_shooting = False
                if ball.x > ball.starting_x + 20:
                    ball.shoot(time, 60, math.pi/4)  #USE /3, /4, /6
                    window.blit(ball.ball_png, (ball.x, ball.y))
            
            else:
                ball.shoot(time, 60, math.pi/4)  #USE /3, /4, /6
                window.blit(ball.ball_png, (ball.x, ball.y))

#         # if ball is scored
#         if rim_line[0][0] <= ball.x <= rim_line[1][0] and\
#         rim_line[0][1] <= ball.y + ball.diameter/2 <= rim_line[0][1]+15:
#             print('BUCKET')
#             ball.in_air = False
#             window.blit(pygame.transform.scale(pygame.image.load('images/score.PNG'), 
# (100, 70)), (ball.x, ball.y))
            
    # top box
    pygame.draw.rect(window, (0, 0, 0), (0, 0, win_width, 69))
    # top box's border
    pygame.draw.rect(window, (255, 255, 255), (2, 2, win_width - 4, 70), 5) 

    # score
    score_text = score_font.render('Score = ' + str(score), 1, (255, 255, 255))
    window.blit(score_text, (660, 20))
    
    window.blit(net.net_png, (net.x, net.y))
    # pygame.draw.line(window, (255, 255, 255), rim_line[0], rim_line[1])


    pygame.display.update()