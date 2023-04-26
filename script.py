# Multiplayer hangman game: A Terminal game created by Rowan Jeffery-Wall as part of the CodeCademy Computer Science Career Path. This is a hangman game that can be played alone or with up to 6 players.
import random


# The player class is used to keep track of player details
class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.games_won = 0

    def __repr__(self):
        return "A player called {name}. They have won {games_won} games".format(name=self.name, games_won=self.games_won)
    
# Initial variables are defined here.
title = """
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

num_players_valid = False
vs_AI = False

# Functions are defined here.

# Number of players input is checked for validity.
def check_num_players(input):
    if input.isnumeric() and int(input) in range(1, 7):
        return True
    else:
        return False
    
# This function handles the creation of players depending on the number that was inputted by the user.
def create_players(number):
    players = {}
    for i in range(0, int(number)):
        players[f"player{i + 1}"] = Player(input(f"Player {i + 1}, what is your name? ", ), i + 1)
    return players


    
# Main program code from here below.
print(title)
num_players = input("How many players will there be? The maximum is 6 players: ")
while not check_num_players(num_players):
    num_players =  input("You have entered an invalid input. Please enter a number between 1 and 6: ")
# Create a dictionary containing all the players.
players_dict = create_players(num_players)




