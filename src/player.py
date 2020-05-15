# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
        self.bag = []

    def move_player(self, command):
        print(f'MOVE THIS PLAYER: {command}')
        print(f'Testing command formation => {command}_to')

        if getattr(self.curr_room, f'{command}_to') is not None:
            self.curr_room = getattr(self.curr_room, f'{command}_to')
        else:
            print(f'!! -- Direction not available from your current room -- !!')
    
    def add_item(self, item):
        self.bag.append(item)

        return_string = f''
        return_string += f'{item} was added to your bag'

        return return_string

    def drop_item(self, item):
        if item in self.bag: 
            self.bag.remove(item)

            return_string = f''
            return_string += f'{item} was removed from your bag'

            return return_string
        else:
            return_string = f''
            return_string += f'{item} is not in your bag'
            
    def __str__(self):
        output = '*\n'
        output += f'PLAYER CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'**\n'
        output += f'Current Room:\n'
        output += f'{self.curr_room}\n'
        output += f'**\n'
        output += '*'

        return output

# Test Player Class
# testPlayerClass = Player('testPlayer')
# print(testPlayerClass)