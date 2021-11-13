"""[summary]
"""
import pygame

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

def player():
    screen.blit(player_img, (player_x, player_y))


running = True
while running:

    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player()
    pygame.display.update()
