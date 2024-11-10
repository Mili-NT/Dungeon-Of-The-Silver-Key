from colorama import Fore, Style

class Move:
    def __init__(self, name, damage_range, target, move_str, cost=0, attributes=None):
        self.name = name
        self.damage_range = damage_range
        self.target = target
        self.move_str = move_str
        self.cost = cost
        self.attributes = attributes
# Player Moves
thrust = Move(
    name="thrust",
    damage_range=(25, 30),
    target="health",
    move_str=f"{Fore.GREEN}You deftly weave between the enemy's attacks, giving your sword a powerful forward thrust, dealing %dmg damage.{Style.RESET_ALL}",
)
player_slash = Move(
    name="slash",
    damage_range=(10, 65),
    target="health",
    move_str=f"{Fore.GREEN}With a prayer, you swing your sword in a recklessly wide arc, dealing %dmg damage.{Style.RESET_ALL}",
)
heal = Move(
    name="heal",
    damage_range=(25, 30),
    target="health",
    move_str=f"{Fore.GREEN}A warm light encompasses you and vigor flows back into your damaged limbs. You are healed for %dmg health.",
    cost=10,
    attributes={
        "restore": True,
        "restore_target": "health",
        "spell": True
    }
)
greater_heal = Move(
    name="greater heal",
    damage_range=(50, 60),
    target="health",
    cost=30,
    move_str=f"{Fore.GREEN}A ray of divine light falls upon you, breathing life into your damaged form... you are healed for %dmg.{Style.RESET_ALL}",
    attributes={
        "restore": True,
        "restore_target": "health",
        "spell": True
    }
)
# TODO: Figure this out, it didnt mesh well with the system of comparing targets vs restore_targets
pure_of_mind = Move(
    name="pure of mind",
    damage_range=(20, 30),
    target="mana",
    move_str=f"{Fore.GREEN}You close your eyes and chant the incantation, for a brief second you can feel a ghostly hand upon your shoulder, offering its support. Your mind is clear and you can feel your sanity returning.{Style.RESET_ALL}",
    cost=20,
    attributes={
        'restore': True,
        'restore_target': "sanity",
        'spell': True
    }
)
call_of_madness = Move(
    name="call of madness",
    damage_range=(30, 35),
    target="sanity",
    move_str=f"{Fore.GREEN}Cosmic winds cackle about you. You feel arcane power course through you. You feel... unstable. Your Mana is now %mana. Your sanity is now %sanity.{Style.RESET_ALL}",
    attributes={
        'restore': True,
        'restore_target': "mana",
        'spell': True
    }
)
void_flame = Move(
    name="void flame",
    damage_range=(35, 50),
    target="health",
    move_str=f"{Fore.GREEN}You lift a hand and chant the spell. A torrent of invisible flame pours forth from the Abyss, dealing %dmg damage.{Style.RESET_ALL}",
    cost=30,
    attributes={'spell': True}
)
# Enemy Moves

claw = Move(
    name="claw",
    damage_range=(20, 30),
    target="health",
    move_str=f"{Fore.RED}%enemy slashes at you with sharp claws, dealing %dmg damage.{Style.RESET_ALL}",
)
tear = Move(
    name="tear",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy tears into your flesh, dealing %dmg damage.{Style.RESET_ALL}",
)
unsettling_gaze = Move(
    name="unsettling gaze",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy fixes its gaze upon you and a strange force rips your flesh, dealing %dmg damage.{Style.RESET_ALL}",
)
hypnotic_gaze = Move(
    name="hypnotic gaze",
    damage_range=(10, 10),
    target="sanity",
    move_str=f"{Fore.RED}%enemy affixes you with a hypnotic gaze... you feel your mind slipping away (- %sanity sanity).{Style.RESET_ALL}",
)
bite = Move(
    name="bite",
    damage_range=(20, 30),
    target="health",
    move_str=f"{Fore.RED}%enemy bites down hard, dealing %dmg damage.{Style.RESET_ALL}",
)
snap = Move(
    name="snap",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy snaps at you with a gnarled bite, dealing %dmg damage.{Style.RESET_ALL}",
)
mutilate = Move(
    name="mutilate",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy mutilates you with a savage strike, dealing %dmg damage.{Style.RESET_ALL}",
)
dread_aura = Move(
    name="dread aura",
    damage_range=(10, 10),
    target="sanity",
    move_str=f"{Fore.RED}%enemy exudes an aura of dread, you feel your mind slipping away (- %sanity sanity).{Style.RESET_ALL}",
)
cosmic_wind = Move(
    name="cosmic wind",
    damage_range=(20, 30),
    target="health",
    move_str=f"{Fore.RED}%enemy buffets you with eldritch winds, dealing %dmg damage.{Style.RESET_ALL}",
)
tentacle_swipe = Move(
    name="tentacle swipe",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy strikes with its massive tentacles, dealing %dmg damage.{Style.RESET_ALL}",
)
foul_affliction = Move(
    name="foul affliction",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy afflicts you with a foul curse, dealing %dmg damage.{Style.RESET_ALL}",
)
unnerving_aura = Move(
    name="unnerving aura",
    damage_range=(15, 15),
    target="sanity",
    move_str=f"{Fore.RED}%enemy gives off an unspeakable aura... your mind begins to quiver (- %sanity sanity).{Style.RESET_ALL}",
)
strangle = Move(
    name="strangle",
    damage_range=(20, 30),
    target="health",
    move_str=f"{Fore.RED}%enemy strangles you with crushing force, dealing %dmg damage.{Style.RESET_ALL}",
)
curse_of_the_stars = Move(
    name="curse of the stars",
    damage_range=(20, 25),
    target="health",
    move_str=f"{Fore.RED}%enemy invokes a curse most foul, calling forth a void of twisting stars, dealing %dmg damage.{Style.RESET_ALL}"
)

eldritch_fire = Move(
    name="eldritch fire",
    damage_range=(25, 30),
    target="health",
    move_str=f"{Fore.RED}%enemy unleashes a torrent of accursed flame, dealing %dmg damage.{Style.RESET_ALL}"
)

cursed_blow = Move(
    name="cursed blow",
    damage_range=(35, 40),
    target="health",
    move_str=f"{Fore.RED}%enemy invades your very being, dealing %dmg damage.{Style.RESET_ALL}"
)

cosmic_vampirism = Move(
    name="cosmic vampirism",
    damage_range=(20, 30),
    target="health",
    move_str=f"{Fore.RED}%enemy wraps the tendrils of its mind around your heart... you feel your life force being consumed... (%enemy healed for %dmg health){Style.RESET_ALL}",
    attributes= {
        "restore": True,
        "restore_target": "health"
    }
)

gaze_of_the_abyss = Move(
    name="gaze of the abyss",
    damage_range=(30, 30),
    target="sanity",
    move_str=f"{Fore.RED}Your eyes are drawn to the endless abyss. You feel it gazing back... your sanity is under assault (- %sanity sanity).{Style.RESET_ALL}",
)
weak_slash = Move(
    name="weak slash",
    damage_range=(5, 10),
    target="health",
    move_str=f"{Fore.RED}%enemy weakly slashes at you, dealing %dmg damage.{Style.RESET_ALL}"
)
punch = Move(
    name="punch",
    damage_range=(10, 15),
    target="health",
    move_str=f"{Fore.RED}%enemy throws a strong punch, dealing %dmg damage.{Style.RESET_ALL}",
)
smash = Move(
    name="smash",
    damage_range=(10, 20),
    target="health",
    move_str=f"{Fore.RED}%enemy smashes you with their fist, dealing %dmg damage.{Style.RESET_ALL}",
)
stomp = Move(
    name="stomp",
    damage_range=(10, 15),
    target="health",
    move_str=f"{Fore.RED}%enemy stomps at you with a heavy foot, dealing %dmg damage.{Style.RESET_ALL}",
)
pummel = Move(
    name="pummel",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy pummels you with its appendage, dealing %dmg damage.{Style.RESET_ALL}",
)
engulf = Move(
    name="engulf",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy engulfs you in its gelatinous form, dealing %dmg damage.{Style.RESET_ALL}",
)
slash = Move(
    name="slash",
    damage_range=(30, 40),
    target="health",
    move_str=f"{Fore.RED}%enemy slashes at you viciously, dealing %dmg damage.{Style.RESET_ALL}",
)
eviscerate = Move(
    name="eviscerate",
    damage_range=(30, 35),
    target="health",
    move_str=f"{Fore.RED}%enemy eviscerates you with a terrible blow, dealing %dmg damage.{Style.RESET_ALL}",
)
horrific_wail = Move(
    name="horrific_wail",
    damage_range=(20, 20),
    target="sanity",
    move_str=f"{Fore.RED}%enemy lets loose a horrific wail... you feel your sanity slipping (-%sanity sanity).{Style.RESET_ALL}."
)