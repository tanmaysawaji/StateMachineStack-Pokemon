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
    def __init__(self, name : str, moveset : list, status : dict) -> None:
        self.name = name
        self.moveset = moveset
        self.status = status
        # self.health = health
        # self.max_health = health
        # self.attack = attack
        # self.defense = defense
    
    def list_all_moves(self):
        print(f"Valid moves for {self.name} are:")
        for move in self.moves:
            print(move)

    def list_health(self):
        print(f"Health of {self.name}: {self.status['Health']}/{self.status['Max Health']}")
        

class Charmander(Pokemon):
    def __init__(self) -> None:
        name = 'Charmander'
        moveset = ['Scratch', 'Growl']
        health = 39
        attack = 52
        defense = 43
        status = {
            'Health' : health,
            'Max Health' : health,
            'Attack' : attack,
            'Defense' : defense
        }
        super().__init__(name, moveset, status)

class Squirtle(Pokemon):
    def __init__(self) -> None:
        name = 'Squirtle'
        moveset = ['Tackle', 'Tail Whip']
        health = 44
        attack = 48
        defense = 65
        status = {
            'Health' : health,
            'Max Health' : health,
            'Attack' : attack,
            'Defense' : defense
        }
        super().__init__(name, moveset, status)

class Pidgey(Pokemon):
    def __init__(self) -> None:
        name = 'Pidgey'
        moveset = ['Tackle', 'Gust']
        health = 40
        attack = 45
        defense = 40
        status = {
            'Health' : health,
            'Max Health' : health,
            'Attack' : attack,
            'Defense' : defense
        }
        super().__init__(name, moveset, status)

class Mankey(Pokemon):
    def __init__(self) -> None:
        name = 'Mankey'
        moveset = ['Scratch', 'Leer']
        health = 40
        attack = 80
        defense = 35
        status = {
            'Health' : health,
            'Max Health' : health,
            'Attack' : attack,
            'Defense' : defense
        }
        super().__init__(name, moveset, status)

class Bulbasaur(Pokemon):
    def __init__(self) -> None:
        name = 'Bulbasaur'
        moveset = ['Tackle', 'Growl']
        health = 45
        attack = 49
        defense = 49
        status = {
            'Health' : health,
            'Max Health' : health,
            'Attack' : attack,
            'Defense' : defense
        }
        super().__init__(name, moveset, status)