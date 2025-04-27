from simple_term_menu import TerminalMenu

class GameMenus:
    @staticmethod
    def player_select(players, title="Select player:"):
        return TerminalMenu(
            [p.name for p in players],
            title=title
        ).show()
    
    @staticmethod
    def action_menu(actions):
        return TerminalMenu(actions).show()