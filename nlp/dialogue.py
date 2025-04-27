import random
from colorama import Fore, Back, Style
from game.characters import CHARACTERS
from game.roles import Role


class DialogueGenerator:
    def __init__(self):
        self.characters = CHARACTERS
        
    def generate(self, player, game_state):
        char = next((c for c in self.characters if c["name"] == player.name), None)
        
        if char is None:
            char = {
                "dialogue": [
                    "I don't know what to think...",
                    "Someone here isn't what they seem",
                    "We need to stick together"
                ]
            }
        
        if player.role == Role.WEREWOLF:
            template = random.choice([
                "*wiping mouth* I was... tending my sheep all night. Pay no mind to the blood.",
                "Why would {innocent} accuse me? Clearly they're the beast!",
                "*growls* I mean... cough. Just a cold!"
            ])
        else:
            template = random.choice(char["dialogue"])
        
        alive_players = [p for p in game_state.players if p.is_alive and p != player]
        if alive_players:
            replacements = {
                "{name}": random.choice(alive_players).name,
                "{innocent}": random.choice([p.name for p in alive_players if p.role == Role.VILLAGER]) or "someone"
            }
            for ph, val in replacements.items():
                template = template.replace(ph, val)
        
        return template