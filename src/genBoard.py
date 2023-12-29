import numpy as np
import random

dim = 75
BOARD_DIR = '../'

def random_board(dim):
    board = np.array(np.random.randint(1, 10, size=(dim, dim)), dtype=str)

    start_location = [random.randint(0,dim-1), random.randint(0,dim-1)]
    end_location = [random.randint(0,dim-1), random.randint(0,dim-1)]

    if(start_location == end_location):
        board_info = random_board(dim)
        board = board_info[0]
        start_location = board_info[1][1]
        end_location = board_info[2][1]

    board[start_location[0], start_location[1]] = 'S'
    board[end_location[0], end_location[1]] = 'G'

    return board

board = random_board(dim)

np.savetxt(f'{BOARD_DIR}TestBoard.txt', board, delimiter='\t', fmt='%s')
