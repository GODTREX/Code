import random
import time
from colorama import Fore, Back, Style
from display import GameDisplay
from .player import Player
from .roles import Role
from nlp.dialogue import DialogueGenerator

class Game:
    def __init__(self, player_count=6):
        self.players = [Player(f"Player {i+1}") for i in range(player_count)]
        self.day_phase = True
        self.game_over = False
        self.dialogue = DialogueGenerator()
        self.assign_roles()
    
    def assign_roles(self):
        roles = [Role.WEREWOLF] * 2 + [Role.VILLAGER] * (len(self.players) - 2)
        random.shuffle(roles)
        for i, player in enumerate(self.players):
            player.role = roles[i]
    
    def run(self):
        print("\n" + "="*40)
        print(f"{'WEREWOLF GAME':^40}")
        print("="*40)
        print(f"Players: {', '.join(p.name for p in self.players)}")
        print("2 Werewolves are among you!\n")
        
        while not self.game_over:
            if self.day_phase:
                self.day_actions()
            else:
                self.night_actions()
            self.check_win_condition()
            self.day_phase = not self.day_phase
    
    def day_actions(self):
        GameDisplay.draw_map(self.get_alive_players())
        
        print(f"\n{Back.BLUE}🗳️ DISCUSSION PHASE{Style.RESET_ALL}")
        for player in self.get_alive_players():
            print(f"\n{player.name} says:")
            GameDisplay.typewriter_effect(self.dialogue.generate(player, self))
            time.sleep(1)

        candidates = self.get_alive_players()
        GameDisplay.show_voting_screen(candidates)
        
        while True:
            try:
                vote = int(input("\nEnter number to vote (0 to skip): "))
                if 0 <= vote <= len(candidates):
                    break
            except ValueError:
                pass
            print("Invalid choice!")
        
        if vote > 0:
            executed = candidates[vote-1]
            executed.is_alive = False
            print(f"\n{executed.name} was executed! They were a {executed.role.value['name']}.")
    
    def night_actions(self):
        print(f"\n{Fore.BLUE}🌕 The full moon rises...{Style.RESET_ALL}")
        werewolves = [p for p in self.players if p.role == Role.WEREWOLF and p.is_alive]
        victims = [p for p in self.players if p.role != Role.WEREWOLF and p.is_alive]
        
        if werewolves:
            GameDisplay.draw_map(werewolves)
            chosen = random.choice(victims)
            print(f"\n{werewolves[0].name} transforms under the moonlight!")
            GameDisplay.kill_animation()
            chosen.is_alive = False
    
    def get_alive_players(self, role=None):
        return [p for p in self.players if p.is_alive and (role is None or p.role == role)]
    
    def check_win_condition(self):
        alive_werewolves = len(self.get_alive_players(Role.WEREWOLF))
        alive_villagers = len(self.get_alive_players(Role.VILLAGER))
        
        if alive_werewolves == 0:
            print(f"\n{Back.GREEN}🎉 The villagers win! All werewolves are dead.{Style.RESET_ALL}")
            self.game_over = True
        elif alive_werewolves >= alive_villagers:
            print(f"\n{Back.RED}😈 The werewolves win! They outnumber the villagers.{Style.RESET_ALL}")
            self.game_over = True