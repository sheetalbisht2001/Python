
# WITH THE HELP OF type() we can find the type of object
# >>> name ='sheetal'
# >>> age = 21
# >>> nums=[1,2,3,4]

# >>> type(name)
# <class 'str'>

# >>> type(nums)
# <class 'list'>

# >>> type(age)
# <class 'int'>

class Planet:

    def __init__(self):
        self.name='Hoth'
        self.radius=200000
        self.gravity=5.5
        self.system='Hoth System'

    def orbit(self):
      return f'{self.name} is orbiting in the {self.system}'

hoth = Planet()    
print(f'Name is:{hoth.name}')
print(f'Radius is:{hoth.radius}')
print(f'the gravity is:{hoth.gravity}')
print(hoth.orbit())



# OUTPUT 
# Name is:Hoth
# Radius is:200000
# the gravity is:5.5
#Hoth is orbiting in the Hoth System

