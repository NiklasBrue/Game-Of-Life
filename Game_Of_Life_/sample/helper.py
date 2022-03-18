from . import constants


def mouse_position_to_board_position(mouse_position):
    array_col = mouse_position[0] // constants.cube_size
    array_row = mouse_position[1] // constants.cube_size
    return array_row, array_col
