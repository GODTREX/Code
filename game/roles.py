from enum import Enum

class Role(Enum):
    VILLAGER = {
        "name": "Villager",
        "description": "An honest townsfolk trying to survive the night",
        "night_action": "sleeps fitfully, dreaming of safety"
    }
    WEREWOLF = {
        "name": "Werewolf",
        "description": "A bloodthirsty beast in human form",
        "night_action": "slinks through shadows with glowing eyes"
    }

    def __str__(self):
        return self.value["name"]