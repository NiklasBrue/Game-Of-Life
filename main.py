import pygame as pg
import time

from sample.core import algorithm
from sample.helper import mouse_position_to_board_position
import sample.constants as constants
from sample.board import Board


def main():

    screen = pg.display.set_mode((constants.height, constants.width))
    pg.display.set_caption('Game of Life')

    game_started = False
    game_finished = False

    clock = pg.time.Clock()
    board = Board()

    while not game_finished:
        board.draw(screen)

        for event in pg.event.get():
            clock.tick(30)

            if event.type == pg.QUIT:
                game_finished = True

            if pg.mouse.get_pressed()[0]:  # left mouse button
                position = pg.mouse.get_pos()
                row, col = mouse_position_to_board_position(position)
                board.make_checked(row, col)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_started = True
                if event.key == pg.K_r:
                    board.reset(screen)
                    game_started = False
                if event.key == pg.K_s:
                    game_started = False

        if game_started:
            algorithm(board)
            time.sleep(0.1)

    pg.quit()


if __name__ == '__main__':
    try:
        main()
    except:
        import pdb
        pdb.post_mortem()
