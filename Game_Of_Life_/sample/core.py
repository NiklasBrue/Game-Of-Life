from . import constants


def algorithm(board):
    to_be_checked = []
    to_be_unchecked = []
    for row in range(board.rows):
        for col in range(board.cols):
            current_node = board.node_array[row, col]
            neighbours = board.get_neighbours(current_node)
            active_neighbours = 0
            for neighbour in neighbours:
                if neighbour.color == constants.black:
                    active_neighbours += 1
            # The four rules
            if current_node.color == constants.black and active_neighbours < 2:
                to_be_unchecked.append(current_node)
            elif current_node.color == constants.black and 2 <= active_neighbours <= 3:
                pass
            elif current_node.color == constants.black and active_neighbours >= 3:
                to_be_unchecked.append(current_node)
            elif current_node.color == constants.white and active_neighbours == 3:
                to_be_checked.append(current_node)
    for node in to_be_checked:
        node.make_checked()
    for node in to_be_unchecked:
        node.make_unchecked()

