import pygame
import random
from car import Car 
from Background import background
from Enemy import Enemy
from pygame.math import Vector2
import time
class Reset:
    def __init__(self):
        enemy = Enemy()
        left_lane = enemy.left_lane
        right_lane = enemy.right_lane
        car_position = pygame.Vector2(750, 1080) # reset car position
        car_velocity = pygame.Vector2(0,0) # reset car velocity
        enemy_position = pygame.Vector2(random.choice(left_lane, right_lane)) # reset enemy position
        enemy_velocity = pygame.Vector2(0, 10) # reset enemy velocity
        enemy_spawn_counter = 1 # reset enemy spawn counter