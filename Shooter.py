import pygame

class Shooter:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.is_shooting = False
        self.png_count = 0
        self.listof_pngs = [
            pygame.image.load('images/shoot1.png'),
            pygame.image.load('images/shoot2.png'),
            pygame.image.load('images/shoot3.png'),
            pygame.image.load('images/shoot4.png'),
            pygame.image.load('images/shoot5.png'),
            ]
        
    def nextPNG(self):  # -> Tuple
        self.png_count += 0.2
        if self.png_count > 55:
            self.png_count = 0
        
        if not self.is_shooting:
            return self.listof_pngs[0], 0
        else:
            if self.png_count < 30:#15:
                return self.listof_pngs[0], 0

            elif self.png_count < 35:#20:
                return self.listof_pngs[1], 6

            elif self.png_count < 40:#25:
                return self.listof_pngs[2], 12

            elif self.png_count < 45:#30:
                return self.listof_pngs[3], 14

            else:
                return self.listof_pngs[4], 5
