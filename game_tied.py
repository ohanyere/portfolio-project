#!/usr/bin/python3

'''Defines the logic behind the game outcome being tied'''
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


def is_tied(self):
    '''If the game is tied return True, otherwise False'''
    no_winner = not self.has_winner
    moves_played = (move.label for row in self.current_moves for move in row)
    return no_winner and all(moves_played)
