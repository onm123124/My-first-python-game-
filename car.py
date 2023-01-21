import pygame
class Car():
   def __init__(self):
        self.sprite = pygame.image.load('Sprites/car.png')
        self.position = pygame.Vector2(750,750)
        self.velocity = pygame.Vector2(1,0)
        self.acceleration = 0.1