import pygame
from car import Car 
from Background import background
from Enemy import Enemy
from reset import Reset
#import the class "car" and class "background" and other files
from pygame.math import Vector2
import random
import time
#import the shit
def main():
    pygame.init()
#initialize
    car = Car()
    car_velocity = car.velocity
    screen_height, screen_width = 1920, 1080
    screen = pygame.display.set_mode((1920,1080))
    car_position = pygame.Vector2(car.position)
    player_rect = pygame.Rect(car_position.x, car_position.y,car.sprite.get_width(), car.sprite.get_height())
    
    #define variables
    #Enemy car code starts here:
    enemy = Enemy()
    enemy_velocity = enemy.velocity
    enemy_position = enemy.position
    left_lane = enemy.left_lane
    right_lane = enemy.right_lane
    enemy_spawn_counter = 0
    enemy_spawn_interval = 120
    enemy_rect = pygame.Rect(enemy_position.x, enemy_position.y, enemy.sprite.get_width(), enemy.sprite.get_height())
        
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
        car_rect = pygame.Rect(car_position.x, car_position.y, car.sprite.get_width(), car.sprite.get_height())
        enemy_rect = pygame.Rect(enemy_position.x, enemy_position.y, enemy.sprite.get_width(), enemy.sprite.get_height())

        if car_rect.colliderect(enemy_rect):
            enemy_spawn_counter += 1
            Reset()
        if enemy_spawn_counter == enemy_spawn_interval:
            enemy = Enemy()
            enemy_velocity = enemy.velocity
            enemy_position = enemy.position
            enemy_spawn_counter = 0
        enemy_position += enemy_velocity       
        screen.blit(enemy.sprite, (enemy_position.x, enemy_position.y))
        pygame.display.update()
        if enemy_position.y >= 1080:
            enemy_position.y = -100

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
        print (enemy_position)
        pass
if __name__ == "__main__":
    main() #run Main sequence
