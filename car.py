import pygame
class Car():
   def __init__(self):
        self.sprite = pygame.image.load('Sprites/car.png')
        self.position = pygame.Vector2(750,1080)
        self.velocity = pygame.Vector2(0,-5)
        self.acceleration = 0.0