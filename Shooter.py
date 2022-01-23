from numpy import index_exp
import pygame
import random

class Shooter:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.is_shooting = False
        self.is_standing = True
        self.png_count = 0
        self.listof_pngs = [
            pygame.image.load('images/shoot1.png'),
            pygame.image.load('images/shoot2.png'),
            pygame.image.load('images/shoot3.png'),
            pygame.image.load('images/shoot4.png'),
            pygame.image.load('images/shoot5.png'),
            ]
        self.nextShot = False
        
    def nextPNG(self):  # -> Tuple:
        self.png_count += 2
        if self.png_count > 52:
            self.png_count = 0
        
        if not self.is_shooting:
            self.is_standing = True
            return self.listof_pngs[0], 0
        else:
            if self.png_count < 30:
                self.is_standing = True
                return self.listof_pngs[0], 0

            elif self.png_count < 35:
                self.is_standing = False
                return self.listof_pngs[1], 6

            elif self.png_count < 40:
                self.is_standing = False
                return self.listof_pngs[2], 12

            elif self.png_count < 45:
                self.is_standing = False
                return self.listof_pngs[3], 14

            else:
                self.is_standing = False
                return self.listof_pngs[4], 5

    def chooseShot(self) -> None: ## CHANGE THE NONE
        angles = [2.5, 5]#3, 4, 5]
        index_chosen = random.randint(0,1)
        angle_chosen = angles[index_chosen]

        if index_chosen == 0:
            power = 80
            time = 34
        elif index_chosen == 1:
            power = random.randint(62, 72)
            time = 30
        elif index_chosen == 2:
            power = random.randint(55, 68)
            time = 25
        else:
            power = random.randint(60, 70)
            time = 25
        
        return [angle_chosen, power, time]
        


