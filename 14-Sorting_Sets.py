# >>> nums =[1,4,2,7,3,8,3,4,8,1]
# >>> sorted(nums)

# [1, 1, 2, 3, 3, 4, 4, 7, 8, 8]
# >>> names =['shaun','ryu','abe','apple']

# >>> sorted(names)
# ['abe', 'apple', 'ryu', 'shaun']

# >>> set(nums)
# {1, 2, 3, 4, 7, 8}   //set will remove duplicate and print in sorted ways

def belt_count(dictionary):
    belts = list(dictionary.values())

    for belt in set(belts):
        num=belts.count(belt)
        print(f'There are {num} {belt} belts')


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
belt_count(ninja_belts)

#OUTPUT
# enter a ninja name:hi
# enter a belt colour:black
# add another? (y/n)n
# There are 1 black belts