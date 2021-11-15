"""[summary]
"""
import pygame
from . import player


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 800))
        self.set_window_settings()
        self.running = True
        self.player = player.Player()

    def set_window_settings(self):
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.show(self.screen)
        pygame.display.update()

    def start(self):
        while self.running:
            self.event_loop()
            self.draw()
