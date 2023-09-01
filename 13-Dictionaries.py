# # //dictionaries is a datatype
# #key in dict (key in we are looking for )



# python3
# Python 3.8.10 (default, May 26 2023, 14:05:08) 
# [GCC 9.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
  
# >>> ninja_belts ={"crystal":"red","ryu":"black"}
# >>> ninja_belts
# {'crystal': 'red', 'ryu': 'black'}


# >>> ninja_belts['crystal']
# 'red'

# >>> ninja_belts['ryu']
# 'black'

# >>> 'yoshi'
# 'yoshi'

# >>> 'yoshi' in ninja_belts
# False

# >>> 'ryu' in ninja_belts
# True

# >>> ninja_belts.key()  //key should be spelled  correctly like keys
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'key'


# >>> ninja_belts.keys()
# dict_keys(['crystal', 'ryu'])


# >>> list(ninja_belts.keys())
# ['crystal', 'ryu']

# >>> ninja_belts.values()
# dict_values(['red', 'black'])



# >>> vals = list(ninja_belts.values())
# >>> vals
# ['red', 'black']

# >>> vals.count('black')
# 1

# >>> vals.count('red')
# 1

# >>> vals.count('blue')
# 0

# >>> ninja_belts['yoshi']='blue'

# >>> ninja_belts
# {'crystal': 'red', 'ryu': 'black', 'yoshi': 'blue'}

# >>> person=dict(name="shaun",age=27,height="6ft")
# >>> person
# {'name': 'shaun', 'age': 27, 'height': '6ft'}
# >>> 


def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')


ninja_belts={}

while True:
    ninja_name= input('enter a ninja name:')
    ninja_belt = input('enter a belt colour:')
    ninja_belts[ninja_name]=ninja_belt


    another = input('add another? (y/n)')
    if another == 'y':
     continue
    else:
     break

ninja_intro(ninja_belts)




# OUTPUT

# enter a ninja name:sita
# enter a belt colour:black
# add another? (y/n)y
# enter a ninja name:sheetal
# enter a belt colour:blue
# add another? (y/n)n
# I am sitaand I am a black belt
# I am sheetaland I am a blue belt


