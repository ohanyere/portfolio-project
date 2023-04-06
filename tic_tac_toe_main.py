#!/usr/bin/python3

'''Defines the game board and runs its main loop'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from alternate_player import switch_player
from creating_board_display import create_board_display
from creating_grid import create_board_grid
from game_tied import is_tied
from game_play import play
from get_winning import get_winning_combination
from highlight_cells import cells_highlight
from is_winner import any_winner
from processing_move import process_move
from reset_board import board_reset
from reset_game import game_reset
from tic_tac_toe_board import Board
from tic_tac_toe_board import create_menu
from tic_tac_toe_game import Game
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import get_name
from tic_tac_toe_move import Move
from tic_tac_toe_player import Player
from update_button import button_update
from update_display import display_update
from valid_move import is_move_valid


def main():
    '''Creates the game board and runs its main loop'''
    game = Game()
    board = Board(game)
    board.mainloop()


if __name__ == "__main__":
    main()
