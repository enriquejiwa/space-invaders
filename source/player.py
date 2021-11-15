"""[summary]
"""
import pygame

class Player():
    def __init__(self):
        self.x_coord = 350
        self.y_coord = 700
        self.change = 0
        self.image = None
        self.set_image()
    
    def set_image(self):
        img = pygame.image.load("assets/sprites.png").convert()
        img = img.subsurface((1, 49, 16, 8))
        self.image = pygame.transform.scale(img, (48, 24))
    
    def show(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x_coord, self.y_coord))
