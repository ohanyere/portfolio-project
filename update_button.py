#!/usr/bin/python3

'''Defines the logic on what happens whenever buttons are clicked'''
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
from is_winner import any_winner
from game_tied import is_tied
from alternate_player import switch_player
from creating_board_display import create_board_display
from creating_grid import create_board_grid
from reset_board import board_reset
from game_play import play
from update_display import display_update
from reset_game import game_reset
from highlight_cells import cells_highlight


def button_update(self, clicked_button):
    '''Updates game buttons on the board when clicked by a player'''
    clicked_button.config(text=self.game.current_player.label)
    clicked_button.config(fg=self.game.curent_player.color)
