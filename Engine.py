from Pokemon import Bulbasaur, Charmander, Mankey, Pidgey, Squirtle
from State import StateMachine, Ash, Rival


class Engine(StateMachine):
    def __init__(self) -> None:
        self.turn = 0       # Turn 0:player Turn 1:Rival
        
        ash_pokemons = [
            Charmander(), Bulbasaur(), Pidgey()
        ]
        ash_items = {
            'Potion' : 1,
            'Super Potion' : 1
        }
        

        rival_pokemons = [
            Squirtle(), Mankey()
        ]
        rival_items = {
            'Potion' : 1,
            'Super Potion' : 1
        }

        player = Ash()
        rival = Rival()

        self.game_state = GameState(player, rival)


    '''
    - Start game
    - Maintain both player states
    - Calculate damage if move is performed
    - Apply status if move or item is used
    - Create player SM and Rival SM
    - End game
    '''

    def end_turn(self):
        self.turn = 1 - self.turn

    def perform_move(self, move, attacker, defender):
        pass

    def apply_status(self, pokemon, status):
        pass

    def calculate_damage(self, attack, defense, move_stat):
        pass


class GameState():
    def __init__(self, player, rival) -> None:
        self.player = player
        self.rival = rival
    
    def set_player(self, state):
        self.player = state
    
    def set_rival(self, state):
        self.rival = state

    def is_game_over(self):
        game_over = True
        for pokemon in self.player.pokemons:
            if pokemon.status['Health'] != 0:
                print('Congratulations, you won!!!')
                game_over = False
                return game_over
        for pokemon in self.rival.pokemons:
            if pokemon.status['Health'] != 0:
                print('Nice try, keep it up!!!')
                game_over = False
                return game_over
        return game_over