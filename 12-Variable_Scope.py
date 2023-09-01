# my_name ="sheetal" //GLOBAL

# def print_name():
#     print("the name inside the function is",my_name)

# print_name()
# print("outside the function the name is",my_name)  

# OUTPUT
# the name inside the function is sheetal
# outside the function the name is sheetal



# my_name ="sheetal" 

# def print_name():
#     my_name='sita'
#     print("the name inside the function is",my_name)

# print_name()
# print("outside the function the name is",my_name) 

# OUTPUT

# the name inside the function is sita
# outside the function the name is sheetal


my_name ="sheetal" 

def print_name():
    global my_name
    my_name ='sita'
print("the name inside the function is", my_name)

print_name()
print("outside the function the name is", my_name) 




