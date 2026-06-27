import pygame 

class Star(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('pygame\Space_Shooter\Sprites\stars.png')
        self.image = pygame.transform.rotozoom(self.image,270,0.01)
        self.rect = self.image.get_rect(center = (x,y))

    def star_motion(self):
        self.rect.y += 2
        
        if self.rect.bottom >= 600:
            self.kill()

    def update(self):
        self.star_motion()   