import random
import tabulate
from colorama import Fore, Style
from pyfiglet import Figlet
import moves
import rooms


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
        # Inventory
        self.inventory = Inventory()
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

    def add_item_to_inventory(self, item):
        if item.teaches_move:
            if item.teaches_move not in self.player_moves:
                self.player_moves.append(item.teaches_move)
        if item.pickup_str:
            print(item.pickup_str)
        self.inventory.add_item(item)
        print(f"{item.item_name} has been added to your inventory.")

    def move(self, direction, game_map):
        # Get the current room from the room_map using the player's location
        room = game_map.room_map.get(self.player_location)

        # If the room exists and the direction is valid (check if direction exists in the room's directions)
        if direction in list(room.room_exits.keys()):
            # Update the player's location based on the direction
            self.player_location = game_map.room_map.get(room.room_exits[direction]).room_number
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
        move = random.choice(enemy.enemy_moves)
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
class GameMap:
    def __init__(self):
        # Maps
        """
        This map shows all possible doors in the dungeon and prevents players from walking through the walls into nonexistent rooms.
        # TODO: room '0' for outside the dungeon, room 26 boss fight
        """
        self.room_map = {
            1: rooms.RoomOne,
            2: rooms.RoomTwo,
            3: rooms.RoomThree,
            4: rooms.RoomFour,
            5: rooms.RoomFive,
            6: rooms.RoomSix,
            7: rooms.RoomSeven,
            8: rooms.RoomEight,
            9: rooms.RoomNine,
            10: rooms.RoomTen,
            11: rooms.RoomEleven,
            12: rooms.RoomTwelve,
            13: rooms.RoomThirteen,
            14: rooms.RoomFourteen,
            15: rooms.RoomFifteen,
            16: rooms.RoomSixteen,
            17: rooms.RoomSeventeen,
            18: rooms.RoomEighteen,
            19: rooms.RoomNineteen,
            20: rooms.RoomTwenty,
            21: rooms.RoomTwentyOne,
            22: rooms.RoomTwentyTwo,
            23: rooms.RoomTwentyThree,
            24: rooms.RoomTwentyFour,
            25: rooms.RoomTwentyFive
        }
        self.game_map = [
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
            [5, 10, 15, 20, 25]
        ]
        self.rooms_cleared = {}

    def display(self, player_location, invalid_move=False):
        print(tabulate.tabulate(self.game_map, tablefmt="fancy_grid"))
        print(f"{Fore.LIGHTWHITE_EX}\n  N\nW o E\n  S")
        print(f"{Fore.YELLOW}You are in room {player_location}.")
        print(f"{Fore.LIGHTWHITE_EX}There are exits to the {list(self.room_map[player_location].room_exits.keys())}.")
        print(f"{Fore.RESET}")
