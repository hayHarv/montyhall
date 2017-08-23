"""
Monty Hall Problem Simulator
"""


import numpy as np

def choose(doors):
    choice = np.random.choice(doors, size=1)[0]
    return choice


class Game:
    """
    One round of monty hall game

    Parameters
    --------------
    player_type : {"stay", "switch"}
    stay : player stays with first choice
    switch : player switches

    n_doors : number of doors in the game

    """
    def __init__(self, player_type="stay", n_doors=3):
        self.player_type = player_type
        self.doors = np.arange(n_doors)
        self.winner = choose(self.doors)
        self.guess = choose(self.doors)
        self.result = 0

    def play(self):
        drop_options = self.doors[np.where((self.doors != self.guess) & (self.doors !=
            self.winner))]
        to_drop = np.random.choice(drop_options, size=1)[0]
        new_doors = self.doors[np.where(self.doors != to_drop)]
        if self.player_type == "stay":
            if self.guess == self.winner:
                self.result = 1
                return self.result
            else:
                self.result = 0
                return self.result
        elif self.player_type == "switch":
            new_guess = choose(new_doors[np.where(new_doors != self.guess)])
            if new_guess == self.winner:
                self.result = 1
                return self.result
            else:
                self.result = 0
                return self.result


class N_trials:
    def __init__(self, n, n_doors=3):
        self.n = n
        self.results = {"switch": [], "stay": []}
        self.outcomes = {}
        self.outcome_proba = {}
        self.n_doors = n_doors
 
    def run_trials(self):
        for player_type in ["stay", "switch"]:
            for trial in range(self.n):
                game = Game(player_type=player_type, n_doors=self.n_doors)
                game.play()
                self.results[player_type].append(game.result)
            self.outcomes[player_type] = sum(self.results[player_type])
            proba = self.outcomes[player_type]/self.n
            self.outcome_proba[player_type] = proba



