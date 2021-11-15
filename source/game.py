"""Module containing the Game class.
"""
import pygame
from . import creature


class Game():
    """Class that manages the execution of the game.
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 800))
        self.set_window_settings()
        self.running = True
        self.player = creature.Player()
        self.enemies = []
        self.create_enemies()

    def set_window_settings(self):
        """Sets the window information, the caption and icon.
        """
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)

    def event_loop(self):
        """Checks for the events and utilizes this information as necessary.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        """Fills and updates the screen with all the objects.
        """
        self.screen.fill((0, 0, 0))
        self.player.show(self.screen)
        for enemy in self.enemies:
            enemy.show(self.screen)
        pygame.display.update()

    def start(self):
        """Contains the infinite loop that keeps the game running.
        """
        while self.running:
            self.event_loop()
            self.draw()

    def create_enemies(self):
        """Helper method for the initilitzation of all the enemies.
        """
        y_coord = 100
        for style in range(6):
            x_coord = 75
            for _ in range(11):
                self.enemies.append(creature.Alien(x_coord, y_coord, style//2))
                x_coord += 50
            y_coord += 40
