import pygame
import random

class Enemy:
    def __init__(self):
        self.left_lane = (750,1080)
        self.right_lane = (1050,1080)
        if random.random() > 0.5:
            self.position = pygame.Vector2(self.left_lane)
        else:
            self.position = pygame.Vector2(self.right_lane)
        self.sprite = pygame.image.load('Sprites/car_enemy.png')
        self.velocity = pygame.Vector2(0,10)
        self.acceleration = (0,0)