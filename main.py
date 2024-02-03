import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 600
WIDTH = 1000

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

#player

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
#player_speed = [1, 1]
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_left = [-1, 0]
player_move_right = [1, 0]

#enemy

def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0 ]
    return [enemy, enemy_rect, enemy_move]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []


#bonus

#def create_bonus():
bonus_size = (40, 40)
bonus = pygame.Surface(bonus_size)
bonus.fill(COLOR_GREEN)
bonus_rect = bonus.get_rect()
bonus_move = [0, 1]
#    bonus_rect = pygame.Rect(HEIGHT, random.randint(WIDTH, 1), *bonus_size)
#    bonus_move = [0, random.randint(1, 6) ]
#    return [bonus, bonus_rect, bonus_move]
#
#bonuses = []
#CREATE_BONUS = pygame.USEREVENT + 2
#pygame.time.set_timer(CREATE_BONUS, 2000)

playing = True
while playing:
    FPS.tick(300)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        #if event.type == CREATE_BONUS:
        #    enemies.append(create_bonus())
        

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        #print('pressed')
        player_rect = player_rect.move(player_move_down)
    if keys[K_UP] and player_rect.top > 0:
        #print('pressed')
        player_rect = player_rect.move(player_move_up)
    if keys[K_LEFT] and player_rect.left > 0:
        #print('pressed')
        player_rect = player_rect.move(player_move_left)
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        #print('pressed')
        player_rect = player_rect.move(player_move_right)


    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])


    #for bonus in bonuses:
    #    bonus[1] = bonus[1].move(bonus[2])
    #    main_display.blit(bonus[0], bonus[1])



    #enemy_rect = enemy_rect.move(enemy_move)
    #print(player_rect.bottom)
    #if player_rect.bottom >= HEIGHT:
    #    player_speed = random.choice(([1, -1], [-1, -1]))
    #if player_rect.top < 0:
    #    player_speed = random.choice(([-1, 1], [1, 1]))
    #if player_rect.left < 0:
    #    player_speed = random.choice(([1, 1], [1, -1]))
    #if player_rect.right >= WIDTH:
    #    player_speed= random.choice(([-1, -1], [-1, 1]))

    
    main_display.blit(player, player_rect)
    #main_display.blit(enemy, enemy_rect)
    main_display.blit(bonus, bonus_rect)

    #player_rect = player_rect.move(player_speed)
    print(len(enemies))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

