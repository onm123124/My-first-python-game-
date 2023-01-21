import pygame
from car import Car 
from Background import background
from Enemy import Enemy
#import the class "car" and class "background" and other files
from pygame.math import Vector2
import random
#import the shit
def main():
    pygame.init()
#initialize
    car = Car()
    car_velocity = car.velocity
    screen_height, screen_width = 1920, 1080
    screen = pygame.display.set_mode((1920,1080))
    car_position = pygame.Vector2(car.position)
    #define variables
    #Enemy car code starts here:
    enemy = Enemy()
    enemy_velocity = enemy.velocity
    enemy_position = enemy.position
        
    pygame.display.set_caption('Highway maniac')
    #title
    pygame.display.update()
    #clean screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        #infinte running loop
        screen.blit(background().sprite,(0,0))
        car_velocity.x += car.acceleration
        car_velocity.y += car.acceleration
        car_position += car_velocity
        screen.blit(car.sprite, (car_position.x, car_position.y))
        
        screen.blit(Enemy().sprite,(enemy_position))
        #make the car and background
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            car.velocity.x = -10 # <-- move left
        elif keys[pygame.K_d]:
            car.velocity.x = 10 # <-- move right
        else:
            car.velocity.x = 0 # <-- stop moving        
                #make car go back to center when it get out
        if car_position.x > screen.get_width() or car_position.x < 0 or car_position.y > screen.get_height() or car_position.y < 0:
            car_position = pygame.Vector2(750,1080)
        
        pygame.display.update()
        if car_position.x < (screen_width/2) - -250: # <-- left edge of the road
            car_position.x = (screen_width/2) - -250
        if car_position.x > (screen_width/2) + 500: # <-- right edge of the road
            car_position.x = (screen_width/2) + 500
        #stop car from going into grass
        pygame.display.update()

        
if __name__ == "__main__":
    main() #run Main sequence