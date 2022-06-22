# Imports

from fcntl import F_SEAL_SEAL
import random


class Pokemon(object):
    def __init__(self, name : str, moveset : list, status : dict = {'Health' : 50}) -> None:
        self.name = name
        self.moves = moveset
        self.status = status
    
    def list_all_moves(self):
        print(f"Valid moves for {self.name} are:")
        for move in self.moves:
            print(move)

    def list_status(self):
        print(f"Status of {self.name}:")
        for stat in self.status:
            print(f"{stat} = {self.status[stat]}")

    def make_move(self, move):
        if move not in self.moves: return
        print(f"{self.name} performed {move}\n")    
    
class Item(object):
    def __init__(self, name : str, effect : dict) -> None:
        self.name = name
        self.effect = effect

    def use_item(self, pokemon: Pokemon) -> None:
        for key in self.effect:
            pokemon.status[key] += self.effect[key]
        pokemon.list_status()


class Event(object):
    def __init__(self, event) -> None:
        valid_events = [
            'begin', 'end', 'back', 'list_poke', 'choose_poke', 'list_moves', 'perform_moves', 'list_items', 'use_item'
        ]
        valid_sm_events = [
            'create_item_sm', 'create_move_sm', 'destroy_sm', 'ask_pokemon', 'ask_move_item', 'ask_move', 'ask_item'
        ]
        if event in valid_events:
            self.event = event
            self.is_player_event = True
        elif event in valid_sm_events:
            self.event = event
            self.is_player_event = False
        else:
            self.event = None
            self.is_player_event = False


class StateMachineStack(object):
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.smstack = []
        self.event_queue = []
    
    def pop(self):
        return self.smstack.pop(-1)
    
    def clear_smstack(self):
        while self.smstack:
            self.smstack.pop()
    
    def push(self, sm) -> None:
        self.smstack.append(sm)
    
    def dequeue(self):
        return self.event_queue.pop(0)
    
    def enqueue(self, event: Event) -> None:
        self.event_queue.append(event)

    def start_sm(self, sm):
        self.push(sm)
    
    def stop_sm(self):
        self.pop()

    def main_loop_task(self):
        if not self.smstack: return
        if self.event_queue:
            current_event = self.dequeue()
            # print(self.event_queue)
            current_sm = self.smstack[-1]
            # Perform the event on the top state machine
            # "Propogation" will occur when player selects "end" event. Since there is only one commmand that needs to perform a propogation check, we can directly propagate this event until it reaches main (Poke_sm)
            if current_event.event == "end":
                current_sm = self.smstack[0]
            # Now perform the event
            current_sm.perform_event(current_event, self)

        self.main_loop_task()


class StateMachine(object):
    # Each state machine can push events to its stack's event queue or another stacks event queue
    def __init__(self, name, type = 0, pokemons = [], items = [], curr_pokemon : Pokemon = None) -> None:
        self.name = name                    # Name of the state machine
        self.type = type                    # type = 0(Poke_sm), 1(Move_sm), 2(Item_sm)
        self.pokemons = pokemons
        self.items = items
        self.current_pokemon = curr_pokemon

    def list_all_pokemons(self):
        print("Pokemons:")
        for poke in self.pokemons:
            print(poke.name)
        # print(f"{x.name}\n" for x in self.pokemons)
    
    def list_all_items(self):
        print("Items:\n")
        for x in self.items:
            print(x.name)
        # print(f"{x.name}\n" for x in self.items)
        
    def push_event(self, event: Event, smstack : StateMachineStack) -> None:
        smstack.enqueue(event)

    def perform_event(self, event: Event, smstack : StateMachineStack):
        '''
        All possible events
        '''
        if event.event == "ask_pokemon" and self.type == 0:
            self.list_all_pokemons()
            exit_flag = False
            while not exit_flag:
                command = self.read_event("Which pokemon do you choose?\n")
                if command == "end":
                    self.push_event(Event("end"), smstack)
                    return
                for poke in self.pokemons:
                    if command == poke.name:
                        exit_flag = True
                        self.current_pokemon = poke
                        self.push_event(Event('ask_move_item'), smstack)
        elif event.event == "ask_move_item" and self.type == 0:
            exit_flag = False
            while not exit_flag:
                command = self.read_event("Do you want to 'move' or use 'item'?\n")
                if command == "end":
                    self.push_event(Event("end"), smstack)
                    return
                if command == 'move':
                    self.push_event(Event('create_move_sm'), smstack)
                    exit_flag = True
                elif command == 'item':
                    self.push_event(Event('create_item_sm'), smstack)
                    exit_flag = True

        elif event.event == "create_move_sm" and self.type == 0:
            smstack.push(StateMachine('Move SM', type = 1, curr_pokemon=self.current_pokemon))
            self.push_event(Event('ask_move'), smstack)
        elif event.event == "create_item_sm" and self.type == 0:
            smstack.push(StateMachine('Item SM', type = 2, curr_pokemon=self.current_pokemon, items=self.items))
            self.push_event(Event('ask_item'), smstack)
        elif event.event == "ask_move" and self.type == 1:
            self.current_pokemon.list_all_moves()
            exit_flag = False
            while not exit_flag:
                command = self.read_event("Which move do you want to choose?\n")
                if command == "end":
                    self.push_event(Event("end"), smstack)
                    return
                if command in self.current_pokemon.moves:
                    self.current_pokemon.make_move(command)
                    exit_flag = True
            self.push_event(Event('destroy_sm'), smstack)
        elif event.event == "ask_item" and self.type == 2:
            self.list_all_items()
            exit_flag = False
            while not exit_flag:
                command = self.read_event("Which item do you want to choose?\n")
                if command == "end":
                    self.push_event(Event("end"), smstack)
                    return
                for x in self.items:
                    if x.name == command:
                        x.use_item(self.current_pokemon)
                        exit_flag = True
            self.push_event(Event('destroy_sm'), smstack)
            
        elif event.event == "destroy_sm" and self.type in [1, 2]:
            smstack.stop_sm()
            self.push_event(Event('ask_move_item'), smstack)
        elif event.event == "end" and self.type == 0:
            smstack.clear_smstack()


    def read_event(self, message):
        return str(input(message)).strip()



'''
Possible stacks:
Pokemon stack - choose pokemon and next approach
Move stack - performs a move
Item stack - uses an item

Possible events:
ask_pokemon
ask_move_item
create_move_sm
create_item_sm
ask_move
ask_item
destroy_sm


'''

def main():
    engine_stack = StateMachineStack(0, 'Game Engine')
    poke_sm = StateMachine('Poke_sm', type=0)
    poke_sm.pokemons = [
        Pokemon("Charmander", moveset=['Scratch', 'Growl'], status = {'Health' : 50, }),
        Pokemon("Squirtle", moveset=['Tackle', 'Tail Whip'], status = {'Health' : 45, })
    ]
    poke_sm.items = [
        Item("Potion", effect={'Health' : 20}),
        Item("Super Potion", effect={'Health' : 50})
    ]
    engine_stack.push(poke_sm)
    engine_stack.enqueue(Event('ask_pokemon'))
    engine_stack.main_loop_task()

if __name__ == "__main__":
    main()