import numpy as np
import pygame as pg

from .node import Node
from . import constants


class Board:
    """Class that builds the board visually and as an array"""

    def __init__(self):
        self.height = constants.height
        self.width = constants.width
        self.rows = self.height // constants.cube_size
        self.cols = self.width // constants.cube_size
        self.node_array = np.empty((self.rows, self.cols), dtype=Node)
        self.fill_array()

    def __repr__(self):
        return f'This board is a {self.rows}x{self.cols} grid.'

    def fill_array(self):
        for row in range(self.rows):
            for col in range(self.cols):
                node = Node(row, col)
                self.node_array[row, col] = node

    def draw_grid_lines(self, screen):
        for row in range(self.rows+1):
            pg.draw.line(screen, constants.black, (row * constants.cube_size, 0), (row * constants.cube_size, self.height))
            for col in range(self.cols+1):
                pg.draw.line(screen, constants.black, (0, col * constants.cube_size), (self.width, col * constants.cube_size))

    def draw(self, screen):
        screen.fill(constants.white)
        for row in self.node_array:
            for node in row:
                node.draw(screen)
        self.draw_grid_lines(screen)
        pg.display.update()

    def make_checked(self, row, col):
        self.node_array[row, col].make_checked()

    def make_unchecked(self, row, col):
        self.node_array[row, col].make_unchecked()

    def reset(self, screen):
        self.fill_array()
        self.draw(screen)

    def get_neighbours(self, node):
        neighbours = []
        for i in range(node.row-1, node.row+2):
            for j in range(node.col-1, node.col+2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (i, j) != (node.row, node.col):
                    neighbours.append(self.node_array[i, j])
        return neighbours

