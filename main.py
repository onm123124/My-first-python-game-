import pygame
from car import Car 
from Background import background
#import the class "car" and class "background"
from pygame.math import Vector2

def main():
    pygame.init()
    screen = pygame.display.set_mode((0,0),0,0)
    pygame.display.set_caption('Highway maniac')
    pygame.display.set_icon(Car().sprite)
    screen.blit(background().sprite,(0,0))
    
    #The background and stuff
    running = True #change this to "True" for forever running
    while running == True:
        for event in pygame. event.get():
            if event. type == pygame.quit:
                running = False
            if running == False:
                pygame.quit()
    #infinite running loop if needed

if __name__ == "__main__":
    main()