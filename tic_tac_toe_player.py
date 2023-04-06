#!/usr/bin/python3

'''Defines the Player class'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT


class Player(NT):
    '''Player class that inherits NamedTuple class of typing module'''
    label: str
    color: str
