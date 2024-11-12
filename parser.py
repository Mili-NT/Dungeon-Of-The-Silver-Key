import difflib

from colorama import Fore, Style


class CommandParser:
    def __init__(self):
        self.commands = {
            "inventory": self.inventory,
            "look": self.look,
            "take": self.take_item,
            "move": self.move,
        }
        self.directions = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "ne": "northeast",
    "nw": "northwest",
    "se": "southeast",
    "sw": "southwest",
    "u": "up",
    "d": "down"
}

    def parse_command(self, player, game_map, user_input):
        # Split input into command and arguments
        parts = user_input.strip().split()
        if not parts:
            print("No command entered.")
            return
        command = parts[0]
        args = parts[1:]

        if command in self.directions.keys():
            return self.move(player, game_map, command)
        # Find the closest match to the command
        possible_commands = self.commands.keys()
        closest_matches = difflib.get_close_matches(command, possible_commands, n=1, cutoff=0.6)

        if closest_matches:
            # Use the closest match if it exists
            matched_command = closest_matches[0]
            return self.commands[matched_command](player, game_map, *args)
        else:
            print(f"Unknown command: '{command}'")
    def inventory(self, player, game_map):
        return player.inventory.inspect_inventory()
    def look(self, player, game_map):
        room = game_map.room_map[player.player_location]
        description = room.room_description
        if room.isCleared:
            description += f"\n{Fore.WHITE}This room is the same as when you left it.{Style.RESET_ALL}"
        return description

    def take_item(self, player, game_map, *args):
        item = " ".join(args)
        print(item)
        room = game_map.room_map[player.player_location]


    def move(self, player, game_map, *args):
        # Use fuzzy matching for direction names
        direction = " ".join(args)
        if direction in self.directions:
            player.move(direction, game_map)

        closest_direction = difflib.get_close_matches(direction, self.directions.values(), n=1, cutoff=0.6)
        if closest_direction:
            match = closest_direction[0]
            for k,v in self.directions.items():
                if match == v:
                    player.move(k, game_map)
        else:
            print(f"Direction '{direction}' is not recognized.")