class Item:
    def __init__(self) -> None:
        self.effect = None

class Potion(Item):
    def __init__(self) -> None:
        super().__init__()
        self.effect = {
            'health' : 20
        }

class SuperPotion(Item):
    def __init__(self) -> None:
        super().__init__()
        self.effect = {
            'health' : 50
        }