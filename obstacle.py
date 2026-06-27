import pygame 
import random 

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,speed_x = 0,speed_y =0):
        super().__init__()
        self.image = pygame.image.load('pygame\Space_Shooter\Sprites\spaceMeteors_002.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image ,random.randint(0,360),random.uniform(0.2, 0.344))    
        self.rect = self.image.get_rect(center = (x,y))
        self.obstacle_angle = 0
        self.radius = self.rect.width // 2
        self.speed_x = speed_x
        self.speed_y = speed_y

    def obstacle_movement(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

    
    def destroy_obstacle(self):
        if self.rect.bottom > 700 or self.rect.right < -10 or self.rect.left > 1100:
            self.kill()

    def rotate_obstacle(self):
        self.obstacle_angle += 5 
        self.rotated_surface = self.image 
        self.rotated_surface = pygame.transform.rotate(self.rotated_surface,self.obstacle_angle)
        self.rotated_rect = self.rotated_surface.get_rect(center = (random.randint(0,1000),110))
    
    def update(self):
        self.obstacle_movement()
        self.destroy_obstacle()
        self.rotate_obstacle()