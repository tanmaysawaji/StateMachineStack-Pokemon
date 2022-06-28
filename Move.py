

class Move:
    def __init__(self) -> None:
        '''
        Moves have
        damage
        status effect
        target (0 self, 1 opp)
        '''
        self.damage = None
        self.effect_self = None
        self.effect_opp = None
        self.target = 1

class Scratch(Move):
    def __init__(self) -> None:
        super().__init__()
        self.damage = 40

class Tackle(Move):
    def __init__(self) -> None:
        super().__init__()
        self.damage = 40

class Growl(Move):
    def __init__(self) -> None:
        super().__init__()
        self.damage = 0
        self.effect_opp = {
            'attack' : -25
        }

class Leer(Move):
    def __init__(self) -> None:
        super().__init__()
        self.damage = 0
        self.effect_opp = {
            'defense' : -25
        }

class TailWhip(Move):
    def __init__(self) -> None:
        super().__init__()
        self.damage = 0
        self.effect_opp = {
            'defense' : -25
        }


class Gust(Move):
    def __init__(self) -> None:
        super().__init__()
        self.damage = 40