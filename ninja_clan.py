from abc import ABC, abstractmethod
from typing import Any
import random
# I treated this project like a game of rock paper scissors, implementing equal to, less than, and greater than to see which clan would win against which clan, similar to rock vs paper vs scissors. Fire beats air. Water beats fire. Wind beats water.

class NinjaClan(ABC):
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod
    def fighting_style(self):
        pass
    
    @abstractmethod
    def signature_weapon(self):
        pass
    
class FireClan(NinjaClan):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def fighting_style(self) -> str:
        return "Fire Style!"
    
    def signature_weapon(self) -> str:
        return "Flamethrower!"
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, FireClan)
    
    def __lt__(self, other: Any) -> bool:
        return isinstance(other, WaterClan)
    
    def __gt__(self, other: Any) -> bool:
        return isinstance(other, WindClan)

class WaterClan(NinjaClan):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def fighting_style(self) -> str:
        return "Water Style!"
    
    def signature_weapon(self) -> str:
        return "Water Cannon!"
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, WaterClan)
    
    def __lt__(self, other: Any) -> bool:
        return isinstance(other, WindClan)
    
    def __gt__(self, other: Any) -> bool:
        return isinstance(other, FireClan)

class WindClan(NinjaClan):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def fighting_style(self) -> str:
        return "Wind Style!"
    
    def signature_weapon(self) -> str:
        return "Air Cannon!"
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, WindClan)
    
    def __lt__(self, other: Any) -> bool:
        return isinstance(other, FireClan)
    
    def __gt__(self, other: Any) -> bool:
        return isinstance(other, WaterClan)
    

class Player:
    def __init__(self,player_name) -> None:
        self.player_name = player_name
        self.action = None
    
    def play_clan(self, ninja_clan: NinjaClan) -> NinjaClan:
        print(f"{self.player_name} attacks with their {ninja_clan.signature_weapon()}")
        return ninja_clan


def main():
    actions = [FireClan("Fire Clan"),WindClan("Wind Clan"),WaterClan("Water Clan")]
    player_one = Player(player_name=input("What is your name?: "))
    player_two = Player(player_name="CPU")
    while True:
        player_one_action = input(f"{player_one.player_name}, what action do you choose? (fire, wind, or water): ")
        if player_one_action.lower() == "fire":
            player_one.action = player_one.play_clan(actions[0])
            break
        elif player_one_action.lower() == "wind":
            player_one.action = player_one.play_clan(actions[1])
            break
        elif player_one_action.lower() == "water":
            player_one.action = player_one.play_clan(actions[2])
            break
        else:
            continue
    player_two.action = player_two.play_clan(random.choice(actions))
    if player_one.action > player_two.action:
        print(f"{player_one.player_name} wins!")
    elif player_one.action < player_two.action:
        print(f"{player_two.player_name} wins!")
    elif player_one.action == player_two.action:
        print(f"Game is a tie!")
    
    
    

if __name__ == "__main__":
    main()