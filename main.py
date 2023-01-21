import pygame
from car import Car 
from Background import background
#import the class "car" and class "background"
from pygame.math import Vector2

def main():
    screen = pygame.display.set_mode((0,0))
    car = Car()
    car_position = car.position
    car_velocity = car.velocity
    car_velocity.x += car.acceleration
    car_velocity.y += car.acceleration
    car_position.x += car_velocity.x
    car_position.y += car_velocity.y
    screen.blit(car.sprite, (car_position.x, car_position.y))
    #making car

    pygame.init()
   
    pygame.display.set_caption('Highway maniac')
    #title and stuff
    screen.blit(background().sprite,(0,0))
    #Background

    pygame.display.update()
    #The background and stuff
     
    running = True #change this to "True" for forever running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    #infinite running loop if needed

if __name__ == "__main__":
    main() #end Main sequence