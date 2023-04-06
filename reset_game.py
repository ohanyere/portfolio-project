#!/usr/bin/python3

'''Defines the logic behind resetting the game if no winner'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from tic_tac_toe_player import Player
from tic_tac_toe_move import Move
from tic_tac_toe_game import Game
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import get_name
from valid_move import is_move_valid
from get_winning import get_winning_combination
from processing_move import process_move
from is_winner import any_winner
from game_tied import is_tied
from alternate_player import switch_player


def game_reset(self):
    '''Resets the game to play again if no winner emerges'''
    for row, content_of_row in enumerate(self.current_moves):
        for col, _ in enumerate(content_of_row):
            content_of_row[col] = Move(row, col)
    self.has_winner = False
    self.winner_combination = []
