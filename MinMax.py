# Richard Brown - SDEV 300
# March 16, 2020
# Lab_One - This program prompts the user for five integer values,
# then determines which value is the lowest, and which is highest

print ('\nWelcome to this awesome Minimum and Maximum program')
# prompt user for five different integer values
inputNumberOne = input('\nPlease enter the first Integer value: ')
inputNumberTwo = input('Please enter the second Integer value: ')
inputNumberThree = input('Please enter the third Integer value: ')
inputNumberFour = input('Please enter the fourth Integer value: ')
inputNumberFive = input('Please enter the last Integer value: ')

# find and print smallest number entered by user
print('\n\t> The smallest number is', min(int(inputNumberOne),
      int(inputNumberTwo), int(inputNumberThree), int(inputNumberFour),
      int(inputNumberFive)))
# find and print largest number entered by user
print('\n\t> The largest number is', max(int(inputNumberOne),
      int(inputNumberTwo), int(inputNumberThree), int(inputNumberFour),
      int(inputNumberFive)))
# say good-bye
print ('\nThank you for using this amazing Minimum and Maximum program')
