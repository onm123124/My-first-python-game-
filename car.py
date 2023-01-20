import pygame
class Car():
    def __init__(self):
        self.sprite = pygame.image.load('Sprites/Rectangle.png')
        position = pygame.Vector2()
        position.xy = 295, 100
        velocity = pygame.Vector2()
        velocity.xy = 3, 0
    acceleration = 0.1
        #make car exist
        #movable