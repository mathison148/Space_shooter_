import pygame

class Effect(pygame.sprite.Sprite):
    def __init__(self,rocket:object):
        super().__init__()
        self.rocket = rocket 
        self.image = pygame.image.load('pygame\Space_Shooter\Sprites\spaceEffects_002(Thrust).png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.rocket.rect.centerx ,self.rocket.rect.bottom))
        self.effect_speed = 10

    def effect_motion(self):
        self.rect.y -= self.effect_speed
        if self.rect.bottom < 0:
            self.kill()

    def collision(self): #to destroy effect after rocket is destroy 
        if not self.rocket.alive():
            self.kill()
    
    def update(self): 
        self.effect_motion()
        self.collision()