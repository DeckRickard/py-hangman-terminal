# Multiplayer hangman game: A Terminal game created by Rowan Jeffery-Wall as part of the CodeCademy Computer Science Career Path. This is a hangman game that can be played alone or with up to 6 players.
import random
import string
# Local word bank file is read and used to create a list of words for the AI to use.
with open('words.csv') as word_bank:
    raw_text = word_bank.read()
    words_list_raw = raw_text.split(',')
    words_list = []
    for word in words_list_raw:
        words_list.append(word.strip())


# The player class is used to keep track of player details
class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.games_won = 0

    def __repr__(self):
        return "A player called {name}. They have won {games_won} games".format(name=self.name, games_won=self.games_won)
    
    def winner(self):
        self.games_won += 1
    
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
alphabet = set(string.ascii_uppercase) # A set containing all letters of the alphabet in uppercase.
gallows = {6: """
        --------
        |      |
        |
        |
        |
        |
        _______
        """,
        5: """
        --------
        |      |
        |      O
        |
        |
        |
        _______
        """,
        4: """
        --------
        |      |
        |      O
        |      |
        |
        |
        _______
        """,
        3: """
        --------
        |      |
        |      O
        |     /|
        |
        |
        _______
        """,
        2: """
        --------
        |      |
        |      O
        |     /|\\
        |
        |
        _______
        """,
        1: """
        --------
        |      |
        |      O
        |     /|\\
        |     /
        |
        _______
        """,
        0:"""
        --------
        |      |
        |      O
        |     /|\\
        |     /\\
        |
        _______
        """
        }

# Functions are defined here.

# Number of players input is checked for validity.
def check_num_players(input):
    if input.isnumeric() and int(input) in range(1, 7):
        return True
    else:
        return False
    
def check_word(word):
    for letter in word:
        if not letter.isalpha():
            return False
    return True
    
# This function handles the creation of players depending on the number that was inputted by the user.
def create_players(number):
    players = {}
    for i in range(0, int(number)):
        players[f"player{i + 1}"] = Player(input(f"Player {i + 1}, what is your name? "), i + 1)
    return players

def single_player_game_init(player):
    print(f"Welcome {player.name} You will be playing against the AI today. They will think of a word and you will guess it.")
    # The program chooses a random word from the supplied word bank and converts it to uppercase.
    word = random.choice(words_list).upper()
    game(player, word, True)    


def multiplayer_game_init(players):
    
    print("In a multiplayer game, each player will have a turn to come up with a word, and the other players will work as a team to guess the word. If you can't guess the word, the player that came up with the word will get a point.")
    # Each player is cycled through and given a chance to guess word.
    for i in range(0, len(players)):
        player_name = players[f"player{i + 1}"].name
        print(f"{player_name} will choose a word.")
        word = input("Come up with a word. no spaces or numbers: ")
        while not check_word(word):
            word = input("Invalid word entered. Try again: ")
        game(players[f"player{i + 1}"], word.upper(), False)
    print_scores(players)
    play_again(False)
    

# This function contains the main game logic, whether single or multiplayer.
def game(player, word, vs_AI):
    word_letters = set(word)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("You have guessed the following letters: ", ', '.join(used_letters))
        print(f"You have {lives} lives remaining.")

        word_list = [letter if letter in used_letters else '-' for letter in word] # Create a list of letters in the word, showing only those that have been correctly guessed to the user.
        print("Current guesses: ", ' '.join(word_list))
        print(render_gallows(lives))

        if vs_AI == True:
            print("The other players will take turns to guess letters.")
        
        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1

        elif user_letter in used_letters:
            print("You have already guessed this letter. Try again.")
    
        else:
            print("This isn't a valid character. Try again.")

    if len(word_letters) == 0:
        if vs_AI:
            print(f"Congratulations, you have guessed the word, it was: {word.lower()}. {player.name} gains a point.")
            player.winner()
            play_again(True)
        else:
            print(f"The other players guessed {player.name}'s word. {player.name} doesn't score.")
    
    else:
        print(gallows[0])
        print(f"Sorry, you ran out of lives. The word was: {word.lower()}")
        if vs_AI:
            play_again(True)
        else:
            print(f"The word was {word.lower()}. {player.name} came up with a word that you couldn't guess! They get a point.")
            player.winner()
        
        

def play_again(singleplayer): 
    if input("Play again? 'y' for yes and 'n' for no:").lower()[0] == 'y':
        if singleplayer:
            single_player_game_init(players_dict["player1"])
        else:
            multiplayer_game_init(players_dict)
    
    return

def render_gallows(lives):
    return gallows[lives]

def print_scores(players):
    for player in players.values():
        print(f"{player.name} has {player.games_won} points.")

    
# Main program code from here below.
print(words_list)
print(title)
num_players = input("How many players will there be? The maximum is 6 players: ")
while not check_num_players(num_players):
    num_players =  input("You have entered an invalid input. Please enter a number between 1 and 6: ")
# Create a dictionary containing all the players.
players_dict = create_players(num_players)

if len(players_dict) == 1:
    single_player_game_init(players_dict["player1"])
else:
    multiplayer_game_init(players_dict)




