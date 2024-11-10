import random
import tabulate
from colorama import Fore, Style
from pyfiglet import Figlet

import moves

class Player:
    def __init__(self, player_health=100, player_sanity=100, player_mana=100, player_speed=None,
                 player_location=None, damage_done=0, damage_taken=0, amount_healed=0,
                 sanity_lost=0, player_score=0):
        self.player_health = player_health
        self.player_sanity = player_sanity
        self.player_mana = player_mana
        self.player_speed = player_speed if player_speed is not None else random.randint(45, 100)
        self.player_location = player_location or 13
        self.player_moves = [moves.player_slash, moves.thrust, moves.heal]
        self.in_combat = False
        # Score components
        self.damage_done = damage_done
        self.damage_taken = damage_taken
        self.amount_healed = amount_healed
        self.sanity_lost = sanity_lost
        self.player_score = player_score

    def game_over(self, sanity_loss=False, victory=False):
        custom_message = Figlet(font='cyberlarge')
        game_end = custom_message.renderText("Game Over")
        self.calc_score()
        if sanity_loss:
            print(f"{Fore.RED}The darkness of the dungeon comes rushing in, a terrifying force of overwhelming power. From far away, you hear yourself cry out.{Style.RESET_ALL}")
            print(f"{Fore.RED}You have been driven to madness.{Style.RESET_ALL}")
        if victory:
            victory_message = (Figlet(font='cyberlarge').renderText("""YOU STAND VICTORIOUS"""))
            print(f"{Fore.GREEN}{victory_message}")
        print(f"{Fore.YELLOW}You did {self.damage_done} damage!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}You healed for {self.amount_healed} health!{Style.RESET_ALL}")
        print(f"{Fore.RED}You took {self.damage_taken} damage!{Style.RESET_ALL}")
        print(f"{Fore.RED}You lost {self.sanity_lost} sanity!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Your score was: {self.player_score}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{game_end}{Style.RESET_ALL}")
        exit()

    def calc_score(self):
        positives = self.damage_done + self.amount_healed
        negatives = self.damage_taken + self.sanity_lost
        self.player_score = positives - negatives

    def move(self, direction, game_map):
        room = game_map.room_map.get(self.player_location)
        if room and direction in room:
            self.player_location = room[direction]
        else:
            print(f"{Fore.YELLOW}There is no door in that direction.")
            print(f"{Fore.RESET}")

    def format_move_string(self, move, move_effect):
        """
        This function replaces placeholders in the move_str with actual values:
        - %dmg -> move_effect (damage dealt)
        - %sanity -> self.player_sanity (current sanity)
        - %mana -> self.player_mana (current mana)
        """
        move_str = move.move_str  # Get the move's descriptive string

        # Replace %dmg with the damage dealt (move_effect)
        move_str = move_str.replace('%dmg', str(move_effect))

        # Replace %sanity with the player's current sanity
        move_str = move_str.replace('%sanity', str(self.player_sanity))

        # Replace %mana with the player's current mana
        move_str = move_str.replace('%mana', str(self.player_mana))

        return move_str

    def player_turn(self, enemy):
        move = None
        while True:
            print(f"{Fore.WHITE}Select your action: {', '.join([m.name for m in self.player_moves])}{Style.RESET_ALL}")
            player_action = input(f"{Fore.WHITE}> ").lower()

            # Check if the player's action matches any move by name
            selected_move = next((m for m in self.player_moves if m.name.lower() == player_action), None)

            if selected_move is None:
                print(f"{Fore.WHITE}Please select a move available to you!{Style.RESET_ALL}")
            else:
                move = selected_move
                if move.attributes["spell"] and move.cost > self.player_mana:
                    print(f"{Fore.RED}You feel your power fail you... (not enough mana).{Style.RESET_ALL}")
                    continue
                else:
                    break
        # MOVE EFFECTS:
        move_effect = random.randint(*move.damage_range)
        if move.attributes["spell"]:
            self.player_mana -= move.cost
        if move.attributes["restore"]:
            restore_target = move.attributes["restore_target"]
            if move.target != restore_target:
                if move.target == "sanity" and restore_target == "mana":
                    self.player_sanity -= move.cost
                    self.player_mana += move.cost
                elif move.target == "health" and restore_target == "mana":
                    self.player_health -= move.cost
                    self.player_mana += move.cost
                elif move.target == "mana" and restore_target == "sanity":
                    self.player_mana -= move.cost
                    self.player_sanity += move.cost
            else:
                if restore_target == "sanity":
                    self.player_sanity += move_effect
                elif restore_target == "health":
                    self.player_health -= move_effect
                elif restore_target == "mana":
                    self.player_mana += move_effect
        else:
            enemy.health -= move_effect
        print(self.format_move_string(move, move_effect))

    def enemy_turn(self, enemy):
        move = random.choice(enemy.moves)
        move_effect = random.randint(*move.damage_range)
        if move.attributes["restore"]:
            restore_target = move.attributes["restore_target"]
            if move.target == "health" and restore_target == "health":
                self.player_health -= move.cost
                enemy.health += move.cost
            elif move.target == "mana" and restore_target == "health":
                self.player_mana -= move.cost
                enemy.health += move.cost
            elif move.target == "sanity" and restore_target == "health":
                self.player_sanity -= move.cost
                enemy.health += move.cost
        else:
            self.player_health -= move_effect
        print(self.format_move_string(move, move_effect))


    def combat(self, enemy):
        # Determine who takes the first turn based on speed
        player_turn = self.player_speed >= enemy.speed  # Player goes first if speeds are equal

        while self.player_health > 0 and enemy.health > 0:
            if player_turn:
                # Player's turn
                self.player_turn(enemy)
                player_turn = False  # Switch to enemy's turn
            else:
                # Enemy's turn
                self.enemy_turn(enemy)
                player_turn = True  # Switch to player's turn

        # End of combat check
        if self.player_health <= 0:
            print(f"{Fore.RED}You have been defeated!{Style.RESET_ALL}")
            self.game_over()
        elif self.player_sanity <= 0:
            self.game_over(sanity_loss=True)
        elif enemy.health <= 0:
            print(f"{Fore.GREEN}The enemy has been defeated!{Style.RESET_ALL}")


class Move:
    def __init__(self, name, damage_range, target, move_str, cost=0, attributes=None):
        self.name = name
        self.damage_range = damage_range
        self.target = target
        self.move_str = move_str
        self.cost = cost
        self.attributes = attributes
class Item:
    def __init__(self, item_name, item_description, item_damage, item_heal, stat_boost):
        self.item_name = item_name
        self.item_description = item_description
        self.item_damage = item_damage
        self.item_heal = item_heal
        self.stat_boost = stat_boost

    def inspect_item(self):
        print(f"This item is a {self.item_name}. It is {self.item_description}.")
        if self.item_damage > 0:
            print(f"This item does {self.item_damage} damage.")
        if self.item_heal > 0:
            print(f"This item restores {self.item_heal} health.")
        if self.stat_boost > 0:
            print(f"This item boosts your stats by {self.stat_boost}.")
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def drop_item(self, item):
        self.items[item] -= 1
        if self.items[item] <= 0:
            del self.items[item]

    def inspect_inventory(self):
        print('\t'.join(['Name', 'Description', 'Damage', 'Healing', 'Stat Boost']))
        for item, count in self.items.items():
            print(f"[{count}] {item.item_name}. {item.item_description}.")
            if item.item_damage > 0:
                print(f"This item does {item.item_damage} damage.")
            if item.item_heal > 0:
                print(f"This item restores {item.item_heal} health.")
            if item.stat_boost > 0:
                print(f"This item boosts your stats by {item.stat_boost}.")
class Enemy:
    def __init__(self, adjective, name, description, speed, health, moves):
        self.adjective = adjective
        self.name = name
        self.description = description
        self.speed = speed
        self.health = health
        self.moves = moves
class GameMap:
    def __init__(self):
        # Maps
        """
        This map shows all possible doors in the dungeon and prevents players from walking through the walls into nonexistent rooms.
        the integers are there for clarity and are not essential.
        """
        self.room_map = {
            1: {'s': 2, 'e': 6},
            2: {'n': 1, 's': 3, 'e': 7},
            3: {'n': 2, 's': 4, 'e': 8},
            4: {'n': 3, 's': 5, 'e': 9},
            5: {'n': 4, 'e': 10},
            6: {'s': 7, 'e': 11, 'w': 1},
            7: {'n': 6, 's': 8, 'e': 12, 'w': 6},
            8: {'n': 7, 's': 9, 'e': 13, 'w': 3},
            9: {'n': 8, 's': 10, 'e': 4, 'w': 14},
            10: {'n': 9, 'e': 15, 'w': 5},
            11: {'s': 12, 'e': 16, 'w': 6},
            12: {'n': 11, 's': 13, 'e': 7, 'w': 17},
            13: {'n': 12, 's': 14, 'e': 18, 'w': 8},
            14: {'n': 13, 's': 15, 'e': 9, 'w': 9},
            15: {'n': 14, 'e': 20, 'w': 5},
            16: {'s': 17, 'e': 21, 'w': 11},
            17: {'n': 17, 's': 18, 'e': 22, 'w': 12},
            18: {'n': 17, 's': 19, 'e': 23, 'w': 13},
            19: {'n': 18, 's': 20, 'e': 14, 'w': 24},
            20: {'n': 19, 'e': 25, 'w': 15},
            21: {'s': 22, 'w': 16},
            22: {'n': 21, 's': 23, 'w': 17},
            23: {'n': 22, 's': 24, 'w': 18},
            24: {'n': 23, 's': 25, 'w': 19},
            25: {'n': 24, 'w': 20}
        }
        self.overmap = [
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
            [5, 10, 15, 20, 25]
        ]
        self.rooms_cleared = {}

    def display(self, player_location, invalid_move=False):
        print(tabulate.tabulate(self.overmap, tablefmt="fancy_grid"))
        print(f"{Fore.LIGHTWHITE_EX}\n  N\nW o E\n  S")
        print(f"{Fore.YELLOW}You are in room {player_location}.")
        print(f"{Fore.LIGHTWHITE_EX}There are exits to the {list(self.room_map[player_location].keys())}.")
        print(f"{Fore.RESET}")
