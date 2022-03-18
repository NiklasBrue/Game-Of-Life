import pygame as pg
from . import constants


class Node:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x_position = col * constants.cube_size
        self.y_position = row * constants.cube_size
        self.color = constants.white

    def __repr__(self):
        return f'(Position: ({self.row},{self.col}), color: {self.color})'

    def get_position(self):
        return self.x_position, self.y_position

    def make_checked(self):
        self.color = constants.black

    def make_unchecked(self):
        self.color = constants.white

    def is_checked(self):
        if self.color == constants.black:
            return True

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x_position, self.y_position, constants.cube_size, constants.cube_size))

