#!/usr/bin/python3

'''Defining the logic behind the valididty of any move made on the board'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from tic_tac_toe_player import Player
from tic_tac_toe_move import Move
from tic_tac_toe_game import Game
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import get_name
from get_winning import get_winning_combination
from processing_move import process_move


def is_move_valid(self, move):
    '''Returns True for valid move and False otherwise'''
    row, col = move.row, move.col
    move_unplayed = self.current_moves[row][col].label == ""
    no_winner = not self.has_winner
    return no_winner and move_unplayed

