from colorama import Fore, Back, Style
import enemies
import items


class Room:
    def __init__(self, room_number, room_description, room_exits, room_enemy, room_contents, is_cleared=False):
        self.room_number = room_number
        self.room_description = room_description
        self.room_exits = room_exits
        self.room_enemy = room_enemy
        self.room_contents = room_contents
        self.isCleared = is_cleared

    def location_check(self):
        print(self.room_description)


RoomOne = Room(
    room_number=1,
    room_description=f"Blast marks and dark stains litter the walls of this room. In the center lies a robed skeleton grasping a blue potion.",
    room_exits={'s': 2, 'e': 6},
    room_enemy="none",
    room_contents=items.mana_potion
)

RoomTwo = Room(
    room_number=2,
    room_description=f"A bare stone room, with a single clay golem wandering on the far side.",
    room_exits={'n': 1, 's': 3, 'e': 7},
    room_enemy=enemies.golem,
    room_contents="none"
)

RoomThree = Room(
    room_number=3,
    room_description=f"There is a foul muck covering the floor. A group of corpses lie in the center of the room, strangely positioned. {Fore.RED}From the far side of the room, you feel a foul presence.{Style.RESET_ALL}",
    room_exits={'n': 2, 's': 4, 'e': 8},
    room_enemy=enemies.hunting_horror,
    room_contents=items.sun_talisman
)

RoomFour = Room(
    room_number=4,
    room_description=f"Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered flasks litter the floor. It appears to be an ancient alchemical storeroom.",
    room_exits={'n': 3, 's': 5, 'e': 9},
    room_enemy="none",
    room_contents=items.health_potion
)

RoomFive = Room(
    room_number=5,
    room_description=f"The room is littered with the bodies of fallen Lesser Spawn. In the center, the corpse of a long dead warrior clutches an ornate tome. {Fore.RED}Between you and the tome stands a Moon-Beast.{Style.RESET_ALL}",
    room_exits={'n': 4, 'e': 10},
    room_enemy=enemies.moon_beast,
    room_contents=items.ornate_tome
)

RoomSix = Room(
    room_number=6,
    room_description=f"This room is barren and nondescript, with only a few skeletons to keep you company.",
    room_exits={'s': 7, 'e': 11, 'w': 1},
    room_enemy="none",
    room_contents="none"
)

RoomSeven = Room(
    room_number=7,
    room_description=f"The room is empty, save for a lone pedestal holding an ancient scroll. {Fore.RED}Before you reach the pedestal, a thick tar-like liquid flows from the walls and amasses into a horrible shape.{Style.RESET_ALL}",
    room_exits={'n': 6, 's': 8, 'e': 12, 'w': 6},
    room_enemy=enemies.shoggoth,
    room_contents=items.ancient_scroll
)

RoomEight = Room(
    room_number=8,
    room_description=f"You see a bare stone room, {Fore.RED}with a single Lesser Spawn on the far side.{Style.RESET_ALL}",
    room_exits={'n': 7, 's': 9, 'e': 13, 'w': 3},
    room_enemy=enemies.lesser_spawn,
    room_contents="none"
)

RoomNine = Room(
    room_number=9,
    room_description=f"This room is barren and nondescript, with only a few skeletons to keep you company.",
    room_exits={'n': 8, 's': 10, 'e': 4, 'w': 14},
    room_enemy="none",
    room_contents="none"
)

RoomTen = Room(
    room_number=10,
    room_description=f"Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered flasks litter the floor. It appears to be an ancient alchemical storeroom.",
    room_exits={'n': 9, 'e': 15, 'w': 5},
    room_enemy="none",
    room_contents=items.mana_potion
)

RoomEleven = Room(
    room_number=11,
    room_description=f"You see a bare stone room, {Fore.RED}with a single clay golem wandering on the far side.{Style.RESET_ALL}",
    room_exits={'s': 12, 'e': 16, 'w': 6},
    room_enemy=enemies.golem,
    room_contents="none"
)

RoomTwelve = Room(
    room_number=12,
    room_description=f"Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered flasks litter the floor. It appears to be an ancient alchemical storeroom.",
    room_exits={'n': 11, 's': 13, 'e': 7, 'w': 17},
    room_enemy="none",
    room_contents=items.health_potion
)

RoomThirteen = Room(
    room_number=13,
    room_description=f"You see a barren room made of ancient stone riddled with moss and pockmarks. There seems to be no enemies or items in this room.",
    room_exits={'n': 12, 's': 14, 'e': 18, 'w': 8},
    room_enemy="none",
    room_contents="none"
)

RoomFourteen = Room(
    room_number=14,
    room_description=f"You see a bare stone room, {Fore.RED}with a single clay golem wandering on the far side.{Style.RESET_ALL}",
    room_exits={'n': 13, 's': 15, 'e': 9, 'w': 9},
    room_enemy=enemies.golem,
    room_contents="none"
)
# TODO: Rewrite room desc
RoomFifteen = Room(
    room_number=15,
    room_description=f"This room is large and ornate, with carvings of every sort adorning the walls. In the center is a large pedestal with a single Silver Key laying upon it.",
    room_exits={'n': 14, 'e': 20, 'w': 5},
    room_enemy="none",
    room_contents=items.silver_key
)

RoomSixteen = Room(
    room_number=16,
    room_description=f"This room is barren and nondescript, with only a few skeletons to keep you company.",
    room_exits={'s': 17, 'e': 21, 'w': 11},
    room_enemy="none",
    room_contents="none"
)

RoomSeventeen = Room(
    room_number=17,
    room_description=f"You see a bare stone room, {Fore.RED}with a single Lesser Spawn on the far side.{Style.RESET_ALL}",
    room_exits={'n': 17, 's': 18, 'e': 22, 'w': 12},
    room_enemy=enemies.lesser_spawn,
    room_contents="none"
)

RoomEighteen = Room(
    room_number=18,
    room_description=f"You see a bare stone room, {Fore.RED}with a single clay golem wandering on the far side.{Style.RESET_ALL}",
    room_exits={'n': 17, 's': 19, 'e': 23, 'w': 13},
    room_enemy=enemies.golem,
    room_contents=items.health_potion
)

RoomNineteen = Room(
    room_number=19,
    room_description=f"This room is barren and nondescript, with only a few skeletons to keep you company.",
    room_exits={'n': 18, 's': 20, 'e': 14, 'w': 24},
    room_enemy="none",
    room_contents="none"
)

RoomTwenty = Room(
    room_number=20,
    room_description=f"You see a bare stone room, {Fore.RED}with a single Lesser Spawn on the far side.{Style.RESET_ALL}",
    room_exits={'n': 19, 'e': 25, 'w': 15},
    room_enemy=enemies.lesser_spawn,
    room_contents="none"
)

RoomTwentyOne = Room(
    room_number=21,
    room_description=f"{Fore.RED}A stale wind sweeps past you as you enter the room.{Style.RESET_ALL} On the far side there is a pedestal with a strange book upon it. {Fore.RED}You have a feeling that you are not alone.{Style.RESET_ALL}",
    room_exits={'s': 22, 'w': 16},
    room_enemy=enemies.flying_polyp,
    room_contents=items.cursed_tome
)

RoomTwentyTwo = Room(
    room_number=22,
    room_description=f"This room is barren and nondescript, with only a few skeletons to keep you company.{Style.RESET_ALL}",
    room_exits={'n': 21, 's': 23, 'w': 17},
    room_enemy="none",
    room_contents="none"
)

RoomTwentyThree = Room(
    room_number=23,
    room_description=f"{Fore.RED}As the door creaks open, you see a rift open on the far side of the room. A horrifying figure emerges.{Style.RESET_ALL}",
    room_exits={'n': 22, 's': 24, 'w': 18},
    room_enemy=enemies.dimensional_shambler,
    room_contents=items.ancient_spellbook
)

RoomTwentyFour = Room(
    room_number=24,
    room_description=f"You see a bare stone room, {Fore.RED}with a single Lesser Spawn on the far side.{Style.RESET_ALL}",
    room_exits={'n': 23, 's': 25, 'w': 19},
    room_enemy=enemies.lesser_spawn,
    room_contents="none"
)

RoomTwentyFive = Room(
    room_number=25,
    room_description="Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered flasks litter the floor. It appears to be an ancient alchemical storeroom",
    room_exits={'n': 24, 'w': 20},
    room_enemy="none",
    room_contents=items.health_potion)

RoomTwentySix = Room(
    room_number=26,
    room_description=(
        f"{Fore.RED}{Style.BRIGHT}{Back.RED}You find yourself in the endless abyss.\n THE AVATAR OF NYARLATHOTEP HAS AWOKEN{Style.RESET_ALL}"
    ),
    room_exits={"none"},
    room_enemy=enemies.boss,
    room_contents="None"
)