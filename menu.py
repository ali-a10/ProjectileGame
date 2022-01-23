from redraw_func import *

clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('images/court1.png'), 
(1000, 520))

def main_menu():
    menu = True
    close = False

    while menu:
        window.blit(bg, (0, 0))
        menu_font = pygame.font.SysFont('Agency FB', 100, True)
        inst_font = pygame.font.SysFont('Agency FB', 40, True)
        press_space1 = menu_font.render('Press Space to Start', 1,
                                        (255, 255, 255))
        inst_title = menu_font.render('Instructions', 1, (5, 14, 166))
        instructions1 = inst_font.render('Use arrows to move', 1, (5, 14, 166))
        
        window.blit(press_space1, (150, 75))
        pygame.draw.rect(window, (255, 255, 255), (0, 208, win_width, 4))
        window.blit(inst_title, (288, 350))
        window.blit(instructions1, (365, 460))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False

        pygame.display.update()
        clock.tick(5)
    if close:
        return False
    return True

def game_over():
    over = True

    while over:
        pygame.draw.rect(window, (0, 0, 0), (140, 90, 720, 370))
        pygame.draw.rect(window, (255, 255, 255), (150, 100, 700, 350))
        over_font = pygame.font.SysFont('Agency FB', 120, True)
        instruc_font = pygame.font.SysFont('Agency FB', 80, True)
        over_text = over_font.render('GAME OVER', 1, (0, 255, 0))
        press_r = instruc_font.render('Press R to Restart', 1,
                                      (0, 255, 0))

        window.blit(over_text, (275, 100))
        window.blit(press_r, (260, 270))
        window.blit(pygame.transform.scale(pygame.image.load(
            "images/xmark.png"), (55, 55)), (200, 10))

        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                over = False
                pygame.quit()

            if event1.type == pygame.KEYDOWN:
                if event1.key == pygame.K_r:
                    player.lives = 0
                    player.score = 0
                    over = False

        clock.tick(5)
        pygame.display.update()