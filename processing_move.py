#!/usr/bin/python3

'''Defines the logic behind processing move on the board'''
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


def process_move(self, move):
    '''Checking if the current move is a win'''
    row, col = move.row, move.col
    self.current_moves[row][col] = move
    for combination in self.winning_combination:
        outcome = set(self.current_moves[n][m].label for n, m in combination)
        is_win = (len(outcome) == 1) and ("" not in outcome)
        if is_win:
            self.has_winner = True
            self.winner_combination = combination
            break

