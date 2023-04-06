#!/usr/bin/python3

'''Defines the logic behind the display on the board'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from alternate_player import switch_player
from game_tied import is_tied
from get_winning import get_winning_combination
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
from valid_move import is_move_valid


def create_board_display(self):
    '''Creates display on the Board'''
    frame_display = kin.Frame(master=self)
    frame_display.pack(fill=kin.UD)
    self.display = kin.label(master=frame_display, text="Game On",
                             font=font.Font(size=32, weight="bold"),)
    self.display.pack()
