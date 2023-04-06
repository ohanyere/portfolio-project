#!/usr/bin/python3

'''Defines the logic behind a winner emerging'''
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


def any_winner(self):
    '''If there is a winner return True, and False if otherwise'''
    return self.has_winner
