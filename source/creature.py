"""Module containing the class Creature and its inherited, Player and Alien.
"""
import pygame


class Creature():
    """Parent class that defines the shared attributes and methods.
    """

    def __init__(self, x_coord: int, y_coord: int,
                 x_change: int, y_change: int,
                 left_limit: int, right_limit: int):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_change = x_change
        self.y_change = y_change
        self.image = None
        self.left_limit = left_limit
        self.right_limit = right_limit

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
        """Change the position coordinates using the change value, keeps the 
        creature beetwen the bondaries marked by left_limit and right_limit.
        """
        self.x_coord += self.x_change
        self.y_coord += self.y_change
        if self.x_coord < self.left_limit:
            self.x_coord = self.left_limit
        elif self.x_coord > self.right_limit:
            self.x_coord = self.right_limit


class Player(Creature):
    """Class that corresponds to the player, inherits from Creature.
    """

    def __init__(self):
        super().__init__(350, 700, 0, 0, 25, 725)
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

    def __init__(self, x_coord: int, y_coord: int, style: int, right_limit: int):
        super().__init__(x_coord, y_coord, 0.1, 0, x_coord, right_limit)
        self.set_image(style)

    def set_image(self, style: int):
        """Sets the sprite of the player, uses the sprites.png file.

        Args:
            style (int): The version on the sprite.
        """
        img = pygame.image.load("assets/sprites.png").convert()
        img = img.subsurface((*self.sprite_coord[style], 16, 8))
        self.image = pygame.transform.scale(img, (48, 24))

    def move(self):
        super().move()
        if self.x_coord in (self.left_limit, self.right_limit):
            self.y_coord += 30
            self.x_change *= -1
