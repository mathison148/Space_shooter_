import pygame 


class Rocket(pygame.sprite.Sprite):
    def __init__(self ,x,y):
        super().__init__()
        self.image = pygame.image.load('pygame\Space_Shooter\Sprites\spaceMissiles_001.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,0.5)
        self.rect = self.image.get_rect(center = (x,y))
        self.rocket_speed = 10

    def rocket_motion(self):
        self.rect.y -= self.rocket_speed
        if self.rect.bottom < 0:
            self.kill()

    def update(self):
        self.rocket_motion()  