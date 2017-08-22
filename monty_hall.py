"""
Monty Hall Simulator

Simulates Monty Hall decision agents
"""

import numpy as np


def assign_doors():
    items = ["car", "toothpaste", "garbage can"]
    d_keys = [1, 2, 3]
    doors = dict()
    random_doors = np.random.permutation(d_keys)
    random_items = np.random.permutation(items)
    random_zip = zip(random_doors, random_items)
    for door, item in random_zip:
        doors[door] = item
    return doors


def guess(doors):
    """
    Returns dictionary key for first guess

    This is a private guess only known to the Player

    """
    door_guess = np.random.choice(list(doors.keys()))
    return door_guess


class Player:
    def __init__(self, doors):
        self.guess = guess(doors)

    def guess_again(self, new_doors):
        self.guess = guess(new_doors)
        return self.guess


class Game:
    """Monty Hall Game

    Parameters 
    ----------
    
    player_type : {'stay', 'change'}
        determines player strategy
        stay : keep first choice
        change : choose again


    """

    def __init__(self, player_type="stay", rounds = 1):
        self.player_type = player_type
        self.doors = assign_doors()
        self.results = []
        self.rounds = rounds

    def play(self):
        player = Player(self.doors)
        guess = player.guess
        



