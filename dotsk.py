import os

from game import Player, GameMap
from parse import CommandParser

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
# TODO: More adjustments to healing rates needed.
# TODO: Lesser spawn in room 17 autodefeated (multiple rooms)
# TODO: Golem in room 14 autodefeated
# TODO: Map potentially still wonky around room 12
# TODO: Call of Madness doesnt properly exchange sanity for mana
# TODO: pure of mind doesnt decrement mana and isnt capped at 100 sanity
# TODO: bad parser implementation -> inv doesnt match to inventory
# TODO: All items labeled as [1] in Inventory.display()
# TODO: Items autopicked up ( or not)


def main():
    player = Player(player_location=13)
    game_map = GameMap()
    command_parser = CommandParser()
    while True:
        game_map.display(player.player_location)

        command = input(">  ").lower()
        output = command_parser.parse_command(player, game_map, command)
        if output:
            print(output)


if __name__ == "__main__":
    main()
