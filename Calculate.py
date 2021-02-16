# Richard Brown - SDEV 300
# March 16, 2020
# Lab_One - This program prompts the user to select a math function,
# then performs that function on two integers values entered by the user.

print ('\nWelcome to this awesome Python coded calculator\n')
# provide user with the math function options
print ('Select 1 for ADDITION ( + )')
print ('Select 2 for SUBTRACTION ( - )')
print ('Select 3 for DIVISION ( / )')
print ('Select 4 for MULTIPLICATION ( * )')
print ('Select 5 for MODULUS ( % )')
# prompt user for selection
userSelection = int(input('\nPlease make your selection: '))
userInputOne = int(input('\t>> Please provide the first integer value: '))
userInputTwo = int(input('\t>> Please provide the second integer value: '))
# determine which selection the user chose, and then execute the math function
# on the set of integers input by the user
# Selection 1
if userSelection == 1:
    print ('\nYou have chosen to ADD the two values:', userInputOne,
           'and', userInputTwo)
    userAdditionAnswer = userInputOne + userInputTwo
    print ('\nThe sum of those two integers is:', userAdditionAnswer)
# Selection 2
if userSelection == 2:
    print ('\nYou have chosen to SUBTRACT the two values', userInputOne,
           'and', userInputTwo)
    userSubtractionAnswer = userInputOne - userInputTwo
    print ('\nThe difference of those two integers is: ',
           userSubtractionAnswer)
# Selection 3
if userSelection == 3:
    print ('\nYou have chosen to DIVIDE the two values: ', userInputOne,
           'and', userInputTwo)
# alert to user that the value entered is not valid
# and then re-prompts for valid value
    if userInputTwo <= 0:
        userInputTwo = int(input('\nThis program is unable to divide by zero '
                       'or negative numbers,\nPlease select a non-zero'
                       ' positive integer value: '))
    userDivisionAnswer = userInputOne / userInputTwo
    print ('\nThe quotient of those two integers is: ', int(userDivisionAnswer))
# Selection 4
if userSelection == 4:
    print ('\nYou have chosen to MULTIPLE the values: ', userInputOne, 'and',
           userInputTwo)
    userMultiplicationAnswer = userInputOne * userInputTwo
    print ('\nThe product of those two integers is: ', 
           userMultiplicationAnswer)
# Selection 5
if userSelection == 5:
    print ('\nYou have chosen to find the REMAINDER of: ', userInputOne,
           'and', userInputTwo)
# alert to user that the value entered is not valid
# and re-prompts for valid value
    if userInputTwo <= 0:
        userInputTwo = int(input('\nThis program is unable to divide by zero '
                       'or negative numbers,\nPlease select a non-zero'
                       ' positive integer value: '))
    userModulusAnswer = userInputOne % userInputTwo
    print ('\nThe remained of those to two integers is: ', userModulusAnswer)
# saying good-bye
print ('\nThank you for using this awesome Python programmed calculator')
