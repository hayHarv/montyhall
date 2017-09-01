"""
Author Hayden Harvey

Monty Hall Problem Simulator

I wrote this because the Monty Hall problem
is really confusing and it seemed like good
practice for working with numpy structures.

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


class N_rounds:
    """
    class for simulating Monty Hall game

    runs n_trials for each "switch" and "stay" player types


    Parameters
    ----------
    n_rounds: number of rounds
    n_doors: number of doors per round

    Returns
    ----------
    results: dict of outcomes (wins and losses) for each player type
    outcomes: dict of count of outcomes (wins) for each over n_rounds
    outcome_proba: dict of outcome probabilities for each player type

    """
    def __init__(self, n_rounds, n_doors=3):
        self.n_rounds = n_rounds
        self.results = {"switch": [], "stay": []}
        self.outcomes = {}
        self.outcome_proba = {}
        self.n_doors = n_doors

        def run_trials(self):
            for player_type in ["stay", "switch"]:
                for trial in range(self.n_rounds):
                    game = Game(player_type=player_type, n_doors=self.n_doors)
                    game.play()
                    self.results[player_type].append(game.result)
                self.outcomes[player_type] = sum(self.results[player_type])
                proba = self.outcomes[player_type]/self.n_rounds
                self.outcome_proba[player_type] = proba

        run_trials(self)

