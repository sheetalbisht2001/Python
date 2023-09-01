class Planet:

    shape ='round'  #instance level attributes

    def __init__(self,name,radius,gravity,system):
        self.name=  name    #class level attributes
        self.radius= radius
        self.gravity= gravity
        self.system= system

    def orbit(self):
      return f'{self.name} is orbiting in the {self.system}'
    

    @classmethod  #class method is accessible to all class level attributes
    def commons(cls):
       return f'All planets are {cls.shape} because of gravity'
    
    @staticmethod #it has access to individual only
    def spin(speed='2000 miles per hour'):
        return f'THe planet spins and spins a {speed}'
    
naboo = Planet('Naboo',3000,8,'Naboo System')    



print(Planet.commons())
print(Planet.spin())
print(naboo.spin('a very high speed'))
