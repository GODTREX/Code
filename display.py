import time
from colorama import Fore, Back, Style

class GameDisplay:
    @staticmethod
    def draw_character(role, size="normal"):
        if role == "Werewolf":
            if size == "small":
                return f"{Fore.RED}🔴{Style.RESET_ALL}"
            return f"""{Fore.RED}
  /\\_/\\  
 ( o.o ) 
  > ^ < {Style.RESET_ALL}"""
        else:
            if size == "small":
                return f"{Fore.GREEN}🟢{Style.RESET_ALL}"
            return f"""{Fore.GREEN}
   ___  
  (o o) 
  / ^ \\ {Style.RESET_ALL}"""

    @staticmethod
    def draw_map(players):
        print(f"\n{'Village Square':^40}")
        for player in players:
            status = " (DEAD)" if not player.is_alive else ""
            print(f"{player.name}{status:^10}")
            print(GameDisplay.draw_character(player.role.value['name']))
            print()

    @staticmethod
    def typewriter_effect(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.03)
        print()

    @staticmethod
    def kill_animation():
        frames = [
            f"{Fore.RED}•᷄⌓•᷅",
            f"{Fore.RED}•᷄⌓•᷅  claws flash!",
            f"{Fore.RED}•᷄⌓•᷅  A scream echoes!",
            f"{Fore.WHITE}{Back.RED}☠️ BODY REPORTED!{Style.RESET_ALL}"
        ]
        for frame in frames:
            print(frame)
            time.sleep(0.7)
            print("\033[F\033[K", end='')

    @staticmethod
    def show_voting_screen(candidates):
        print(f"\n{Back.YELLOW}🕵️ TIME TO VOTE{Style.RESET_ALL}")
        for i, player in enumerate(candidates):
            print(f"{i+1}. {player.name} {GameDisplay.draw_character(player.role.value['name'], 'small')}")