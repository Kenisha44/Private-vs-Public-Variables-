#abstraction means hiding or abstracting away information given access to only what is neccessary. 

#private? "_", most likely means this should be a private variable
class PlayerCharacter: 
  def __init__(self, name, age):
   self._name = name 
   self._age = age 

  def run(self):
     print('run')
    
  def speak(self):
     print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter("Kenisha", 100)

# player1.name = '!!!'
# player1.speak = 'Boooo'

# print(player1.speak)

print(player1.speak)
