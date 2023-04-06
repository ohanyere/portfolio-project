#!/usr/bin/python3

'''Defines the logic behind creating grid of the Board'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from alternate_player import switch_player
from creating_board_display import create_board_display
from game_play import play
from game_tied import is_tied
from get_winning import get_winning_combination
from is_winner import any_winner
from processing_move import process_move
from reset_game import game_reset
from tic_tac_toe_board import Board
from tic_tac_toe_board import create_menu
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import Game
from tic_tac_toe_game import get_name
from tic_tac_toe_move import Move
from tic_tac_toe_player import Player
from valid_move import is_move_valid


def create_board_grid(self):
    frame_grid = kin.Frame(master=self)
    frame_grid.pack()
    for row in range(self.game.board_size):
        self.rowconfigure(row, weight=1, minsize=55)
        self.columnconfigure(row, weight=1, minsize=80)
        for col in range(self.game.board_size):
            button = kin.Button(master=frame_grid, text="",
                                font=font.Font(size=38, weight="bold"),
                                fg="blue", width=4, height=3,
                                highlightbackground="orange",)
            self.cells[button] = (row, col)
            button.bind("<ButtonPress-1>", self.play)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
