import time
from redraw_func import *
from menu import *

ball_time = 0
clock = pygame.time.Clock()
waiting = False
shot = shooter.chooseShot()

menu = main_menu()
run = True
while run and menu:
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

    if ball.in_air:
        ball_time += 0.3

    if ball_time > shot[2] or not ball.in_air:
        ball_time = 0

    rim_line = net.get_rim_line()

    # if ball is scored
    if rim_line[0][0] <= ball.x <= rim_line[1][0] and\
        rim_line[0][1] <= ball.y + ball.diameter/2 <= rim_line[0][1]+20:
        ball.in_air = False
        ball.is_scored = True
        ball_time = 0
        waiting = True
        player.score += 1
        if player.score > player.high_score:
            player.high_score = player.score
        

    if waiting: # only thing that's drawn is 'score'
        window.blit(pygame.transform.scale(pygame.image.load('images/scoree.PNG'), 
            (120, 80)), (net.x-20, net.y-15))
        pygame.display.update()
        time.sleep(0.75)
        shot = shooter.chooseShot()

        waiting = False
        ball.is_scored = False
        ball.x = ball.starting_x
        ball.y = ball.starting_y
    else:
        if ball.ball_on_ground:  # ball hit the ground
            shot = shooter.chooseShot()
            player.lives += 1
            ball.ball_on_ground = False
            if player.lives == 3:
                player.score = 0
                ball.x = ball.starting_x
                ball.y = ball.starting_y
                game_over()

        redraw_window(ball_time, shot)
