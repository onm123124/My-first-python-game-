import pygame
import random
class Enemy:
    def __init__(self):
        left_lane = (750,1080)
        right_lane = (1250,1080)
        self.sprite = pygame.image.load('Sprites/car_enemy.png')
        self.position = pygame.Vector2(left_lane)
        self.velocity = pygame.Vector2(0,10)
        self.acceleration = (0,0)