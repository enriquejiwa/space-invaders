"""Module containing the class Creature and its inherited, Player and Alien.
"""
import pygame


class Creature():
    """Parent class that defines the shared attributes and methods.
    """

    def __init__(self, x_coord: int, y_coord: int,
                 x_change: int = 0, y_change: int = 0):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_change = x_change
        self.y_change = y_change
        self.image = None

    def show(self, screen: pygame.Surface):
        """Displays the creature onto the screen at coordinates determined by
        the attributes.

        Args:
            screen (pygame.Surface): The surface where the creature will be
            displayed.
        """
        if self.image:
            screen.blit(self.image, (self.x_coord, self.y_coord))

    def set_change(self, x_change: int, y_change: int):
        """Set the values to change when the creature moves.

        Args:
            x_change (int): Movement on the x axis.
            y_change (int): Movement on the y axis.
        """
        self.x_change = x_change
        self.y_change = y_change

    def move(self):
        """Change the position coordinates using the change value.
        """
        self.x_coord += self.x_change
        self.y_coord += self.y_change
        if self.x_coord < 75:
            self.x_coord = 75
        elif self.x_coord > 625:
            self.x_coord = 625


class Player(Creature):
    """Class that corresponds to the player, inherits from Creature.
    """

    def __init__(self):
        super().__init__(350, 700)
        self.set_image()

    def set_image(self):
        """Sets the sprite of the player, uses the sprites.png file.
        """
        img = pygame.image.load("assets/sprites.png").convert()
        img = img.subsurface((1, 49, 16, 8))
        self.image = pygame.transform.scale(img, (48, 24))


class Alien(Creature):
    """Class that corresponds to the enemies, inherits from Creature.
    """
    sprite_coord = {0: (1, 1), 1: (19, 1), 2: (37, 1),
                    3: (1, 11), 4: (19, 11), 5: (37, 11)}

    def __init__(self, x_coord: int, y_coord: int, style: int):
        super().__init__(x_coord, y_coord)
        self.set_image(style)

    def set_image(self, style: int):
        """Sets the sprite of the player, uses the sprites.png file.

        Args:
            style (int): The version on the sprite.
        """
        img = pygame.image.load("assets/sprites.png").convert()
        img = img.subsurface((*self.sprite_coord[style], 16, 8))
        self.image = pygame.transform.scale(img, (48, 24))
