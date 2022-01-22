from redraw_func import *

time = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        net.x -= 4

    if keys[pygame.K_RIGHT] and net.x + net.width < win_width:
        net.x += 4         # might have to add 4 ^^

    if keys[pygame.K_DOWN] and net.y + net.height < win_length:
        net.y += 4         # might have to add 4 ^^

    if keys[pygame.K_UP] and net.y > 4:
        net.y -= 4

    if ball.in_air:
        time += 0.3
    # increase time as level increases

    shooter.nextPNG()

    if time > 25 or not ball.in_air:
        time = 0
    redraw_window(0, time)