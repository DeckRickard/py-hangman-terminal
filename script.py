# Multiplayer hangman game: A Terminal game created by Rowan Jeffery-Wall as part of the CodeCademy Computer Science Career Path. This is a hangman game that can be played alone or with up to 6 players.
import random


# The player class is used to keep track of player details
class Player:
    def __init__(self, name):
        self.name = name
        self.games_won = 0

    def __repr__(self):
        return "A player called {name}. They have won {games_won} games".format(name=self.name, games_won=self.games_won)
    
# Initial variables are defined here.
num_players = ""
# Functions are defined here.

# Main program code from here below.

while num_players.isalpha() or int(num_players) > 6:
    num_players = input("How many players will there be? The maximum is 6 players")

