import pygame
from car import Car 
from Background import background
#import the class "car" and class "background"
from pygame.math import Vector2

def main():
    pygame.init()

    car = Car()
    car_velocity = car.velocity
    screen_width, screen_height = pygame.display.get_surface,pygame.display.get_surface
    screen = pygame.display.set_mode((1920,1080))
    car_position = pygame.Vector2(car.position)
    
    

    pygame.display.set_caption('Highway maniac')
    
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        screen.blit(background().sprite,(0,0))
        car_velocity.x += car.acceleration
        car_velocity.y += car.acceleration
        car_position += car_velocity
        screen.blit(car.sprite, (car_position.x, car_position.y))
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

if __name__ == "__main__":
    main() #end Main sequence