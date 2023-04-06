#!/usr/bin/python3

'''Defines the logic that resets the game board to restart game'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from tic_tac_toe_player import Player
from tic_tac_toe_move import Move
from tic_tac_toe_game import Game
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import get_name
from tic_tac_toe_board import Board
from tic_tac_toe_board import create_menu
from valid_move import is_move_valid
from get_winning import get_winning_combination
from processing_move import process_move
from reset_game import game_reset
from is_winner import any_winner
from game_tied import is_tied
from alternate_player import switch_player
from creating_board_display import create_board_display
from creating_grid import create_board_grid
from game_play import play
from update_button import button_update
from update_display import display_update
from highlight_cells import cells_highlight


def board_reset(self):
    '''Resets the game board to restart the game'''
    self.game.game_reset()
    self.display_update(msg="Game On")
    for button in self.cells.keys():
        button.config(highlightbackground="orange")
        button.config(text="")
        button.config(fg="blue")
