import random
from colorama import Fore, Style, Back
from pyfiglet import Figlet
import tabulate
from time import sleep

#                                           Coded by Mili (Python 3.6.0, January 2019)
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

# Classes
class Player:
    def __init__(self, PlayerHealth, PlayerSanity, PlayerMana, player_speed, PlayerLocation, DamageDone,
                 DamageTaken, AmountHealed, SanityLost, Score):
        self.PlayerHealth = PlayerHealth
        self.PlayerMana = PlayerMana
        self.PlayerSanity = PlayerSanity
        self.player_speed = player_speed
        self.PlayerLocation = PlayerLocation
        # Following attributes are score components
        self.DamageDone = DamageDone
        self.DamageTaken = DamageTaken
        self.AmountHealed = AmountHealed
        self.SanityLost = SanityLost
        self.Score = Score


class Room:
    def __init__(self, room_number, room_description, room_directions, room_enemy, room_contents):
        self.RoomNumber = room_number
        self.RoomDescription = room_description
        self.RoomDirections = room_directions
        self.RoomEnemy = room_enemy
        self.RoomContents = room_contents

    def location_check(self):
        print(Fore.WHITE + self.RoomDescription)
        if self.RoomEnemy != "none":
            print(Fore.YELLOW + "You see a " + str(self.RoomEnemy))
        if self.RoomContents != "none":
            print(Fore.WHITE + "This room contains a " + str(self.RoomContents) + ".")

    def print_directions(self):
        print(self.RoomDirections)


class Item(object):
    def __init__(self, ItemName, ItemDescription, ItemDamage, ItemHeal, StatBoost):
        self.ItemName = ItemName
        self.ItemDescription = ItemDescription
        self.ItemDamage = ItemDamage
        self.ItemHeal = ItemHeal
        self.StatBoost = StatBoost

    def InspectItem(self):  # This  method will be used to inspect items in the inventory or on pickup
        print("This item is a " + self.ItemName + ". " + "It is " + self.ItemDescription)
        if self.ItemDamage > 0:
            print("This item does " + str(self.ItemDamage) + " damage.")
        if self.ItemHeal > 0:
            print("This item restores " + str(self.ItemHeal) + " health.")
        if self.StatBoost > 0:
            print("This item boosts your stats by " + str(self.StatBoost))


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items.update({item:1})

    def drop_item(self, item):
        self.items[item] -= 1
        if self.items[item] <= 0:
            del self.items[item]

    def InspectInventory(self):
        print('\t'.join(['Name', 'Description', 'Damage', 'Healing', 'Stat Boost']))
        for i in self.items.keys():
                print("["+str(self.items[i])+"] "+ (i.ItemName + ". " + i.ItemDescription + "."))
                print("""This item does """ + str(i.ItemDamage)+""" damage.""")
                print("""This item does """ + str(i.ItemHeal) + """ healing. """)
                print("""This item boosts all stats by """ + str(i.StatBoost))

inventory = Inventory()

class Enemy:
    def __init__(self, adjective, name, description, speed, health):
        self.adjective = adjective
        self.name = name
        self.description = description
        self.speed = speed
        self.health = health

    def MiniBossAppears(self):  # This method is used to announce the start of a non-boss fight
        print(self.adjective + " " + self.name + " appears before you. " + self.description)
        print("It's speed is " + str(self.speed) + ", your speed is " + str(player.player_speed) + ".")


# Basic utility functions to end game in various ways and display title
def SanityDrain():
    Custom_Message = Figlet(font='cyberlarge')
    GameEnd = (Custom_Message.renderText("""Game Over"""))
    print(Fore.RED + "The darkness of the dungeon comes rushing in, a terrifying force of overwhelming power. "
                     "From far away, you hear yourself cry out.")
    print(Fore.RED + "You have been driven to madness.")
    Positives = player.DamageDone + player.AmountHealed
    Negatives = player.DamageTaken + player.SanityLost
    player.Score = Positives - Negatives
    print(Fore.YELLOW + "You did " + str(player.DamageDone) + " damage!")
    print(Fore.YELLOW + "You healed for " + str(player.AmountHealed) + " health!")
    print(Fore.RED + "You took " + str(player.DamageTaken) + " damage!")
    print(Fore.RED + "You lost " + str(player.SanityLost) + " sanity!")
    print(Fore.YELLOW + "Your score was: " + str(player.Score))
    print(Fore.RED + GameEnd)
    exit()


def GameOver():
    Custom_Message = Figlet(font='cyberlarge')
    GameEnd = (Custom_Message.renderText("""Game Over"""))
    Positives = player.DamageDone + player.AmountHealed
    Negatives = player.DamageTaken + player.SanityLost
    player.Score = Positives - Negatives
    print(Fore.YELLOW + "You did " + str(player.DamageDone) + " damage!")
    print(Fore.YELLOW + "You healed for " + str(player.AmountHealed) + " health!")
    print(Fore.RED + "You took " + str(player.DamageTaken) + " damage!")
    print(Fore.RED + "You lost " + str(player.SanityLost) + " sanity!")
    print(Fore.YELLOW + "Your score was: " + str(player.Score))
    print(Fore.RED + GameEnd)
    exit()


def DisplayTitle():
    CustomTitle = Figlet(font='cyberlarge')
    CustomArt = """
    
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'

    
    """
    Title = (CustomTitle.renderText("""DUNGEON OF THE SILVER KEY"""))
    print(Fore.YELLOW + Title)
    print(Fore.WHITE + CustomArt)


def Victory():
    Victory_message = Figlet(font='cyberlarge')
    VictoryMessage = (Victory_message.renderText("""YOU STAND VICTORIOUS"""))
    print(Fore.GREEN + VictoryMessage)
    Positives = player.DamageDone + player.AmountHealed
    Negatives = player.DamageTaken + player.SanityLost
    player.Score = Positives - Negatives
    print(Fore.YELLOW + "You did " + str(player.DamageDone) + " damage!")
    print(Fore.YELLOW + "You healed for " + str(player.AmountHealed) + " health!")
    print(Fore.RED + "You took " + str(player.DamageTaken) + " damage!")
    print(Fore.RED + "You lost " + str(player.SanityLost) + " sanity!")
    print(Fore.YELLOW + "Your score was: " + str(player.Score))
    print(Fore.WHITE + """
                                        ...
                                        ...
                                        ...
    """)
    print(Fore.BLUE + """
               You hear a voice, loud and silent, swaying in an unearthly rhythm...
               """ + Fore.GREEN + Username + Fore.BLUE + """... 
               You have conquered a mighty foe, risking life and limb to prove your worth...

               Consider it acknowledged.

               For your deeds, I bid you keep that Silver Key.
               Speak my name, and it shall unlock all the doors of the cosmos.
               """)
    FinalChoice = input(Fore.WHITE + "Speak the name? Y/N: ")
    if FinalChoice.upper() == "Y":
        print(Fore.GREEN + Style.BRIGHT +
              "                         You shout to the cosmos: " + Fore.BLUE + "YOG-SOTHOTH"                         )
        print(Fore.WHITE + Style.RESET_ALL + Back.RESET +
             "The Silver Key glows with cosmic radiance and your vision fades to white... you know not what awaits you"
             " next.")
        exit()
    if FinalChoice.upper() == "N":
        print(Fore.WHITE + """
        Your vision fades to black... when you awake, you stand at the entrance to the dungeon. 
        The walls, once filled with the names of those who challenged the dungeon, are now clear, 
        save for one name... """ + Fore.YELLOW + Username)
        exit()


# Move lists for the player and all enemies

player_moves = {"Thrust": (25, 30),
                "Slash": (10, 65),
                "Heal": (25, 40)}

DimensionalShamblerMoves = {"Claw": (20, 30),
                            "Tear": (30, 35),
                            "Unsettling Gaze": (30, 35),
                            "Hypnotic Gaze": 10}

HuntingHorrorMoves = {"Bite": (20, 30),
                      "Snap": (30, 35),
                      "Mutilate": (30, 35),
                      "Dread Aura": 10
                      }

FlyingPolypMoves = {"Cosmic Wind": (20, 30),
                    "Tentacle Swipe": (30, 35),
                    "Foul Affliction": (30, 35),
                    "Unnerving Aura": 15}

ShoggothMoves = {"Strangle": (20, 30),
                 "Pummel": (30, 35),
                 "Engulf": (30, 35),
                 "Unsettling Gaze": 10}

MoonBeastMoves = {"Claw": (20, 30),
                  "Slash": (30, 40),
                  "Eviscerate": (30, 35),
                  "Horrific Wail": 20}

BossMoves = {"Curse of the Stars": (20, 25),
             "Eldritch Fire": (25, 30),
             "Cursed Blow": (35, 40),
             "Cosmic Vampirism": (20, 30),
             "Gaze of the Abyss": (30, 30)}

LesserSpawnMoves = {"Slash": (5, 10),
                    "Punch": (10, 15)}

GolemMoves = {"Smash": (10, 20),
              "Stomp": (10, 15)}


# Item Section, each item has a name, description, and three integer values: Damage, Healing, and Stat Boost

Ornate_Tome = Item("Ornate Tome", """A large, white book bound with gold thread. 
It must have been a holy book at some point.""", 0, 0, 0)
Cursed_Tome = Item("Cursed Tome", "a book bound in a most unsettlingly familiar substance.", 0, 0, 0)
Health_Potion = Item("Health Potion", "a red-hued restorative brew mixed by a skilled alchemist.",
                     0, 35, 0)

Mana_Potion = Item("Mana Potion", "a deep blue potion in an ornate bottle. This must've belonged to a mage at some"
                                  " point.", 0, 45, 0)
Ancient_Scroll = Item("Ancient Scroll", """
an aeon old scroll of bloodied and torn parchment. It appears to have a spell inscribed upon it.""", 
                      0, 0, 0)
Ancient_Spellbook = Item("Ancient Spellbook", "A leather-bound spellbook containing arcane symbols and instructions",
                         0, 0, 0)
Silver_Key = Item("Silver Key", """
a large, ornate silver key decorated with strange sigils. 
On the bit, the an inscription reads "Randolph C."... 
A previous owner, perhaps?""",0, 0, 40)
Sun_Talisman = Item("Sun Talisman", """
a small talisman depicting the sun. It's craftsmanship is crude, but it fills you with a sense of vigor.""", 0, 0, 15)

# Enemy Section

# Miniboss
DimensionalShambler = Enemy("A twisted", "Dimensional Shambler", "It's body is twisted and ape-like, with wrinkled"
                                                                 " skin and sharp teeth. It's eyes see more than you"
                                                                 " care to think of", random.randint(30, 60), 75)
# Miniboss
HuntingHorror = Enemy("A snakelike", "Hunting Horror", "It's body is snakelike and it's head is malformed. It's strange"
                                                       " form is ever-changing.", random.randint(50, 75), 75)
# Miniboss
FlyingPolyp = Enemy("A colossal, terrifying ", "Flying Polyp", "It is an ancient alien entity, momentarily "
                                                               "disappearing from sight every now and again as it "
                                                               "angrily approaches you.", random.randint(30, 60), 80)
# Miniboss
Shoggoth = Enemy("A wandering", "Shoggoth", "It is a terrifying protoplasmic mass, an "
                                            "ancient servant of masters long forgotten", random.randint(1, 50), 100)
# Miniboss
MoonBeast = Enemy("A pale, toadlike", "Moon-Beast", "A foul stench emanates from this being",
                  random.randint(1, 100), 80)
# Boss
Boss = Enemy("You are stricken with hopelessness. The unspeakable", "Servant of The Nameless Mist",
             "It is a being of immense and terrifying power", int(200), 125)
# Enemy
LesserSpawn = Enemy("A malformed and hideous ", "Lesser Spawn", "It's form is twisted and frail, it appears quite"
                                                                " weak.", random.randint(1, 20), 50)
# Enemy
Golem = Enemy("A human sized", "Clay Golem", "It is a long abandoned construct of rogue cultists.",
              random.randint(1, 50), 50)



RoomOne = Room(room_number=1, room_description="""Blast marks and dark stains litter the walls of this room. 
In the center lies a robed skeleton grasping a blue potion""", room_directions="There are doors to the [S]outh and [E]ast",
               room_enemy="none", room_contents="Mana Potion")

RoomTwo = Room(room_number=2, room_description="A bare stone room, with a single clay golem wandering on the far side.",
               room_directions="There are doors to the [N]orth and [E]ast", room_enemy="Golem", room_contents="none")

RoomThree = Room(room_number=3, room_description="There is a foul muck covering the floor. A group of corpses lie in the center"
                 " of the room, strangely positioned. From the far side of the room, you feel a foul presence.",
                 room_directions=" is a door to the [E]ast.", room_enemy="Hunting Horror", room_contents="Talisman")

RoomFour = Room(room_number=4, room_description="Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered "
                  "flasks litter the floor. It appears to be an ancient alchemical storeroom",
                room_directions="There are doors to the [S]outh and [E]ast", room_enemy="none", room_contents="Health Potion")

RoomFive = Room(room_number=5, room_description=""" The room is littered with the bodies of fallen Lesser Spawn. In the center, 
         the corpse of a long dead warrior clutches an ornate tome. Between you and the tome stands a Moon-Beast.""",
                room_directions="There are doors to the [N]orth and [E]ast", room_enemy="Moon-Beast", room_contents="Ornate Tome")

RoomSix = Room(room_number=6, room_description="This room is barren and nondescript, with only a few skeletons to keep you company.",
               room_directions="There are doors to the [S]outh, [E]ast, and [W]est", room_enemy="none", room_contents="none")

RoomSeven = Room(room_number=7, room_description=""" The room is empty, save for a lone pedestal holding an ancient
scroll. Before you reach the pedestal, a thick tar-like liquid flows from the walls and amasses into a horrible shape.""",
                 room_directions="There are doors to the [N]orth, [S]outh, [E]ast, and [W]est", room_enemy="Shoggoth", room_contents="Ancient Scroll")

RoomEight = Room(room_number=8, room_description="You see bare stone room, with a single Lesser Spawn on the far side.",
                 room_directions="There are doors to the [N]orth, [S]outh, [E]ast, and [W]est", room_enemy="Lesser Spawn", room_contents="none")

RoomNine = Room(room_number=9, room_description="This room is barren and nondescript, with only a few skeletons to keep you company.",
                room_directions="There are doors to the [S]outh, [E]ast, and [W]est", room_enemy="none", room_contents="none")

RoomTen = Room(room_number=10, room_description="Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered "
                   "flasks litter the floor. It appears to be an ancient alchemical storeroom",
               room_directions="There are doors to the [N]orth and [W]est", room_enemy="none", room_contents="Mana Potion")

RoomEleven = Room(room_number=11, room_description="You see bare stone room, with a single clay golem wandering on the far side.",
                  room_directions="There are doors to the [S]outh, [W]est, and [E]ast", room_enemy="Golem", room_contents="none")

RoomTwelve = Room(room_number=12, room_description="Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered"
                   " flasks litter the floor. It appears to be an ancient alchemical storeroom",
                  room_directions="There are doors to the [N]orth, [S]outh, [E]ast, and [W]est.", room_enemy="none", room_contents="Health Potion")

RoomThirteen = Room(room_number=13, room_description="""You see a barren room made of ancient stone riddled with moss and pockmarks. 
                  There seems to be no enemies or items in this room.""",
                    room_directions="There are door to the [N]orth, [S]outh, [E]ast, and [W]est", room_enemy="none", room_contents="none")

RoomFourteen = Room(room_number=14, room_description="You see bare stone room, with a single clay golem wandering on the far side.",
                    room_directions="There are doors to the [N]orth, [S]outh, [W]est, and [E]ast", room_enemy="Golem", room_contents="none")

RoomFifteen = Room(room_number=15, room_description="""This room is large and ornate, with carvings of every sort adorning the walls. 
                  In the center is a large pedestal with a single Silver Key laying upon it""",
                   room_directions="There is a door to the [N]orth", room_enemy="none", room_contents="Silver Key")

RoomSixteen = Room(room_number=16, room_description="This room is barren and nondescript, with only a few skeletons to keep you company.",
                   room_directions="There are doors to the [S]outh, [E]ast, and [W]est", room_enemy="none", room_contents="none")

RoomSeventeen = Room(room_number=17, room_description="You see bare stone room, with a single Lesser Spawn on the far side.",
                     room_directions="There are doors to the [N]orth, [S]outh, [E]ast, and [W]est", room_enemy="Lesser Spawn", room_contents="none")

RoomEighteen = Room(room_number=18, room_description="You see bare stone room, with a single clay golem wandering on the far side.",
                    room_directions="There are doors to the [N]orth, [S]outh, [W]est, and [E]ast", room_enemy="Golem", room_contents="Health Potion")

RoomNineteen = Room(room_number=19, room_description="This room is barren and nondescript, with only a few skeletons to keep you company.",
                    room_directions="There are doors to the [N]orth, [S]outh, [E]ast, and [W]est", room_enemy="none", room_contents="none")

RoomTwenty = Room(room_number=20, room_description="You see bare stone room, with a single Lesser Spawn on the far side.",
                  room_directions="There are doors to the [N]orth and [E]ast", room_enemy="Lesser Spawn", room_contents="none")

RoomTwentyOne = Room(room_number=21, room_description="""A stale wind sweeps past you as you enter the room. On the far side there is a pedestal "
                  "with an strange book upon it. You have a feeling that you are not alone.""",
                     room_directions="There are doors to the [S]outh and [W]est", room_enemy="Flying Polyp", room_contents="Cursed Tome")

RoomTwentyTwo = Room(room_number=22, room_description="This room is barren and nondescript, with only a few skeletons to keep you company.",
                     room_directions="There are doors to the [N]orth and [W]est", room_enemy="none", room_contents="none")

RoomTwentyThree = Room(room_number=23, room_description="As the door creaks open, you see a rift open aon the far side of the"
                  "room. A horrifying figure emerges.", room_directions="There is a door to the [W]est",
                       room_enemy="Dimensional Shambler", room_contents="Ancient Spellbook")

RoomTwentyFour = Room(room_number=24, room_description="You see bare stone room, with a single Lesser Spawn on the far side.",
                      room_directions="There are doors to the [S]outh and [W]est", room_enemy="Lesser Spawn", room_contents="none")

RoomTwentyFive = Room(room_number=25, room_description="Damaged and collapsed shelves decorate the walls, and overturned cauldrons and shattered"
                   " flasks litter the floor. It appears to be an ancient alchemical storeroom",
                      room_directions="There are doors to the [N]orth and [W]est", room_enemy="none", room_contents="Health Potion")
RoomTwentySix = Room(room_number=26, room_description=Fore.RED + Style.BRIGHT + Back.RED + """

                                        You find yourself in the endless abyss

                                        THE AVATAR OF NYARLATHOTEP HAS AWOKEN

""" + Style.RESET_ALL,
                     room_directions=Fore.WHITE + "There are no doors, there is no escape. Defeat your enemy.",
                     room_enemy="unspeakable sight", room_contents="None")


# Maps
room_map = {
        1: {'s': 2, 'e': 6},
        2: {'n': 1, 's': 3, 'e': 7},
        3: {'n': 2, 's': 4, 'e': 8},
        4: {'n': 3, 's': 5, 'e': 9},
        5: {'n': 4, 'e': 10},
        6: {'s': 7, 'e': 11, 'w': 1},
        7: {'n': 6, 's': 8, 'e': 12, 'w': 6},
        8: {'n': 7, 's': 9, 'e': 13, 'w': 3},
        9: {'n': 8, 's': 10, 'e': 4, 'w': 14},
        10: {'n': 9, 'e': 15, 'w': 5},                  # This map shows all possible doors in the dungeon and prevents
        11: {'s': 12, 'e': 16, 'w': 6},                 # players from walking through the walls into nonexistent rooms
        12: {'n': 11, 's': 13, 'e': 7, 'w': 17},        # the integers are there for clarity and are not essential
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

game_map = [[1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],  # This map is used in the PerformAction() function
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
            [5, 10, 15, 20, 25]]

# This dictionary is empty at game start, and ever time a room is cleared, it is added. If the room is in this
# dictionary, the game will not execute sanity gain, enemy combat, or item pickup code for that room

rooms_cleared = {}

# Player object

player = Player(PlayerHealth=999, PlayerSanity=999, PlayerMana=999, player_speed=random.randint(45, 100),
                PlayerLocation=RoomThirteen, DamageDone=0, DamageTaken=0, AmountHealed=0, SanityLost=0, Score=0)

# Three main functions essential to game operation. Main() is the function that changes the rooms, Game() is the
# function that determines the player location and executes code for that location accordingly, and PerformAction()
# allows the player to inspect inventory, use items, and view the map outside of combat


def Game():
    while True:
        if player.PlayerLocation == RoomOne.RoomNumber:
            RoomOneCode()
        if player.PlayerLocation == RoomTwo.RoomNumber:
            RoomTwoCode()
        if player.PlayerLocation == RoomThree.RoomNumber:
            RoomThreeCode()
        if player.PlayerLocation == RoomFour.RoomNumber:
            RoomFourCode()
        if player.PlayerLocation == RoomFive.RoomNumber:
            RoomFiveCode()
        if player.PlayerLocation == RoomSix.RoomNumber:
            RoomSixCode()
        if player.PlayerLocation == RoomSeven.RoomNumber:
            RoomSevenCode()
        if player.PlayerLocation == RoomEight.RoomNumber:
            RoomEightCode()
        if player.PlayerLocation == RoomNine.RoomNumber:
            RoomNineCode()
        if player.PlayerLocation == RoomTen.RoomNumber:
            RoomTenCode()
        if player.PlayerLocation == RoomEleven.RoomNumber:
            RoomElevenCode()
        if player.PlayerLocation == RoomTwelve.RoomNumber:
            RoomTwelveCode()
        if player.PlayerLocation == RoomThirteen.RoomNumber:
            RoomThirteenCode()
        if player.PlayerLocation == RoomFourteen.RoomNumber:
            RoomFourteenCode()
        if player.PlayerLocation == RoomFifteen.RoomNumber:
            RoomFifteenCode()
        if player.PlayerLocation == RoomSixteen.RoomNumber:
            RoomSixteenCode()
        if player.PlayerLocation == RoomSeventeen.RoomNumber:
            RoomSeventeenCode()
        if player.PlayerLocation == RoomEighteen.RoomNumber:
            RoomEighteenCode()
        if player.PlayerLocation == RoomNineteen.RoomNumber:
            RoomNineteenCode()
        if player.PlayerLocation == RoomTwenty.RoomNumber:
            RoomTwentyCode()
        if player.PlayerLocation == RoomTwentyOne.RoomNumber:
            RoomTwentyOneCode()
        if player.PlayerLocation == RoomTwentyTwo.RoomNumber:
            RoomTwentyTwoCode()
        if player.PlayerLocation == RoomTwentyThree.RoomNumber:
            RoomTwentyThreeCode()
        if player.PlayerLocation == RoomTwentyFour.RoomNumber:
            RoomTwentyFourCode()
        if player.PlayerLocation == RoomTwentyFive.RoomNumber:
            RoomTwentyFiveCode()
        if player.PlayerLocation == RoomTwentySix.RoomNumber:
            RoomTwentySixCode()


def Main():
    while True:
        MovementChoice = input(Fore.WHITE + "Choose a door: ")
        if MovementChoice.upper() == "N":
            if 'n' not in room_map[player.PlayerLocation]:  # detects if there's door in that direction using room_map
                print(Fore.YELLOW + "There is no door in that direction.")
                continue
            else:
                player.PlayerLocation -= 1
                print(Fore.YELLOW + "You are in room " + str(player.PlayerLocation))
                break
        if MovementChoice.upper() == "S":
            if 's' not in room_map[player.PlayerLocation]:
                print(Fore.YELLOW + "There is no door in that direction.")
                continue
            else:
                player.PlayerLocation += 1
                print(Fore.YELLOW + "You are in room " + str(player.PlayerLocation))
                break
        if MovementChoice.upper() == "E":
            if 'e' not in room_map[player.PlayerLocation]:
                print(Fore.YELLOW + "There is no door in that direction.")
                continue
            else:
                player.PlayerLocation += 5
                print(Fore.YELLOW + "You are in room " + str(player.PlayerLocation))
                break
        if MovementChoice.upper() == "W":
            if 'w' not in room_map[player.PlayerLocation]:
                print(Fore.YELLOW + "There is no door in that direction.")
                continue
            else:
                player.PlayerLocation -= 5
                print(Fore.YELLOW + "You are in room " + str(player.PlayerLocation))
                break
        else:
            print("Enter a valid option.")
            continue


def PerformAction():
    while True:
        ActionInput = input(Fore.WHITE + "[i]nspect inventory, [u]se item, [v]iew map, or [c]ontinue?: ")
        if ActionInput.lower() == "i":
            inventory.InspectInventory()
            while True:
                ContinueChoice = input("Anything else? Y/N: ")
                if ContinueChoice.upper() == "Y":
                    break  # go back to the loop for another action
                elif ContinueChoice.upper() == "N":
                    return  # exit the PerformAction function
                else:
                    print("Choose Y or N.")  # if invalid input, prompt again
                    continue

        elif ActionInput.lower() == "u":
            inventory.InspectInventory()
            ChooseItem = input("Select usable item: ")
            if ChooseItem.lower() == "health potion" and Health_Potion in inventory.items:
                player.PlayerHealth = player.PlayerHealth + Health_Potion.ItemHeal
                if player.PlayerHealth > 100:
                    player.PlayerHealth = 100
                print(Fore.WHITE + "Your health is now " + str(player.PlayerHealth))
                Inventory.drop_item(inventory, Health_Potion)
                while True:
                    ContinueChoice = input(Fore.WHITE + "Anything else? Y/N: ")
                    if ContinueChoice.upper() == "Y":
                        break
                    elif ContinueChoice.upper() == "N":
                        return  # exit the PerformAction function
                    else:
                        print("Choose Y or N.")  # if invalid input, prompt again
                        continue

            elif ChooseItem.lower() == "health potion" and Health_Potion not in inventory.items:
                print("Choose a usable item.")
                continue  # repeat the loop to prompt again
            elif ChooseItem.lower() == "mana potion" and Mana_Potion in inventory.items:
                player.PlayerMana = player.PlayerMana + Mana_Potion.ItemHeal
                if player.PlayerMana > 100:
                    player.PlayerMana = 100
                print(Fore.WHITE + "Your Mana is now " + str(player.PlayerMana))
                Inventory.drop_item(inventory, Mana_Potion)
                while True:
                    ContinueChoice = input(Fore.WHITE + "Anything else? Y/N: ")
                    if ContinueChoice.upper() == "Y":
                        break
                    elif ContinueChoice.upper() == "N":
                        return  # exit the PerformAction function
                    else:
                        print("Choose Y or N.")  # if invalid input, prompt again
                        continue
            elif ChooseItem.lower() == "mana potion" and Mana_Potion not in inventory.items:
                print("Choose a usable item.")
                continue  # repeat the loop to prompt again
            else:
                print(Fore.YELLOW + "Choose a usable item.")
                continue  # repeat the loop to prompt again

        elif ActionInput.lower() == "v":
            print(tabulate.tabulate(game_map, tablefmt="fancy_grid"))
            print(Fore.LIGHTWHITE_EX + """
              N
            W o E
              S
            """)
            print(Fore.YELLOW + "You are in room " + str(player.PlayerLocation))
            while True:
                ContinueChoice = input(Fore.WHITE + "Anything else? Y/N: ")
                if ContinueChoice.upper() == "Y":
                    break  # go back to the loop for another action
                elif ContinueChoice.upper() == "N":
                    return  # exit the PerformAction function
                else:
                    print("Choose Y or N.")  # if invalid input, prompt again
                    continue

        elif ActionInput.lower() == "c":
            break  # exit the PerformAction function

        else:
            print("Invalid input, try again.")  # Prompt again if input is invalid
            continue



#
# Function for each room
#
def RoomOneCode():
    if "RoomOne" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomOne.location_check()
        while True:
            ItemPickup = input("Pick up the item? Y/N: ")
            if ItemPickup.upper() == "Y":
                Inventory.add_item(inventory, Mana_Potion)
                break
            if ItemPickup.upper() == "N":
                print("You choose to leave the item where it is.")
                break
        rooms_cleared['RoomOne'] = True
        PerformAction()
        RoomOne.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomOne.print_directions()
        Main()


def RoomTwoCode():
    if "RoomTwo" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomTwo.location_check()
        Golem.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if Golem.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > Golem.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or Golem.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        # This next statement takes the tuple from the
                        # player_moves dictionary and converts it to a random value in the defined range
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")
                            break


                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print(Fore.GREEN + "The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print(Fore.YELLOW + "The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + player.PlayerMana + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                            feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                            can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                    else:
                        print("Please enter an action available to you.")
                        continue
                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(GolemMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Golem rears back and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth <= 0:
                        print(Fore.RED + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomTwo'] = True
        RoomTwo.print_directions()
        PerformAction()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwo.print_directions()
        Main()


def RoomThreeCode():
    if "RoomThree" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
        RoomThree.location_check()
        HuntingHorror.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if HuntingHorror.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > HuntingHorror.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or HuntingHorror.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        HuntingHorror.health = HuntingHorror.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if HuntingHorror.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(HuntingHorror.health))
                            enemy_turn = True
                        if HuntingHorror.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + HuntingHorror.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + HuntingHorror.name + " did not drop any items.")
                            ItemPickup = input("You see a curious talisman within the jaws of the Horror, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You reach into the creature's mouth and withdraw the talisman.")
                                Sun_Talisman.InspectItem()
                                Inventory.add_item(inventory, Sun_Talisman)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        HuntingHorror.health = HuntingHorror.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if HuntingHorror.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(HuntingHorror.health))
                            enemy_turn = True
                        if HuntingHorror.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + HuntingHorror.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + HuntingHorror.name + " did not drop any items.")
                            ItemPickup = input("You see a curious talisman within the jaws of the Horror, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You reach into the creature's mouth and withdraw the talisman.")
                                Sun_Talisman.InspectItem()
                                Inventory.add_item(inventory, Sun_Talisman)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print(Fore.WHITE + "You change your mind.")
                                    Sun_Talisman.InspectItem()
                                    Inventory.add_item(inventory, Sun_Talisman)
                                    break
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if HuntingHorror.health > 0:
                            enemy_turn = True

                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                            feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                            can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if HuntingHorror.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        HuntingHorror.health = HuntingHorror.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if HuntingHorror.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(HuntingHorror.health))
                            enemy_turn = True
                        if HuntingHorror.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + HuntingHorror.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + HuntingHorror.name + " did not drop any items.")
                            ItemPickup = input("You see a curious talisman within the jaws of the Horror, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You reach into the creature's mouth and withdraw the talisman.")
                                Sun_Talisman.InspectItem()
                                Inventory.add_item(inventory, Sun_Talisman)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print(Fore.WHITE + "You change your mind.")
                                    Sun_Talisman.InspectItem()
                                    Inventory.add_item(inventory, Sun_Talisman)
                                    break

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if HuntingHorror.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if HuntingHorror.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(HuntingHorrorMoves.items()))
                    if move == "Dread Aura":
                        enemy_damage = 10
                        print(Fore.RED + "The Hunting Horror gives off a terrible aura... "
                                         "you feel your sanity slipping.")
                        player.PlayerSanity = player.PlayerSanity - enemy_damage
                        if player.PlayerSanity < 0:
                            player.PlayerSanity = 0
                        print(Fore.YELLOW + "Your sanity is " + str(player.PlayerSanity))
                        player.SanityLost = player.SanityLost + enemy_damage
                        if player.PlayerSanity <= 0:
                            SanityDrain()

                    else:
                        enemy_damage = random.randint(*enemy_damage_range)
                        print(Fore.RED + "The Hunting Horror hisses insidiously and uses "
                                         "" + move + ", dealing " + str(enemy_damage), "damage")
                        player.PlayerHealth = player.PlayerHealth - enemy_damage
                        player.DamageTaken = player.DamageTaken + enemy_damage
                        if player.PlayerHealth < 0:
                            print(Fore.GREEN + "Your health is 0.")
                            GameOver()
                        else:
                            print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                            if player.PlayerHealth > 0:
                                player_turn = True
        rooms_cleared['RoomThree'] = True
        PerformAction()
        RoomThree.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomThree.print_directions()
        Main()


def RoomFourCode():
    if "RoomFour" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomFour.location_check()
        while True:
            ItemPickup = input(Fore.WHITE + "Pick up the item? Y/N: ")
            if ItemPickup.upper() == "Y":
                Inventory.add_item(inventory, Health_Potion)
                break
            if ItemPickup.upper() == "N":
                print("You choose to leave the item where it is.")
                break
        rooms_cleared['RoomFour'] = True
        PerformAction()
        RoomFour.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomFour.print_directions()
        Main()


def RoomFiveCode():
    if "RoomFive" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomFive.location_check()
        MoonBeast.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if MoonBeast.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > MoonBeast.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or MoonBeast.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print(Fore.YELLOW + "Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        MoonBeast.health = MoonBeast.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if MoonBeast.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(MoonBeast.health))
                            enemy_turn = True
                        if MoonBeast.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print(Fore.GREEN + "The " + MoonBeast.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print(Fore.WHITE + "The " + MoonBeast.name + " did not drop any items.")
                            while True:
                                ItemPickup = input(Fore.WHITE + "You see a skeleton grasping an ancient scroll, "
                                                                "previously obscured by the mist. Pick it up? Y/N: ")
                                if ItemPickup.upper() == "Y":
                                    print(Fore.WHITE + """
                                    The tome contains a powerful healing spell, capable of curing
                                    even the most gruesome wounds.
                                    """)
                                    player_moves["Greater Heal"] = (50, 60)
                                    print(Fore.GREEN + "You learn Greater Heal!")
                                    break
                                if ItemPickup.upper() == "N":
                                    ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                    if ItemConfirmation.upper() == "Y":
                                        print("You leave the item where it is.")
                                    if ItemConfirmation.upper() == "N":
                                        continue
                                break
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        MoonBeast.health = MoonBeast.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if MoonBeast.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(MoonBeast.health))
                            enemy_turn = True
                        if MoonBeast.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + MoonBeast.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + MoonBeast.name + " did not drop any items.")
                            while True:
                                ItemPickup = input(Fore.WHITE + "You see a skeleton grasping an ancient scroll, "
                                                                "previously obscured by the mist. Pick it up? Y/N: ")
                                if ItemPickup.upper() == "Y":
                                    print(Fore.WHITE + """
                                    The tome contains a powerful healing spell, capable of curing
                                    even the most gruesome wounds.
                                    """)
                                    player_moves["Greater Heal"] = (50, 60)
                                    print(Fore.GREEN + "You learn Greater Heal!")
                                    break
                                if ItemPickup.upper() == "N":
                                    ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                    if ItemConfirmation.upper() == "Y":
                                        print("You leave the item where it is.")
                                    if ItemConfirmation.upper() == "N":
                                        continue
                                break
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if MoonBeast.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                            feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                            can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if MoonBeast.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        MoonBeast.health = MoonBeast.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if MoonBeast.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(MoonBeast.health))
                            enemy_turn = True
                        if MoonBeast.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + MoonBeast.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + MoonBeast.name + " did not drop any items.")
                            while True:
                                ItemPickup = input(Fore.WHITE + "You see a skeleton grasping an ancient scroll, "
                                                                "previously obscured by the mist. Pick it up? Y/N: ")
                                if ItemPickup.upper() == "Y":
                                    print(Fore.WHITE + """
                                    The tome contains a powerful healing spell, capable of curing
                                    even the most gruesome wounds.
                                    """)
                                    player_moves["Greater Heal"] = (50, 60)
                                    print(Fore.GREEN + "You learn Greater Heal!")
                                    break
                                if ItemPickup.upper() == "N":
                                    ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                    if ItemConfirmation.upper() == "Y":
                                        print("You leave the item where it is.")
                                    if ItemConfirmation.upper() == "N":
                                        continue
                                break
                            break

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if MoonBeast.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerSanity < 100:
                            SanityDrain()
                        if MoonBeast.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(MoonBeastMoves.items()))
                    if move == "Horrific Wail":
                        enemy_damage = 20
                        print(Fore.RED + "The Moon-Beast gives a horrific wail... you feel your sanity slipping.")
                        player.PlayerSanity = player.PlayerSanity - enemy_damage
                        if player.PlayerSanity < 0:
                            player.PlayerSanity = 0
                        print(Fore.YELLOW + "Your sanity is " + str(player.PlayerSanity))
                        player.SanityLost = player.SanityLost + enemy_damage
                        if player.PlayerSanity <= 0:
                            SanityDrain()

                    else:
                        enemy_damage = random.randint(*enemy_damage_range)
                        print(Fore.RED + "The Moon-Beast groans unsettlingly and uses "
                              "" + move + ", dealing " + str(enemy_damage), "damage")
                        player.PlayerHealth = player.PlayerHealth - enemy_damage
                        player.DamageTaken = player.DamageTaken + enemy_damage
                        if player.PlayerHealth < 0:
                            print(Fore.GREEN + "Your health is 0.")
                            GameOver()
                        else:
                            print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                            if player.PlayerHealth > 0:
                                player_turn = True
        rooms_cleared['RoomFive'] = True
        PerformAction()
        RoomThree.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomThree.print_directions()
        Main()


def RoomSixCode():
    if "RoomSix" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        rooms_cleared['RoomSix'] = True
        RoomSix.location_check()
        PerformAction()
        RoomSix.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it""")
        PerformAction()
        RoomSix.print_directions()
        Main()


def RoomSevenCode():
    if "RoomSeven" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        RoomSeven.location_check()
        Shoggoth.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if Shoggoth.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > Shoggoth.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or Shoggoth.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        Shoggoth.health = Shoggoth.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Shoggoth.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Shoggoth.health))
                            enemy_turn = True
                        if Shoggoth.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Shoggoth.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Shoggoth.name + " did not drop any items.")
                            ItemPickup = input("You approach the pedestal that holds the scroll, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You pick up the scroll and read it's contents.")
                                print(Fore.GREEN + """
                                 Madness has claimed many in this dark place, yet before it took
                                 it's toll, a long dead sorcerer had penned his final spell- a hopeful chant to push 
                                 back the darkness of the dungeon.
                                 """)
                                print(Fore.YELLOW + "You have learned the spell Pure of Mind!")
                                player_moves["Pure of Mind"] = (20, 30)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input(Fore.WHITE + "Are you sure you wish to leave the item "
                                                                      "here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print("You change your mind.")
                                    print("You pick up the scroll and read it's contents.")
                                    print(Fore.GREEN + """
                                    Madness has claimed many in this dark place, yet before it took
                                    it's toll, a long dead sorcerer had penned his final spell- 
                                    a hopeful chant to push back the darkness of the dungeon.
                                    """)
                                    print(Fore.YELLOW + "You have learned the spell Pure of Mind!")
                                    player_moves["Pure of Mind"] = (20, 30)
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        Shoggoth.health = Shoggoth.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Shoggoth.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Shoggoth.health))
                            enemy_turn = True
                        if Shoggoth.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Shoggoth.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Shoggoth.name + " did not drop any items.")
                            ItemPickup = input("You approach the pedestal that holds the scroll, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You pick up the scroll and read it's contents.")
                                print(Fore.GREEN + """
                                Madness has claimed many in this dark place, yet before it took 
                                it's toll, a long dead sorcerer had penned his final spell- 
                                a hopeful chant to push back the darkness of the dungeon.""")
                                print(Fore.YELLOW + "You have learned the spell Pure of Mind!")
                                player_moves["Pure of Mind"] = (20, 30)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input(Fore.WHITE + "Are you sure you wish to leave the item "
                                                                      "here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print("You change your mind.")
                                    print("You pick up the scroll and read it's contents.")
                                    print(Fore.GREEN + """Madness has claimed many in this dark place, yet before it took
                                     it's toll, a long dead sorcerer had penned his final spell- 
                                     a hopeful chant to push back the darkness of the dungeon.""")
                                    print(Fore.YELLOW + "You have learned the spell Pure of Mind!")
                                    player_moves["Pure of Mind"] = (20, 30)
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Shoggoth.health > 0:
                            enemy_turn = True
                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        Shoggoth.health = Shoggoth.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Shoggoth.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Shoggoth.health))
                            enemy_turn = True
                        if Shoggoth.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Shoggoth.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Shoggoth.name + " did not drop any items.")
                            ItemPickup = input("You approach the pedestal that holds the scroll, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You pick up the scroll and read it's contents.")
                                print(Fore.GREEN +
                                """
                                Madness has claimed many in this dark place, yet before it took
                                it's toll, a long dead sorcerer had penned his final spell- a hopeful chant to push 
                                back the darkness of the dungeon.
                                """)
                                print(Fore.YELLOW + "You have learned the spell Pure of Mind!")
                                player_moves["Pure of Mind"] = (20, 30)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input(Fore.WHITE + "Are you sure you wish to leave the item "
                                                                      "here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print("You change your mind.")
                                    print("You pick up the scroll and read it's contents.")
                                    print(Fore.GREEN +
                                          """Madness has claimed many in this dark place, yet before it took
                                           it's toll, a long dead sorcerer had penned his final spell- 
                                           a hopeful chant to push back the darkness of the dungeon.""")
                                    print(Fore.YELLOW + "You have learned the spell Pure of Mind!")
                                    player_moves["Pure of Mind"] = (20, 30)

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if Shoggoth.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Shoggoth.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(ShoggothMoves.items()))
                    if move == "Unsettling Gaze":
                        enemy_damage = 10
                        print(Fore.RED + "The Shoggoth fixes its multitude of eyes upon you... you feel your sanity slipping")
                        player.PlayerSanity = player.PlayerSanity - enemy_damage
                        if player.PlayerSanity < 0:
                            player.PlayerSanity = 0
                        print(Fore.YELLOW + "Your sanity is " + str(player.PlayerSanity))
                        player.SanityLost = player.SanityLost + enemy_damage
                        if player.PlayerSanity <= 0:
                            SanityDrain()

                    else:
                        enemy_damage = random.randint(*enemy_damage_range)
                        print(Fore.RED + "The Shoggoth roils angrily and uses "
                                         "" + move + ", dealing " + str(enemy_damage), "damage")
                        player.PlayerHealth = player.PlayerHealth - enemy_damage
                        player.DamageTaken = player.DamageTaken + enemy_damage
                        if player.PlayerHealth < 0:
                            print(Fore.GREEN + "Your health is 0.")
                            GameOver()
                        else:
                            print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                            if player.PlayerHealth > 0:
                                player_turn = True
        rooms_cleared['RoomSeven'] = True
        PerformAction()
        RoomSeven.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomSeven.print_directions()
        Main()


def RoomEightCode():
    if "RoomEight" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomEight.location_check()
        LesserSpawn.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if LesserSpawn.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > LesserSpawn.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or LesserSpawn.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(LesserSpawnMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Lesser Spawn gives a furious shriek and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth < 0:
                        print(Fore.GREEN + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomEight'] = True
        PerformAction()
        RoomEight.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomEight.print_directions()
        Main()


def RoomNineCode():
    if "RoomNine" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        rooms_cleared['RoomNine'] = True
        RoomNine.location_check()
        PerformAction()
        RoomNine.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it""")
        PerformAction()
        RoomNine.print_directions()
        Main()


def RoomTenCode():
    if "RoomTen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomTen.location_check()
        while True:
            ItemPickup = input("Pick up the item? Y/N: ")
            if ItemPickup.upper() == "Y":
                Inventory.add_item(inventory, Mana_Potion)
            if ItemPickup.upper() == "N":
                print("You choose to leave the item where it is.")
            rooms_cleared['RoomTen'] = True
            break
        PerformAction()
        RoomTen.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTen.print_directions()
        Main()


def RoomElevenCode():
    if "RoomEleven" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomEleven.location_check()
        Golem.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if Golem.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > Golem.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or Golem.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print(Fore.GREEN + "The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print(Fore.YELLOW + "The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                   feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                   can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                    else:
                        print("Please enter an action available to you.")
                        continue
                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(GolemMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Golem rears back and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth <= 0:
                        print(Fore.RED + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomEleven'] = True
        PerformAction()
        RoomEleven.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomEleven.print_directions()
        Main()


def RoomTwelveCode():
    if "RoomTwelve" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomTwelve.location_check()
        while True:
            ItemPickup = input("Pick up the item? Y/N: ")
            if ItemPickup.upper() == "Y":
                Inventory.add_item(inventory, Health_Potion)
                break
            if ItemPickup.upper() == "N":
                print("You choose to leave the item where it is.")
                break
        rooms_cleared['RoomTwelve'] = True
        PerformAction()
        RoomTwelve.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwelve.print_directions()
        Main()


def RoomThirteenCode():
    if "RoomThirteen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        rooms_cleared['RoomThirteen'] = True
    RoomThirteen.location_check()
    PerformAction()
    RoomThirteen.print_directions()
    Main()


def RoomFourteenCode():
    if "RoomFourteen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomFourteen.location_check()
        Golem.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if Golem.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > Golem.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or Golem.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print(Fore.GREEN + "The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print(Fore.YELLOW + "The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True
                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                        else:
                            print("Please enter an action available to you.")
                            continue
                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(GolemMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Golem rears back and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth <= 0:
                        print(Fore.RED + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomFourteen'] = True
        PerformAction()
        RoomFourteen.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomFourteen.print_directions()
        Main()


def RoomFifteenCode():
    if "RoomFifteen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
            rooms_cleared['RoomFifteen'] = True
    RoomFifteen.location_check()
    print(Fore.WHITE + "You approach the pedestal, small flecks of cosmic energy seem to radiate off of the key.")
    if Sun_Talisman or Ancient_Scroll not in inventory.items:
        print(Fore.YELLOW + """You reach for the key, but a force demands you hesitate... visions of a sun and a scroll
                            flash through your mind. Perhaps there is still more to find in this dungeon...""")
        while True:
            ItemPickup = input(Fore.WHITE + "Pick up the key, despite your better instincts? Y/N: ")
            if ItemPickup.upper() == "Y":
                print(Fore.WHITE + "You pick up the key.")
                player.PlayerHealth = player.PlayerHealth + Silver_Key.StatBoost
                player.player_speed = player.player_speed + Silver_Key.StatBoost
                player.PlayerMana = player.PlayerMana + Silver_Key.StatBoost
                player.PlayerSanity = player.PlayerSanity + Silver_Key.StatBoost
                Silver_Key.InspectItem()
                break
            if ItemPickup.upper() == "N":
                print(Fore.WHITE +
                      """You decide to heed your instincts and stay your hand... perhaps the dungeon has some
                      items left that will aid in your journey.""")
                Main()
            else:
                print("Make your choice.")
                continue
        player.PlayerLocation = RoomTwentySix.RoomNumber
    elif Sun_Talisman and Ancient_Scroll in inventory.items:
        print("You pick up the key.")
        Silver_Key.InspectItem()
        player.PlayerLocation = RoomTwentySix.RoomNumber
    player.PlayerLocation = RoomTwentySix.RoomNumber


def RoomSixteenCode():
    if "RoomSixteen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        rooms_cleared['RoomSixteen'] = True
        RoomSixteen.location_check()
        PerformAction()
        RoomSixteen.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it""")
        PerformAction()
        RoomSixteen.print_directions()
        Main()


def RoomSeventeenCode():
    if "RoomSeventeen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomSeventeen.location_check()
        LesserSpawn.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if LesserSpawn.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > LesserSpawn.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or LesserSpawn.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                 feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                 can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(LesserSpawnMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Lesser Spawn gives a furious shriek and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth < 0:
                        print(Fore.GREEN + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomSeventeen'] = True
        PerformAction()
        RoomSeventeen.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomSeventeen.print_directions()
        Main()


def RoomEighteenCode():
    if "RoomEighteen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomEighteen.location_check()
        Golem.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if Golem.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > Golem.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or Golem.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print(Fore.GREEN + "The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print(Fore.YELLOW + "The " + Golem.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        Golem.health = Golem.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if Golem.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(Golem.health))
                            enemy_turn = True
                        if Golem.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + Golem.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + Golem.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if Golem.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if Golem.health > 0:
                            enemy_turn = True

                    else:
                        print("Please enter an action available to you.")
                        continue
                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(GolemMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Golem rears back and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth <= 0:
                        print(Fore.RED + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        ItemPickup = input("You see an ornate blue bottle on the floor. Pick it up? Y/N: ")
        if ItemPickup.upper() == "Y":
            print(Fore.GREEN + "You gain a Mana Potion!")
            inventory.add_item(Mana_Potion)
        elif ItemPickup.upper() == "N":
            print(Fore.WHITE + "You leave the item where it is.")
        rooms_cleared['RoomEighteen'] = True
        PerformAction()
        RoomEighteen.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomEighteen.print_directions()
        Main()


def RoomNineteenCode():
    if "RoomNineteen" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        rooms_cleared['RoomNineteen'] = True
        RoomNineteen.location_check()
        PerformAction()
        RoomNineteen.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it""")
        PerformAction()
        RoomNineteen.print_directions()
        Main()


def RoomTwentyCode():
    if "RoomTwenty" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomTwenty.location_check()
        LesserSpawn.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if LesserSpawn.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > LesserSpawn.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or LesserSpawn.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                 feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                 can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(LesserSpawnMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Lesser Spawn gives a furious shriek and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth < 0:
                        print(Fore.GREEN + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomTwenty'] = True
        PerformAction()
        RoomTwenty.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwenty.print_directions()
        Main()


def RoomTwentyOneCode():
    if "RoomTwentyOne" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        RoomTwentyOne.location_check()
        FlyingPolyp.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if FlyingPolyp.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > FlyingPolyp.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or FlyingPolyp.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print(Fore.YELLOW + "Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        FlyingPolyp.health = FlyingPolyp.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if FlyingPolyp.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(FlyingPolyp.health))
                            enemy_turn = True
                        if FlyingPolyp.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print(Fore.GREEN + "The " + FlyingPolyp.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print(Fore.WHITE + "The " + FlyingPolyp.name + " did not drop any items.")
                            while True:
                                ItemPickup = input(Fore.WHITE + "You approach the pedestal and inspect the ornate tome"
                                                                ". Pick it up? Y/N: ")
                                if ItemPickup.upper() == "Y":
                                    print(Fore.WHITE + "The tome contains a dark spell that can regenerate the caster's"
                                                       "Mana... at the cost of his sanity.")
                                    player_moves["Call of Madness"] = (30, 35)
                                    print(Fore.GREEN + "You learn Call of Madness!")
                                    break
                                if ItemPickup.upper() == "N":
                                    ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                    if ItemConfirmation.upper() == "Y":
                                        print("You leave the item where it is.")
                                    if ItemConfirmation.upper() == "N":
                                        continue
                                break
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        FlyingPolyp.health = FlyingPolyp.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if FlyingPolyp.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(FlyingPolyp.health))
                            enemy_turn = True
                        if FlyingPolyp.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + FlyingPolyp.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + FlyingPolyp.name + " did not drop any items.")
                            while True:
                                ItemPickup = input(Fore.WHITE + "You approach the pedestal and inspect the ornate tome"
                                                                ". Pick it up? Y/N: ")
                                if ItemPickup.upper() == "Y":
                                    print(Fore.WHITE + "The tome contains a dark spell that can regenerate the caster's"
                                                       "Mana... at the cost of his sanity.")
                                    player_moves["Call of Madness"] = (30, 35)
                                    print(Fore.GREEN + "You learn Call of Madness!")
                                    break
                                if ItemPickup.upper() == "N":
                                    ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                    if ItemConfirmation.upper() == "Y":
                                        print("You leave the item where it is.")
                                    if ItemConfirmation.upper() == "N":
                                        continue
                                break
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if FlyingPolyp.health > 0:
                            enemy_turn = True
                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                    feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                    can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if FlyingPolyp.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        FlyingPolyp.health = FlyingPolyp.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if FlyingPolyp.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(FlyingPolyp.health))
                            enemy_turn = True
                        if FlyingPolyp.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + FlyingPolyp.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + FlyingPolyp.name + " did not drop any items.")
                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(
                            Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                         "from the Abyss, dealing ", str(player_damage), " damage.")
                        FlyingPolyp.health = FlyingPolyp.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if FlyingPolyp.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(FlyingPolyp.health))
                            enemy_turn = True
                        if FlyingPolyp.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + FlyingPolyp.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + FlyingPolyp.name + " did not drop any items.")
                            while True:
                                ItemPickup = input(Fore.WHITE + "You approach the pedestal and inspect the ornate tome"
                                                                ". Pick it up? Y/N: ")
                                if ItemPickup.upper() == "Y":
                                    print(Fore.WHITE + "The tome contains a dark spell that can regenerate the caster's"
                                                       "Mana... at the cost of his sanity.")
                                    player_moves["Call of Madness"] = (30, 35)
                                    print(Fore.GREEN + "You learn Call of Madness!")
                                    break
                                if ItemPickup.upper() == "N":
                                    ItemConfirmation = input("Are you sure you wish to leave the item here? Y/N: ")
                                    if ItemConfirmation.upper() == "Y":
                                        print("You leave the item where it is.")
                                    if ItemConfirmation.upper() == "N":
                                        continue
                                break
                            break

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if FlyingPolyp.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(FlyingPolypMoves.items()))
                    if move == "Unnerving Aura":
                        enemy_damage = 15
                        print(Fore.RED + "The Flying Polyp gives an unspeakable aura... you feel your sanity slipping.")
                        player.PlayerSanity = player.PlayerSanity - enemy_damage
                        if player.PlayerSanity < 0:
                            player.PlayerSanity = 0
                        print(Fore.YELLOW + "Your sanity is " + str(player.PlayerSanity))
                        player.SanityLost = player.SanityLost + enemy_damage
                        if player.PlayerSanity <= 0:
                            SanityDrain()

                    else:
                        enemy_damage = random.randint(*enemy_damage_range)
                        print(Fore.RED + "The Flying Polyp writhes hideously and uses "
                                         "" + move + ", dealing " + str(enemy_damage), "damage")
                        player.PlayerHealth = player.PlayerHealth - enemy_damage
                        player.DamageTaken = player.DamageTaken + enemy_damage
                        if player.PlayerHealth < 0:
                            print(Fore.GREEN + "Your health is 0.")
                            GameOver()
                        else:
                            print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                            if player.PlayerHealth > 0:
                                player_turn = True
        rooms_cleared['RoomTwentyOne'] = True
        PerformAction()
        RoomTwentyOne.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwentyOne.print_directions()
        Main()


def RoomTwentyTwoCode():
    if "RoomTwentyTwo" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        rooms_cleared['RoomTwentyTwo'] = True
        RoomTwentyTwo.location_check()
        PerformAction()
        RoomTwentyTwo.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it""")
        PerformAction()
        RoomTwentyTwo.print_directions()
        Main()


def RoomTwentyThreeCode():
    if "RoomTwentyThree" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before")
        RoomTwentyThree.location_check()
        DimensionalShambler.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if DimensionalShambler.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > DimensionalShambler.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or DimensionalShambler.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        DimensionalShambler.health = DimensionalShambler.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if DimensionalShambler.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(DimensionalShambler.health))
                            enemy_turn = True
                        if DimensionalShambler.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + DimensionalShambler.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + DimensionalShambler.name + " did not drop any items.")
                            ItemPickup = input("You approach the skeleton grasping the spellbook, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You pick up the spellbook and read it's contents.")
                                print(Fore.GREEN + """
                                It is a spellbook that teaches the user to summon forth a powerful torrent of invisible 
                                flames from the abyss, searing the target's soul.
                                """)
                                print(Fore.YELLOW + "You have learned the spell Void Flame!")
                                player_moves["Void Flame"] = (35, 50)(35, 50)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input(Fore.WHITE + "Are you sure you wish to leave the item "
                                                                      "here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print("You change your mind.")
                                    print("You pick up the spellbook and read it's contents.")
                                    print(Fore.GREEN + """
                                    It is a spellbook that teaches the user to summon forth a powerful torrent of 
                                    invisible flames from the abyss, searing the target's soul.
                                    """)
                                    print(Fore.YELLOW + "You have learned the spell Void Flame!")
                                    player_moves["Void Flame"] = (35, 50)
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        DimensionalShambler.health = DimensionalShambler.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if DimensionalShambler.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(DimensionalShambler.health))
                            enemy_turn = True
                        if DimensionalShambler.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + DimensionalShambler.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + DimensionalShambler.name + " did not drop any items.")
                            ItemPickup = input("You approach the skeleton grasping the spellbook, "
                                               "take it? Y/N: ")
                            if ItemPickup.upper() == "Y":
                                print("You pick up the spellbook and read it's contents.")
                                print(Fore.GREEN + """
                                It is a spellbook that teaches the user to summon forth a powerful torrent of invisible 
                                flames from the abyss, searing the target's soul.
                                """)
                                print(Fore.YELLOW + "You have learned the spell Void Flame!")
                                player_moves["Void Flame"] = (35, 50)
                            if ItemPickup.upper() == "N":
                                ItemConfirmation = input(Fore.WHITE + "Are you sure you wish to leave the item "
                                                                      "here? Y/N: ")
                                if ItemConfirmation.upper() == "Y":
                                    print("You leave the item where it is.")
                                    break
                                if ItemConfirmation.upper() == "N":
                                    print("You change your mind.")
                                    print("You pick up the spellbook and read it's contents.")
                                    print(Fore.GREEN + """
                                    It is a spellbook that teaches the user to summon forth a powerful torrent of 
                                    invisible flames from the abyss, searing the target's soul.
                                    """)
                                    print(Fore.YELLOW + "You have learned the spell Void Flame!")
                                    player_moves["Void Flame"] = (35, 50)
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if DimensionalShambler.health > 0:
                            enemy_turn = True

                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                                    feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                                    can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if DimensionalShambler.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if DimensionalShambler.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if DimensionalShambler.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(DimensionalShamblerMoves.items()))
                    if move == "Hypnotic Gaze":
                        enemy_damage = 10
                        print(
                            Fore.RED + "The Shambler affixes you with a hypnotic Gaze... you feel your sanity slipping")
                        player.PlayerSanity = player.PlayerSanity - enemy_damage
                        if player.PlayerSanity < 0:
                            player.PlayerSanity = 0
                        print(Fore.YELLOW + "Your sanity is " + str(player.PlayerSanity))
                        player.SanityLost = player.SanityLost + enemy_damage
                        if player.PlayerSanity <= 0:
                            SanityDrain()

                    else:
                        enemy_damage = random.randint(*enemy_damage_range)
                        print(Fore.RED + "The Dimensional Shambler howls and uses "
                                         "" + move + ", dealing " + str(enemy_damage), "damage")
                        player.PlayerHealth = player.PlayerHealth - enemy_damage
                        player.DamageTaken = player.DamageTaken + enemy_damage
                        if player.PlayerHealth < 0:
                            print(Fore.GREEN + "Your health is 0.")
                            GameOver()
                        else:
                            print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                            if player.PlayerHealth > 0:
                                player_turn = True
        rooms_cleared['RoomTwentyThree'] = True
        PerformAction()
        RoomTwentyThree.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwentyThree.print_directions()
        Main()


def RoomTwentyFourCode():
    if "RoomTwentyFour" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomTwenty.location_check()
        LesserSpawn.MiniBossAppears()
        CombatOngoing = True
        while CombatOngoing:  # combat starts
            if LesserSpawn.speed > player.player_speed:
                player_turn = False
                enemy_turn = True
            elif player.player_speed > LesserSpawn.speed:
                player_turn = True
                enemy_turn = False
            if not enemy_turn:
                player_turn = True
            if not player_turn:
                enemy_turn = True
            while player.PlayerHealth > 0 or LesserSpawn.health > 0:
                if player_turn:
                    print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                    player_action = input(Fore.WHITE + "> ")
                    if player_action not in player_moves:
                        print("Please select a move available to you!")
                        continue
                    if player_action.lower() == "thrust":
                        player_action = player_moves["Thrust"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                           " forward thrust, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "slash":
                        player_action = player_moves["Slash"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                              , str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")
                            break
                    elif player_action.lower() == "heal":
                        if player.PlayerMana < 10:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                           "You are healed for ", str(player_damage), " health.")
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 10
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action == "Pure of Mind":
                        if player.PlayerMana < 20:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_action = player_moves["Pure of Mind"]
                        player.PlayerMana = player.PlayerMana - 20
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        player_damage = random.randint(*player_action)
                        print(
                            Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                 feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                 can feel your sanity returning.""")
                        player.PlayerSanity = player.PlayerSanity + player_damage
                        if player.PlayerSanity > 100:
                            player.PlayerSanity = 100
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "void flame":
                        player_action = player_moves["Void Flame"]
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You don't have enough Mana!")
                            continue
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana - 30
                        print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                        print(Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours "
                                           "forth from the Abyss, dealing ", str(player_damage), " damage.")
                        LesserSpawn.health = LesserSpawn.health - player_damage
                        player.DamageDone = player.DamageDone + player_damage
                        if LesserSpawn.health > 0:
                            print(Fore.RED + "The enemy's health is " + str(LesserSpawn.health))
                            enemy_turn = True
                        if LesserSpawn.health < 0:
                            print(Fore.RED + "The enemy's health is 0.")
                            CombatOngoing = False
                            DropChance = random.randrange(5)
                            if DropChance >= 3:
                                print("The " + LesserSpawn.name + " drops a health potion!")
                                inventory.add_item(Health_Potion)
                            if DropChance < 3:
                                print("The " + LesserSpawn.name + " did not drop any items.")

                    elif player_action.lower() == "call of madness":
                        if player.PlayerSanity < 35:
                            SanityDrain()
                        player_action = player_moves["Call of Madness"]
                        player_damage = random.randint(*player_action)
                        player.PlayerMana = player.PlayerMana + player_damage
                        player.PlayerSanity = player.PlayerSanity - player_damage
                        if player.PlayerMana > 100:
                            player.PlayerMana = 100
                        print(
                            Fore.GREEN + """Cosmic winds cackle about you. You feel arcane power course through you.
                             You feel... unstable.""")
                        print(Fore.GREEN + "Your Mana is now " + str(player.PlayerMana))
                        print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                    elif player_action.lower() == "greater heal":
                        if player.PlayerMana < 30:
                            print(Fore.RED + "You have no Mana remaining!")
                            continue
                        player_action = player_moves["Greater Heal"]
                        player_damage = random.randint(*player_action)
                        print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                         form... you are healed for """ + str(player_damage))
                        player.PlayerHealth = player.PlayerHealth + player_damage
                        player.AmountHealed = player.AmountHealed + player_damage
                        player.PlayerMana = player.PlayerMana - 30
                        if player.PlayerMana < 0:
                            player.PlayerMana = 0
                        print("You have " + str(player.PlayerMana) + " Mana remaining.")
                        if player.PlayerHealth > 100:
                            player.PlayerHealth = 100
                        print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                        if LesserSpawn.health > 0:
                            enemy_turn = True

                if enemy_turn:
                    move, enemy_damage_range = random.choice(list(LesserSpawnMoves.items()))
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Lesser Spawn gives a furious shriek and uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth < 0:
                        print(Fore.GREEN + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
        rooms_cleared['RoomTwentyFour'] = True
        PerformAction()
        RoomTwentyFour.print_directions()
        Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwentyFour.print_directions()
        Main()


def RoomTwentyFiveCode():
    if "RoomTwentyFive" not in rooms_cleared:
        if player.PlayerSanity < 100:
            player.PlayerSanity = player.PlayerSanity + 5
            if player.PlayerSanity > 100:
                player.PlayerSanity = 100
            print(Fore.GREEN + "Your mind feels a little more stable than before...")
        RoomTwentyFive.location_check()
        while True:
            ItemPickup = input(Fore.WHITE + "Pick up the item? Y/N: ")
            if ItemPickup.upper() == "Y":
                Inventory.add_item(inventory, Health_Potion)
            if ItemPickup.upper() == "N":
                print("You choose to leave the item where it is.")
            rooms_cleared['RoomTwentyFive'] = True
            PerformAction()
            RoomTwentyFive.print_directions()
            Main()
    else:
        print(Fore.WHITE + """This room is the same as when you left it.""")
        PerformAction()
        RoomTwentyFive.print_directions()


def RoomTwentySixCode():
    print(Fore.YELLOW + """

                 Bands and rays of color utterly foreign to any spectrum of the universe
                 play and weave and interlace before you, and you become conscious of 
                 a frightful velocity of motion.

                          """)
    sleep(0.5)
    print(Fore.YELLOW + """
                        You find yourself floating in the endless abyss...
                                        
    """)
    print("                                             ...                                                           ")
    sleep(1)
    print("                                             ...                                                           ")
    sleep(1)
    print("                                             ...                                                           ")
    sleep(1)
    print(Fore.RED + Style.BRIGHT + """
    
                               AN UNSPEAKABLE PRESENCE APPROACHES
    """)
    print(Fore.RED + """
          You are stricken with hopelessness. An unspeakable Servant of The Nameless Mist has appeared. 
                    It is a being of immense and terrifying power. It is unfathomably fast.""")
    print(Fore.YELLOW + "Your speed is a mere: " + str(player.player_speed))
    CombatOngoing = True
    while CombatOngoing:  # combat starts
        if Boss.speed > player.player_speed:
            player_turn = False
            enemy_turn = True
        elif player.player_speed > Boss.speed:
            player_turn = True
            enemy_turn = False
        if not enemy_turn:
            player_turn = True
        if not player_turn:
            enemy_turn = True
        while player.PlayerHealth > 0 or Boss.health > 0:
            if player_turn:
                print(Fore.WHITE + 'Select your action:', ', '.join(player_moves))
                player_action = input(Fore.WHITE + "> ")
                if player_action not in player_moves:
                    print("Please select a move available to you!")
                    continue
                if player_action.lower() == "thrust":
                    player_action = player_moves["Thrust"]
                    player_damage = random.randint(*player_action)
                    print(Fore.GREEN + "You deftly weave between the enemy's attacks, giving your sword a powerful"
                                       " forward thrust, dealing ", str(player_damage), " damage.")
                    Boss.health = Boss.health - player_damage
                    player.DamageDone = player.DamageDone + player_damage
                    if Boss.health > 0:
                        print(Fore.RED + "The enemy's health is " + str(Boss.health))
                        enemy_turn = True
                    if Boss.health < 0:
                        print(Fore.RED + "The enemy's health is 0.")
                        break
                elif player_action.lower() == "slash":
                    player_action = player_moves["Slash"]
                    player_damage = random.randint(*player_action)
                    print(Fore.GREEN + "With a prayer, you swing your sword in a recklessly wide arc, dealing "
                          , str(player_damage), " damage.")
                    Boss.health = Boss.health - player_damage
                    player.DamageDone = player.DamageDone + player_damage
                    if Boss.health > 0:
                        print(Fore.RED + "The enemy's health is " + str(Boss.health))
                        enemy_turn = True
                    if Boss.health < 0:
                        print(Fore.RED + "The enemy's health is 0.")
                        CombatOngoing = False
                        break
                elif player_action.lower() == "heal":
                    if player.PlayerMana < 10:
                        print(Fore.RED + "You have no Mana remaining!")
                        continue
                    player_action = player_moves["Heal"]
                    player_damage = random.randint(*player_action)
                    print(Fore.GREEN + "A warm light encompasses you and vigor flows back into your damaged limbs. "
                                       "You are healed for ", str(player_damage), " health.")
                    player.PlayerHealth = player.PlayerHealth + player_damage
                    player.AmountHealed = player.AmountHealed + player_damage
                    player.PlayerMana = player.PlayerMana - 10
                    if player.PlayerMana < 0:
                        player.PlayerMana = 0
                    print("You have " + str(player.PlayerMana) + " Mana remaining.")
                    if player.PlayerHealth > 100:
                        player.PlayerHealth = 100
                    print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                    if Boss.health > 0:
                        enemy_turn = True

                elif player_action == "Pure of Mind":
                    if player.PlayerMana < 20:
                        print(Fore.RED + "You don't have enough Mana!")
                        continue
                    player_action = player_moves["Pure of Mind"]
                    player.PlayerMana = player.PlayerMana - 20
                    if player.PlayerMana < 0:
                        player.PlayerMana = 0
                    print("You have " + str(player.PlayerMana) + " Mana remaining.")
                    player_damage = random.randint(*player_action)
                    print(
                        Fore.GREEN + """You close your eyes and chant the incantation, for a brief second you can 
                                                feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you 
                                                can feel your sanity returning.""")
                    player.PlayerSanity = player.PlayerSanity + player_damage
                    if player.PlayerSanity > 100:
                        player.PlayerSanity = 100
                    print(Fore.GREEN + "Your sanity is " + str(player.PlayerSanity))
                    if player.PlayerHealth > 100:
                        player.PlayerHealth = 100
                    print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                    if Boss.health > 0:
                        enemy_turn = True

                elif player_action.lower() == "void flame":
                    player_action = player_moves["Void Flame"]
                    if player.PlayerMana < 30:
                        print(Fore.RED + "You don't have enough Mana!")
                        continue
                    player_damage = random.randint(*player_action)
                    player.PlayerMana = player.PlayerMana - 30
                    print(Fore.YELLOW + "You have " + str(player.PlayerMana) + " Mana remaining.")
                    print(
                        Fore.GREEN + "You lift a hand and chant the spell. A torrent of invisible flame pours forth "
                                     "from the Abyss, dealing ", str(player_damage), " damage.")
                    Boss.health = Boss.health - player_damage
                    player.DamageDone = player.DamageDone + player_damage
                    if Boss.health > 0:
                        print(Fore.RED + "The enemy's health is " + str(Boss.health))
                        enemy_turn = True
                    if Boss.health < 0:
                        print(Fore.RED + "The enemy's health is 0.")
                        CombatOngoing = False
                        break

                elif player_action.lower() == "greater heal":
                    if player.PlayerMana < 30:
                        print(Fore.RED + "You have no Mana remaining!")
                        continue
                    player_action = player_moves["Greater Heal"]
                    player_damage = random.randint(*player_action)
                    print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                     form... you are healed for """ + str(player_damage))
                    player.PlayerHealth = player.PlayerHealth + player_damage
                    player.AmountHealed = player.AmountHealed + player_damage
                    player.PlayerMana = player.PlayerMana - 30
                    if player.PlayerMana < 0:
                        player.PlayerMana = 0
                    print("You have " + str(player.PlayerMana) + " Mana remaining.")
                    if player.PlayerHealth > 100:
                        player.PlayerHealth = 100
                    print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                    if Boss.health > 0:
                        enemy_turn = True

                elif player_action.lower() == "greater heal":
                    if player.PlayerMana < 30:
                        print(Fore.RED + "You have no Mana remaining!")
                        continue
                    player_action = player_moves["Greater Heal"]
                    player_damage = random.randint(*player_action)
                    print(Fore.GREEN + """A ray of divine light falls upon you, breathing life into your damaged 
                     form... you are healed for """ + str(player_damage))
                    player.PlayerHealth = player.PlayerHealth + player_damage
                    player.AmountHealed = player.AmountHealed + player_damage
                    player.PlayerMana = player.PlayerMana - 30
                    if player.PlayerMana < 0:
                        player.PlayerMana = 0
                    print("You have " + str(player.PlayerMana) + " Mana remaining.")
                    if player.PlayerHealth > 100:
                        player.PlayerHealth = 100
                    print(Fore.GREEN + "Your health is now " + str(player.PlayerHealth))
                    if Boss.health > 0:
                        enemy_turn = True

            if enemy_turn:
                move, enemy_damage_range = random.choice(list(BossMoves.items()))
                if move == "Gaze of The Abyss":
                    enemy_damage = 30
                    print(
                        Fore.RED + "Your eyes are drawn to the endless abyss. You feel it gazing back... "
                                   "your sanity is under assault.")
                    player.PlayerSanity = player.PlayerSanity - enemy_damage
                    if player.PlayerSanity < 0:
                        player.PlayerSanity = 0
                    print(Fore.YELLOW + "Your sanity is " + str(player.PlayerSanity))
                    player.SanityLost = player.SanityLost + enemy_damage
                    if player.PlayerSanity <= 0:
                        SanityDrain()
                elif move == "Curse of the Stars":
                    enemy_damage = 20
                    print(Fore.RED + "The servant casts a dreadful curse... you feel your life force being consumed...")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + 20
                    Boss.health = Boss.health + 20
                    print(Fore.YELLOW + "Your health is " + str(player.PlayerHealth))
                    print(Fore.YELLOW + "The servant's health is " + str(Boss.health))
                    if player.PlayerHealth < 0:
                        print(Fore.GREEN + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
                else:
                    enemy_damage = random.randint(*enemy_damage_range)
                    print(Fore.RED + "The Servant of the Nameless Mist uses "
                                     "" + move + ", dealing " + str(enemy_damage), "damage")
                    player.PlayerHealth = player.PlayerHealth - enemy_damage
                    player.DamageTaken = player.DamageTaken + enemy_damage
                    if player.PlayerHealth < 0:
                        print(Fore.GREEN + "Your health is 0.")
                        GameOver()
                    else:
                        print(Fore.GREEN + "Your health is " + str(player.PlayerHealth))
                        if player.PlayerHealth > 0:
                            player_turn = True
    print(Fore.GREEN + Style.BRIGHT + """
                            THE SERVANT OF THE NAMELESS ABYSS IS STRUCK DOWN
    """)
    Victory()
    exit()

#
# Game code starts
#

DisplayTitle()
print(Fore.WHITE +
"""The entrance to the dungeon is a large, menacing crevice. On the walls, the names and messages of those 
who came before you are visible. You decide to leave a simple note, and leave your name on the wall with those hundreds
that challenged the dungeon before you.""")
Username = input("Leave your name: ")
while True:
    EnterTheDungeon = input("Your mark has been left. Enter the dungeon? Y/N: ")
    if EnterTheDungeon.lower() == "y":
        print("You steel your resolve and descend into the abyss.")
        break

    elif EnterTheDungeon.lower() == "n":
        print("You think back to all those depending on you. Surely, you would'nt let them down so easily?")
        AreYouSure = input("Let those who are counting on you down? Y/N: ")
        if AreYouSure.lower() == "y":
            print(Fore.RED + "This world has no room for cowards such as you.")
            Player.PlayerHealth = 0
            print("You have been deemed unworthy, perhaps the world will "
                  "find a more suitable hero to conquer the dungeon.")
            GameOver()
            exit()
        elif AreYouSure.lower() == "n":
            print("The thoughts of those who depend on you bolsters your courage.")
            continue
    else:
        print("Make your choice.")
        continue

player.PlayerLocation = RoomThirteen.RoomNumber
print(tabulate.tabulate(game_map, tablefmt="fancy_grid"))
print(Fore.YELLOW + "You are in room " + str(player.PlayerLocation))
RoomThirteen.location_check()
RoomThirteen.print_directions()
Main()
Game()
