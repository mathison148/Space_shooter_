import pygame 
import sys 
import random 
from player import Player
from obstacle import Obstacle
from rocket import Rocket
from effect import Effect
from splash import Splash
from star import Star
from pattern import *


pygame.init() 
pygame.mixer.init()

#player collide against meteor
def player_collision ():

    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        player_collision_sound.play()
        return False 
    else:
        return True
        
def rocket_collision():
    pygame.sprite.groupcollide(rocket_group,obstacle_group,True,True)

#star_bg
def star_pattern_spawn():
    x = random.randint(0,900)
    y = random.randint(-100,-20)
    star_group.add(Star(x,y))

def splash_collision():
    global score_count

    collisions = pygame.sprite.groupcollide(
        rocket_group,
        obstacle_group,
        True,
        True
    )

    for rocket , obstacle_hit in collisions.items():
        score_count += len(obstacle_hit)
        for obstacle in obstacle_hit:
            collision_sound.play()
            splash_group.add(
                Splash(
                    obstacle.rect.centerx,
                    obstacle.rect.centery
                )
            )
    

    
#Screen
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Shooter")
running = True 
clock = pygame.time.Clock()
game_status = False

#Star Pattern
star_group = pygame.sprite.Group()
star_timer = pygame.USEREVENT + 1
pygame.time.set_timer(star_timer,100)

#Player
player = pygame.sprite.GroupSingle()
player.add(Player())

#Obstacle group
obstacle_group = pygame.sprite.Group()
obstacle_timer = pygame.USEREVENT + 2 
pygame.time.set_timer(obstacle_timer,4000)

#bullet group 
rocket_group = pygame.sprite.Group()
rocket_group.add(Rocket(player.sprite.rect.centerx , player.sprite.rect.top)) 
rocket_timer = pygame.USEREVENT + 3
pygame.time.set_timer(rocket_timer, 1000)

#Effect group 
effect_group = pygame.sprite.Group()

#Splash group 
splash_group = pygame.sprite.Group()


#score board 
font_style = pygame.font.SysFont('agencyfb',50)
score_count = 0 

#start_surface / start message  
start_surface = pygame.image.load('pygame/Space_Shooter/Sprites/spaceStation_017.png')
start_surface = pygame.transform.rotozoom(start_surface,0,0.5)
start_surface_rect = start_surface.get_rect(center = (500 , 300))
start_message = font_style.render("Press \'Enter\' to Start", True , (255,255,255))
start_message_rect = start_message.get_rect(center = (500 , 500))
shoot_message = font_style.render("Press \'Space\' to Shoot",True,(255,255,255))
movement_message = font_style.render("Press for Movement",True,(255,255,255))
#sound 
bg_sound = pygame.mixer.music.load("pygame\\Space_Shooter\\audio\\8bit-spaceshooter.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
collision_sound = pygame.mixer.Sound('pygame\\Space_Shooter\\audio\\explosion6.ogg')
collision_sound.set_volume(0.1)
player_collision_sound = pygame.mixer.Sound('pygame\\Space_Shooter\\audio\\explosion4.ogg')
player_collision_sound.set_volume(0.1)
rocket_sound = pygame.mixer.Sound('pygame\\Space_Shooter\\audio\\laser3.ogg')
rocket_sound.set_volume(0.1)

#ui 
space_bar = pygame.image.load('pygame\Space_Shooter\Sprites\Space_bar.png').convert_alpha()
space_bar = pygame.transform.rotozoom(space_bar,0,0.5)
space_bar_rect = space_bar.get_rect(center = (250,320))
movement_button = pygame.image.load('pygame\Space_Shooter\Sprites\Movement_button.png').convert_alpha()
movement_button = pygame.transform.rotozoom(movement_button,0,0.5)
movement_button_rect = movement_button.get_rect(center = (770,320))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            sys.exit()

        if event.type == obstacle_timer:
            spawn_random_asteroid_pattern(obstacle_group)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rocket_sound.play()
                rocket_group.add(   
                    Rocket(
                        player.sprite.rect.centerx,
                        player.sprite.rect.top
                        )
                    )
                      
        if event.type == rocket_timer:
            for rocket in rocket_group:
                effect_group.add(
                    Effect(
                            rocket
                    )
                )

        if event.type == star_timer:
            star_pattern_spawn()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_status = True
                score_count = 0

    if game_status: 

        effect_group.update()
        rocket_group.update()
        obstacle_group.update()
        splash_group.update()
        star_group.update() 
        player.update()


        #check for collision in every frame 
        splash_collision()
        rocket_collision()
        game_status = player_collision()
        
        screen.fill("#000000")
         
        star_group.draw(screen) 
        player.draw(screen)
        rocket_group.draw(screen)
        obstacle_group.draw(screen)
        splash_group.draw(screen)
        effect_group.draw(screen)
        score_board = font_style.render(f"Score :{score_count}" , True ,(255,255,255))
        screen.blit(score_board,(0,0))
        
        

    else :
        obstacle_group.empty()
        rocket_group.empty()
        star_group.empty()
        splash_group.empty()
        
        

        if score_count == 0:

            screen.fill("#000000")
            screen.blit(space_bar,space_bar_rect)
            screen.blit(movement_button,movement_button_rect)
            screen.blit(shoot_message,(70,200))
            screen.blit(movement_message,(600,190))
            screen.blit(start_message,start_message_rect)

        else :

            screen.fill("#000000")
            end_message = font_style.render(f"Score : {score_count}",True,(255,255,255))
            end_message_rect = end_message.get_rect(center = (500,70))
            screen.blit(start_surface,start_surface_rect)
            screen.blit(end_message,end_message_rect)
            screen.blit(start_message,start_message_rect)


    clock.tick(60) #FPS : 60 
    pygame.display.update()

pygame.quit()
    



