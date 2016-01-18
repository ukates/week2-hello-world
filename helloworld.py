# Derrick Cates

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

def helloworld():
    print('Hello World!') # this is what will display as printed text
    print() #this will display a blank line 
    print('Type one of the numbers below and I will greet you in that language!')
    print('    1. Spanish')
    print('    2. Chinese')
    print('    3. Italian')

    choice = input() # This is an assignment statement

    if choice == str(1): # If the user types the number 1 this statement would be true
        print('Hola!')
    if choice == str(2): 
        print('Ni Hao')
    if choice == str(3):
        print('Ciao!')
