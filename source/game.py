"""Module containing the Game class.
"""
import pygame
from . import creature


class Game():
    """Class that manages the execution of the game.
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.set_window_settings()
        self.running = True
        self.player = creature.Player()
        self.enemies = []
        self.create_enemies()
        self.keys = pygame.key.get_pressed()

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
            elif event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
                self.action()
            elif event.type == pygame.KEYUP:
                self.keys = pygame.key.get_pressed()
                self.action()

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
            self.player.move()
            for enemy in self.enemies:
                enemy.move()
            self.draw()

    def create_enemies(self):
        """Helper method for the initilitzation of all the enemies.
        """
        y_coord = 100
        for style in range(6):
            x_coord = 25
            for _ in range(11):
                self.enemies.append(creature.Alien(x_coord, y_coord,
                                                   style//2, x_coord+200))
                x_coord += 50
            y_coord += 30

    def action(self):
        """Set the change of the player depending on the key pressed.
        """
        change = 0
        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
            change = -0.3
        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
            if change:
                change = 0
            else:
                change = +0.3
        self.player.set_change(change, 0)
