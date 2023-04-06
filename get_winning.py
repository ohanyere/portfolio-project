#!/usr/bin/python3

'''Defining the winning combination logic on the board'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from tic_tac_toe_game import Game
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import get_name
from tic_tac_toe_move import Move
from tic_tac_toe_player import Player
from processing_move import process_move
from valid_move import is_move_valid


def get_winning_combination(self):
    rows = [
        [(move.row, move.col) for move in row]
        for row in self.current_moves
    ]
    columns = [list(col) for col in zip(*rows)]
    leftbottom_righttop = [row[x] for x, row in enumerate(rows)]
    rightbottom_lefttop = [col[y] for y, col in enumerate(reversed(columns))]
    return rows + columns + [leftbottom_righttop, rightbottom_lefttop]
