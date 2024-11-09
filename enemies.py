import random
import moves
from classes import Enemy

# Minibosses
dimensional_shambler = Enemy(
    adjective="A twisted",
    name="Dimensional Shambler",
    description="Its body is twisted and ape-like, with wrinkled skin and sharp teeth. Its eyes see more than you care to think of.",
    speed=random.randint(30, 60),
    health=75,
    moves=[moves.claw, moves.tear, moves.unsettling_gaze, moves.hypnotic_gaze]
)

hunting_horror = Enemy(
    adjective="A snakelike",
    name="Hunting Horror",
    description="Its body is snakelike, and its head is malformed. Its strange form is ever-changing.",
    speed=random.randint(50, 75),
    health=75,
    moves=[moves.bite, moves.snap, moves.mutilate, moves.dread_aura]
)

flying_polyp = Enemy(
    adjective="A colossal, terrifying",
    name="Flying Polyp",
    description="An ancient alien entity, momentarily disappearing from sight every now and again as it angrily approaches you.",
    speed=random.randint(30, 60),
    health=80,
    moves=[moves.cosmic_wind, moves.tentacle_swipe, moves.foul_affliction, moves.unnerving_aura]
)

shoggoth = Enemy(
    adjective="A wandering",
    name="Shoggoth",
    description="A terrifying protoplasmic mass, an ancient servant of masters long forgotten.",
    speed=random.randint(1, 50),
    health=100,
    moves=[moves.strangle, moves.pummel, moves.engulf, moves.unsettling_gaze]
)

moon_beast = Enemy(
    adjective="A pale, toad-like",
    name="Moon-Beast",
    description="A foul stench emanates from this being.",
    speed=random.randint(1, 100),
    health=80,
    moves=[moves.claw, moves.slash, moves.eviscerate, moves.horrific_wail]
)

# Boss
boss = Enemy(
    adjective="You are stricken with hopelessness. The unspeakable",
    name="Servant of The Nameless Mist",
    description="A being of immense and terrifying power.",
    speed=200,
    health=125,
    moves=[moves.curse_of_the_stars, moves.eldritch_fire, moves.cursed_blow, moves.cosmic_vampirism, moves.gaze_of_the_abyss]
)

# Regular Enemies
lesser_spawn = Enemy(
    adjective="A malformed and hideous",
    name="Lesser Spawn",
    description="Its form is twisted and frail; it appears quite weak.",
    speed=random.randint(1, 20),
    health=50,
    moves=[moves.weak_slash, moves.punch]
)

golem = Enemy(
    adjective="A human-sized",
    name="Clay Golem",
    description="A long-abandoned construct of rogue cultists.",
    speed=random.randint(1, 50),
    health=50,
    moves=[moves.smash, moves.stomp]
)