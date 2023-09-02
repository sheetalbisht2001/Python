# from 17-Methods_Attributes import Planet



# naboo = Planet('Naboo',3000,8,'Naboo System') 
# print(f'Name:{naboo.name}')

# print(naboo.spin('a very high speed'))

from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo',3000,8,'Naboo System')    

naboo_mass = planet_mass(naboo.gravity,naboo.radius)
naboo_val = planet_vol(naboo.radius)

print(f'{naboo.name}has a mass of {naboo_mass} and a volume of {naboo_val}')

   
