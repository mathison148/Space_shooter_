import pygame

class Splash(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.image = pygame.image.load('pygame\Space_Shooter\Sprites\spaceEffects_016(splash).png')
        self.rect = self.image.get_rect(center = (x,y))
        self.timer = 15

    def timer_count(self):
       if self.timer == 0:
            self.kill()

    def update(self):
        self.timer_count()
        self.timer -= 1