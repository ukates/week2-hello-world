# Derrick Cates

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!


print('Hello World!') # this is what will display as printed text when the program begins. 
print() #this will display a blank line 
print('Type one of the numbers below and I will greet you in that language!')
print('    1. Spanish')
print('    2. Chinese')
print('    3. Huttese') # Huttese is the language of the Huts in StarWars!

choice = input() # This is an assignment statement, the user makes a choice by typing a number. That input is assigned to the word 'choice' which is used to determine if the "if" statement is true or false. 

if choice == str(1): # If the user types the number 1 this statement would be true because choice would equal the input and the input would = 1.  
    print('Hola!')
if choice == str(2): 
    print('Ni Hao')
if choice == str(3): #previous if statements are made false by users input, and the input = 3 then the huttese greeting will display!
    print('Achuta!')




    
    
