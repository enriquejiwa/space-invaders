"""Module containing the Game class.
"""
import pygame
from . import creature


class Game():
    """Class that manages the execution of the game.
    """
    score_coords = [(21, 89), (21, 69), (61, 79), (11, 89), (41, 69)]
    score = []
    game_over_coords = [(61, 69), (1, 69), (41, 79), (41, 69), (61, 79),
    (51, 89), (41, 69), (11, 89)]
    over = []
    numbers_coords = [(21, 99), (31, 99), (41, 99), (51, 99), (61, 99),
                      (71, 99), (1, 109), (11, 109), (21, 109), (31, 109)]
    numbers = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.set_window_settings()
        self.running = True
        self.player = creature.Player()
        self.enemies = []
        self.create_enemies()
        self.keys = pygame.key.get_pressed()
        self.score_value = 0
        self.set_score()
        self.set_game_over()

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
        self.show_score()
        self.player.show(self.screen)
        for enemy in self.enemies:
            if enemy:
                enemy.show(self.screen)
        pygame.display.update()

    def start(self):
        """Contains the infinite loop that keeps the game running.
        """
        while self.running:
            self.event_loop()
            self.player.move()
            for enemy in self.enemies:
                if enemy:
                    enemy.move()
            self.check_collision()
            if self.player.health > 0 and self.score_value < 660:
                self.draw()
            else:
                self.game_over()

    def create_enemies(self):
        """Helper method for the initilitzation of all the enemies.
        """
        y_coord = 50
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
        if self.keys[pygame.K_SPACE]:
            self.player.shoot()

    def check_collision(self):
        """Check the collision on the bullets to the player and enemies.
        """
        for index, enemy in enumerate(self.enemies):
            if enemy:
                if self.player.check_bullet_impact(enemy):
                    self.enemies[index] = None
                    self.score_value += 10
                enemy.check_bullet_impact(self.player)

    def set_score(self):
        """Loads the sprites of SCORE and the numbers.
        """
        img = pygame.image.load("assets/sprites.png").convert()
        for coord in self.score_coords:
            temp = img.subsurface((*coord, 8, 8))
            temp = pygame.transform.scale(temp, (24, 24))
            self.score.append(temp)
        for coord in self.numbers_coords:
            temp = img.subsurface((*coord, 8, 8))
            temp = pygame.transform.scale(temp, (24, 24))
            self.numbers.append(temp)

    def show_score(self):
        """Shows the score of the player
        """
        x_coord = 10
        for letter in self.score:
            self.screen.blit(letter, (x_coord, 10))
            x_coord += 25
        temp = self.score_value
        x_coord += 25
        for i in range(3, -1, -1):
            self.screen.blit(self.numbers[temp//(10**i)], (x_coord, 10))
            temp  %= 10**i
            x_coord += 25
    
    def set_game_over(self):
        """Loads the sprites of GAMEOVER.
        """
        img = pygame.image.load("assets/sprites.png").convert()
        for coord in self.game_over_coords:
            temp = img.subsurface((*coord, 8, 8))
            temp = pygame.transform.scale(temp, (64, 64))
            self.over.append(temp)

    def game_over(self):
        """Shows the game over screen
        """
        self.screen.fill((0, 0, 0))
        x_coord = 120
        for letter in self.over:
            self.screen.blit(letter, (x_coord, 320))
            x_coord += 70
        pygame.display.update()
