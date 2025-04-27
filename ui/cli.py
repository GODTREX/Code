from colorama import Fore, Back, Style
import questionary
from display import GameDisplay

class CLI:
    def __init__(self):
        self.game = None
    
    def start(self):
        GameDisplay.typewriter_effect(f"""{Fore.YELLOW}
        🐺 W E R E W O L F  🏚️
        
The village of Blackhollow has known peace for generations...
Until the night Farmer Jakob's flock was found slaughtered,
with human teeth marks on the bones.

Now every full moon, someone disappears.
The beast walks among you.{Style.RESET_ALL}""")
        
        input("\nPress Enter to begin your nightmare...")
        self.setup_new_game()
    
    def setup_new_game(self):
        player_count = int(questionary.text(
            "Number of players (6-12 recommended):",
            default="6"
        ).ask())
        from game.game import Game
        self.game = Game(player_count)
        self.game.run()
        
        print(f"\n{Back.BLACK}=== FINAL ROLES ===")
        for player in self.game.players:
            print(f"{player.name}: {player.role.value['name']}")
        print(Style.RESET_ALL)