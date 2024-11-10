from colorama import Fore, Style

import moves
from classes import Item

ornate_tome = Item(
    item_name="Ornate Tome",
    item_description="A large, white book bound with gold thread. It must have been a holy book at some point.",
    item_damage=0,
    item_heal=0,
    stat_boost=0,
    teaches_move=moves.greater_heal,
    pickup_str=f"{Fore.GREEN}The tome glows with a peaceful light, its gold threads twining their way across your fingers. You begin to feel a bit better.\n{Style.RESET_ALL}{Fore.YELLOW}You have learned Greater Heal!\n{Style.RESET_ALL}"
)

cursed_tome = Item(
    item_name="Cursed Tome",
    item_description="A book bound in an unsettlingly familiar substance.",
    item_damage=0,
    item_heal=0,
    stat_boost=0,
    teaches_move=moves.call_of_madness,
    pickup_str=f"{Fore.GREEN}The book writhes under your touch, as if alive. A closer look at the books surface chills your blood.\n{Style.RESET_ALL}{Fore.YELLOW}You have learned call of madness!\n{Style.RESET_ALL}"
)

health_potion = Item(
    item_name="Health Potion",
    item_description="A red-hued restorative brew mixed by a skilled alchemist.",
    item_damage=0,
    item_heal=35,
    stat_boost=0
)

mana_potion = Item(
    item_name="Mana Potion",
    item_description="A deep blue potion in an ornate bottle. This must've belonged to a mage at some point.",
    item_damage=0,
    item_heal=45,
    stat_boost=0
)

ancient_scroll = Item(
    item_name="Ancient Scroll",
    item_description="An aeon-old scroll of bloodied and torn parchment. It appears to have a spell inscribed upon it.",
    item_damage=0,
    item_heal=0,
    stat_boost=0,
    teaches_move=moves.pure_of_mind,
    pickup_str=print(f"\n\n{Fore.GREEN}Madness has claimed many in this dark place, yet before it took its toll, a long-dead sorcerer had penned his final spell—a hopeful chant to push back the darkness of the dungeon.\n{Style.RESET_ALL}{Fore.YELLOW}You have learned the spell 'Pure of Mind'!{Style.RESET_ALL}\n\n")
)

ancient_spellbook = Item(
    item_name="Ancient Spellbook",
    item_description="A leather-bound spellbook containing arcane symbols and instructions.",
    item_damage=0,
    item_heal=0,
    stat_boost=0,
    teaches_move=moves.void_flame,
    pickup_str=f"\n\n{Fore.GREEN}The spellbook pulses with a supernatural heat, tongues of abyssal flames lick your fingers and yet... they do not burn.{Style.RESET_ALL}\n{Fore.YELLOW}You have learned the spell 'Void Flame'!{Style.RESET_ALL}\n\n"
)

silver_key = Item(
    item_name="Silver Key",
    item_description="A large, ornate silver key decorated with strange sigils. "
                     "On the bit, an inscription reads 'Randolph C.'... A previous owner, perhaps?",
    item_damage=0,
    item_heal=0,
    stat_boost=40
)

sun_talisman = Item(
    item_name="Sun Talisman",
    item_description="A small talisman depicting the sun. Its craftsmanship is crude, but it fills you with a sense of vigor.",
    item_damage=0,
    item_heal=0,
    stat_boost=15
)
