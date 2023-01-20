import pygame
class car():
    def __init__(self):
        self.sprite = pygame.image.load('Sprites/Rectangle.png')
        self.position = pygame.Vector2()
        self.position.xy