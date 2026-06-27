import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('pygame\Space_Shooter\Sprites\spaceShips_007.png').convert_alpha()
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image ,(50,50)) , 180)
        self.rect = self.image.get_rect(center = (540,600))
        self.player_speed = 7
    
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.right -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.left += self.player_speed 
        if keys[pygame.K_UP]:
            self.rect.bottom -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.rect.top += self.player_speed

    def player_wall_collisions(self):
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600: 
            self.rect.bottom = 600


    def update(self):
        self.player_input()
        self.player_wall_collisions()