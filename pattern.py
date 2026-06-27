
from obstacle import Obstacle 
import pygame 
import random 



#Obstacle Pattern 
def rectangle_pattern_obstacle(obstacle_group):
    start_x = 100 
    start_y = -80

    spacing_x = 100
    spacing_y = 100

    rows = 2 
    cols = 9

    for row in range(rows):
        for col in range(cols):
            x = start_x + (col * spacing_x)
            y = start_y + (row * spacing_y)

            obstacle_group.add(Obstacle(x,y,speed_y =2)) 

def line_pattern_obstacle(obstacle_group): 
    y = -80
    x_positions = [100, 250, 400, 550, 700, 850]

    for x in x_positions:
        obstacle_group.add(Obstacle(x, y, speed_y=random.randint(3,4)))


def spawn_asteroid_reverse_diagonal(obstacle_group):
    start_x = 750
    start_y = -300

    spacing_x = 100
    spacing_y = 100

    for i in range(6):
        x = start_x - i * spacing_x
        y = start_y + i * spacing_y

        obstacle_group.add(Obstacle(x, y, speed_y=3))

def spawn_asteroid_diagonal(obstacle_group):
    start_x = 150
    start_y = -300

    spacing_x = 100
    spacing_y = 100

    for i in range(6):
        x = start_x + i * spacing_x
        y = start_y + i * spacing_y

        obstacle_group.add(Obstacle(x, y, speed_y=4))

def spawn_asteroid_v_shape(obstacle_group):
    positions = [
        (250, -250),
        (300, -200),
        (350, -150),
        (400, -100),
        (450, -50),
        (500, -100),
        (550, -150),
        (600, -200),
        (650, -250),
    ]

    for x, y in positions:
        obstacle_group.add(Obstacle(x, y, speed_y=4))

def spawn_asteroid_rectangle_outline(obstacle_group):
    start_x = 250
    start_y = -300

    spacing_x = 100
    spacing_y = 100

    rows = 4
    cols = 5

    for row in range(rows):
        for col in range(cols):

            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                x = start_x + col * spacing_x
                y = start_y + row * spacing_y

                obstacle_group.add(Obstacle(x, y, speed_y = 3))

def left_side_asteroid_pattern(obstacle_group):
    y_positions = [100,300, 500]

    for y in y_positions:
        obstacle_group.add(
            Obstacle(
                x=-50,
                y=y,
                speed_x=4,
                speed_y=1
            )
        )

def right_side_asteroid_pattern(obstacle_group):
    y_positions = [100, 300, 500]

    for y in y_positions:
        obstacle_group.add(
            Obstacle(
                x=950,
                y=y,
                speed_x=-4,
                speed_y=1
            )
        )

def diagonal_left_asteroid_pattern(obstacle_group):
    positions = [
        (-50, 50),
        (-120, 120),
        (-190, 190),
        (-260, 260),
        (-330, 330)
    ]

    for x, y in positions:
        obstacle_group.add(
            Obstacle(
                x=x,
                y=y,
                speed_x=4,
                speed_y=2
            )
        )
def spawn_random_asteroid_pattern(obstacle_group):
    pattern = random.choice([
            line_pattern_obstacle,
            rectangle_pattern_obstacle,
            spawn_asteroid_reverse_diagonal,
            spawn_asteroid_v_shape,
            spawn_asteroid_diagonal,
            spawn_asteroid_rectangle_outline,
            left_side_asteroid_pattern,
            right_side_asteroid_pattern,
            diagonal_left_asteroid_pattern
            
    ])
    pattern(obstacle_group)