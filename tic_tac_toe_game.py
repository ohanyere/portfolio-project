#!/usr/bin/python3

'''Defines the Game class'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from get_winning import get_winning_combination
from tic_tac_toe_move import Move
from tic_tac_toe_player import Player


class Game:
    '''Describes the game logic'''
    def __init__(self, type, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        '''Initializes the game logic'''
        self.players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combination = []
        self.current_moves = []
        self.has_winner = False
        self.winning_combination = []
        self.type = type
        self.board_setup()
        self.name = self.get_name()

    def board_setup(self):
        '''Setting up the board'''
        self.current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self.winning_combination = self.get_winning_combination()

    def get_name(self):
        '''Returns the name of each player selected'''
        if self.type == "UD":
            name = input("Player selecting UD, enter your name: ")
        else:
            name = input("Player selecting JEK, enter your name: ")
        return 
