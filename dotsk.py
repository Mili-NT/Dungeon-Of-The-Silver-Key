import os
import random
from game import Player, GameMap
from colorama import Fore, Style, Back
from pyfiglet import Figlet
import tabulate
from time import sleep



#                                          Coded by Mili (Python 3.6.0, January 2019, Rewritten November 2024)
#                                          Credits to H.P. Lovecraft and r/LearnPython
# Map:
# ------------------------
# | 1 | 6 | 11 | 16 | 21 |
# |---|---|----|----|----|                                  N
# | 2 | 7 | 12 | 17 | 22 |                                W o E
# |---|---|----|----|----|                                  S
# | 3 | 8 | 13 | 18 | 23 |         ----
# |---|---|----|----|----|        | 26 | (Boss room reached by teleport, from Room 15)
# | 4 | 9 | 14 | 19 | 24 |         ----
# |---|---|----|----|----|
# | 5 | 10| 15 | 20 | 25 |
# -----------------------
# Important rooms: 3 (Miniboss), 5 (Miniboss), 7 (Miniboss), 13 (START), 15 (Key Item), 21 (Miniboss), 23 (Miniboss)
# TODO: Room code
# TODO: Item pickup in enter_room
# TODO: Inventory access
# TODO: Casting greater heal ends the game
# TODO: Going west from room 14 leads to room 9, going west from room 9 leads to room 14
# TODO: Print stats in battle

def main():
    player = Player(player_location=13)
    game_map = GameMap()

    while True:
        game_map.display(player.player_location)
        direction = input("Enter a direction (n/s/e/w): ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        player.move(direction, game_map)


if __name__ == "__main__":
    main()
