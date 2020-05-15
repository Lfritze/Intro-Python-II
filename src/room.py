# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []

        self.n_to = None 
        self.s_to = None 
        self.e_to = None 
        self.w_to = None

    def __str__(self):
        output = ''
        output += f'ROOM CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Description: {self.desc} \n'
        output += f'Methods: {self.n_to, self.s_to, self.e_to, self.w_to} \n\n'
        
        for i in self.items:
            output += f'Item in {self.name}: {i} \n'
        
        return output

# Test Room Class
# testRoomClass = Room('testRoom', 'testRoom description')
# print(testRoomClass)