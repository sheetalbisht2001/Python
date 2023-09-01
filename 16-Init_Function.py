class Planet:

    def __init__(self,name,radius,gravity,system):
        self.name=  name
        self.radius= radius
        self.gravity= gravity
        self.system= system

    def orbit(self):
      return f'{self.name} is orbiting in the {self.system}'

hoth = Planet('Hoth',2000,5.5,'Hoth System')    
print(f'Name is:{hoth.name}')
print(f'Radius is:{hoth.radius}')
print(f'the gravity is:{hoth.gravity}')
print(hoth.orbit())


naboo = Planet('Naboo',3000,8,'Naboo System')    
print(f'Name is:{hoth.name}')
print(f'Radius is:{hoth.radius}')
print(f'the gravity is:{hoth.gravity}')
print(naboo.orbit())



# OUTPUT
# Name is:Hoth
# Radius is:2000
# the gravity is:5.5
# Hoth is orbiting in the Hoth System
# Name is:Hoth
# Radius is:2000
# the gravity is:5.5
# Naboo is orbiting in the Naboo System
