from redraw_func import *

time = 0
clock = pygame.time.Clock()

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
        time += 0.3
    # increase time as level increases

    if time > 25 or not ball.in_air:
        time = 0
    redraw_window(0, time)