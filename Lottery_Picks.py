# Richard Brown
# March 28, 2020
# SDEV 300 - Lab #2
# This program will generate both 3- and 4- digit lottery numbers
# Each nymberical position is individually generated within range(0, 9)
import random

print('\n\t>>>>>  Welcome to the Pick-3 and Pick-4 Lottery Generator  <<<<<')
## prompt user for lottery picks selection
selection = int(input('\nPlease select from the following menu:\n\n1. Generate'
                      '3-Digit Lottery Number\n2. Generate 4-Digit Lottery' 
                      'Number\n3. Exit the application\n>> '))
## selection 3 will exit the program after printing closing message
while selection != 3:
    ## generate and print a 3- digit lottery selection
    if selection == 1:
        print('\nYou selected 1. Your 3-digit Lottery Numbers are:\n', )
        print(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
              sep=', ') # three random number generators
        selection = int(input('\nPlease select from the following menu:\n\n1.'
              'Generate 3-Digit Lottery Number\n2. Generate 4-Digit Lottery'
              'Number\n3. Exit the application\n>> '))
    ## generate and print a 4- digit lottery selection
    if selection == 2: # four random number generators
        print('\nYou selected 2. Your 4-digit Lottery Numbers are:\n', )
        print(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
              random.randint(0, 9), sep=', ') # four random number generators
        selection = int(input('\nPlease select from the following menu:\n\n1.'
              'Generate 3-Digit Lottery Number\n2. Generate 4-Digit Lottery'
              'Number\n3. Exit the application\n>> '))
## closing message when the number 3 is selected by the user
print('\n\t>>>>>Thank you for using this lottery program<<<<<')
