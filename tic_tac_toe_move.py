#!/usr/bin/python3

'''Defines the Move class'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from tic_tac_toe_player import Player


class Move(NT):
    '''Move class that inherited NamedTuple class of typing module'''
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 4
DEFAULT_PLAYERS = (
    Player(label="UD", color="purple"),
    Player(label="JEK", color="orange"),
)
