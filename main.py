import pygame
from car import Car 
from Background import Background
#import the class "car" and class "background"
from pygame.math import Vector2

def main():
    pygame.init
    DISPLAY = pygame.display.set_mode((100,100),0,32)
    pygame.display.set_caption('Highway maniac')
    pygame.display.set_icon(Car().sprite)
    background = pygame.display.set_icon(Background().sprite)
    pygame.display.set_mode()
    #The background and stuff
    running = False #change this to "True" for forever running
    while running == True:
        for event in pygame. event.get():
            if event. type == pygame.quit:
                running = False
            if running == False:
                pygame.quit()
    #infinite running loop if needed

if __name__ == "__main__":
    main()