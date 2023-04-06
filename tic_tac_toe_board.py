#!/usr/bin/python3

'''Defines the game board class'''
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
from creating_board_display import create_board_display
from creating_grid import create_board_grid
from reset_board import board_reset
from reset_game import game_reset


class Board(kin.Tk):
    '''Creates the Board logic of the game'''
    def __init__(self, game):
        super().__init__()
        self.title("2D TIC_TAC_TOE GAME")
        self.cells = {}
        self.game = game
        self.create_menu()
        self.create_board_display()
        self.create_board_grid()

    def create_menu(self):
        menu_bar = kin.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = kin.Menu(master=menu_bar)
        file_menu.add_command(label="Restart", command=self.board_reset)
        file_menu.add_separator()
        file_menu.add_command(label="Pause", command=pause)
        file_menu.add_separator()
        file_menu.add_command(label="Resume", command=resume)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
