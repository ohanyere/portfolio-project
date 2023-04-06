#!/usr/bin/python3

'''Defines the logic behing the players moves'''
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
from update_button import button_update
from update_display import display_update
from reset_game import game_reset
from highlight_cells import cells_highlight


def play(self, event):
    '''Runs the players moves'''
    clicked_button = event.widget
    row, col = self.cells[clicked_button]
    move = Move(row, col, self.game.current_player.label)
    if self.game.is_move_valid(move):
        self.button_update(clicked_button)
        self.game.process_move(move)
        if self.game.is_tied():
            self.display_update(msg="Game Tied!", color="red")
        elif self.game.any_winner():
            self.cells_highlight()
            msg = f"Player '{self.game.current_player.label}' won!"
            color = self.game.current_player.color
            self.display_update(msg, color)
        else:
            self.game.switch_player()
            msg = f"{self.game.current_player.label}'s turn"
            self.display_update(msg)
