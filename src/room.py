# Implement a class to hold room information. This should have name and
# description attributes.

# init constructor method 'DUNDER METHODS' __init__  __str__

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []
    
     # References to connected rooms in each direction
    self.exits = {
      "n": None,
      "s": None,
      "e": None,
      "w": None,
    }

  def __str__(self):
    output = ''
    output += f'Roomdie \n'
    output += f'Name: {self.name} \n'
    output += f'Description: {self.description} \n'
    output += f'Exit Methods: {self.exits} \n\n'

    for i in self.items:
      output += f'Item is in {self.name}: {i} \n'

    return output

testRoomClass = Room('THsi is a test for Room', 'Room description goes here Test')
print(testRoomClass)