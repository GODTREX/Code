import random
from enum import Enum
from .roles import Role

class AIPersonality(Enum):
    TRUTHFUL = 1
    DECEIVER = 2
    RANDOM = 3

class Player:
    def __init__(self, name, role=None, is_ai=True, personality=None):
        self.name = name
        self.role = role
        self.is_alive = True
        self.is_ai = is_ai
        self.personality = personality or random.choice(list(AIPersonality))
        self.known_info = {}
    
    def ai_vote(self, game_state):
        alive_players = [p for p in game_state.players if p.is_alive]
        
        if self.role == Role.WEREWOLF:
            targets = [p for p in alive_players if p.role != Role.WEREWOLF]
            return random.choice(targets).name if targets else None
        else:
            suspicious = [p.name for p in alive_players 
                         if p.role == Role.WEREWOLF and random.random() > 0.7]
            return random.choice(suspicious) if suspicious else random.choice([p.name for p in alive_players if p != self]).name
    
    def night_action(self, game_state):
        if self.role == Role.WEREWOLF and self.is_alive:
            victims = [p for p in game_state.players 
                      if p.role != Role.WEREWOLF and p.is_alive]
            return random.choice(victims).name if victims else None
        return None