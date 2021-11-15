# pylint: skip-file
import pygame
import random
import math

# Initializa the pygame.
pygame.init()

# Create the screen.
screen = pygame.display.set_mode((800, 600))

# Caption and icon.
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

# Player.
player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (64, 64))
player_x = 368
player_y = 480
player_change = 0

enemy_img = []
enemy_x = []
enemy_y = []
enemy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.transform.scale(pygame.image.load("assets/alien1.png"), (64, 64)))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_change.append(0.1)

bullet_img = pygame.image.load("assets/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (64, 64))
bullet_x = 0
bullet_y = 480
bullet_change = 0.1
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16, y+10))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x, 2) +
                         math.pow(enemy_y-bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    player_x += player_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736


    for i in range(num_of_enemies):
        enemy_x[i] += enemy_change[i]

        if enemy_x[i] <= 0:
            enemy_x[i] = 0
            enemy_y[i] += 40
            enemy_change[i] = 0.1
        elif enemy_x[i] >= 736:
            enemy_x[i] = 736
            enemy_y[i] += 40
            enemy_change[i] = -0.1

        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)
        
        enemy(enemy_x[i], enemy_y[i], i)

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= 0.3

    show_score(text_x, text_y)

    player(player_x, player_y)
    pygame.display.update()
