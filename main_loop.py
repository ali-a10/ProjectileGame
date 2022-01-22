import time
from redraw_func import *

ball_time = 0
clock = pygame.time.Clock()
waiting = False
score = 0

run = True
while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and net.x > net_xboundary + 4:
        net.x -= 4

    if keys[pygame.K_RIGHT] and net.x + net.width < win_width - 4:
        net.x += 4

    if keys[pygame.K_DOWN] and net.y + net.height < win_length:
        net.y += 4

    if keys[pygame.K_UP] and net.y > net_yboundary + 4:
        net.y -= 4


    shooter.nextPNG()

    if ball.in_air:
        ball_time += 0.3
    # increase time as level increases

    if ball_time > 25 or not ball.in_air:
        ball_time = 0

    rim_line = net.get_rim_line()
    # if ball is scored
    if rim_line[0][0] <= ball.x <= rim_line[1][0] and\
        rim_line[0][1] <= ball.y + ball.diameter/2 <= rim_line[0][1]+15:
        ball.in_air = False
        ball.is_scored = True
        waiting = True
        score += 1

    if waiting: # only thing that's drawn is 'score'
        window.blit(pygame.transform.scale(pygame.image.load('images/score.PNG'), 
            (100, 70)), (net.x, net.y+70))
        pygame.display.update()
        time.sleep(0.75)

        waiting = False
        ball.is_scored = False
        ball.x = ball.starting_x
        ball.y = ball.starting_y
    else:
        redraw_window(0, ball_time, score)