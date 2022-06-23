'''
Pokemon should have:
Name
Moveset
Health
Attack
Defense
'''
# TODO Change moves to actual objects instead of str
class Pokemon(object):
    def __init__(self, name : str, moveset : list, health : int, attack : int, defense : int) -> None:
        self.name = name
        self.moveset = moveset
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
    
    def list_all_moves(self):
        print(f"Valid moves for {self.name} are:")
        for move in self.moves:
            print(move)

    def list_health(self):
        print(f"Health of {self.name}: {self.health}/{self.max_health}")
        

class Charmander(Pokemon):
    def __init__(self) -> None:
        name = 'Charmander'
        moveset = ['Scratch', 'Growl', 'Ember']
        health = 39
        attack = 52
        defense = 43
        super().__init__(name, moveset, health, attack, defense)

class Squirtle(Pokemon):
    def __init__(self) -> None:
        name = 'Squirtle'
        moveset = ['Tackle', 'Tail Whip', 'Bubble']
        health = 44
        attack = 48
        defense = 65
        super().__init__(name, moveset, health, attack, defense)

class Pidgey(Pokemon):
    def __init__(self) -> None:
        name = 'Pidgey'
        moveset = ['Tackle', 'Gust']
        health = 40
        attack = 45
        defense = 40
        super().__init__(name, moveset, health, attack, defense)

class Mankey(Pokemon):
    def __init__(self) -> None:
        name = 'Mankey'
        moveset = ['Scratch', 'Leer', 'Low Kick']
        health = 40
        attack = 80
        defense = 35
        super().__init__(name, moveset, health, attack, defense)

class Bulbasaur(Pokemon):
    def __init__(self) -> None:
        name = 'Bulbasaur'
        moveset = ['Tackle', 'Growl', 'Vine Whip']
        health = 45
        attack = 49
        defense = 49
        super().__init__(name, moveset, health, attack, defense)