# Richard Brown - UMGC - SDEV 300 - Lab # 3
# 05 April 2020
# this module is designed to square and cube all Integers within a range 1 -100 
# there is also a function that allows the user to provide an Integer value and
# determine if that Integer is contained within both a set of squared_integers
# and cubed_integers, if TRUE the values are returned for that Integer
# User menu is also provided that loops until exited

RANGE = range(1, 101)


def square_integer():
    """Squares all Integers between 1 - 100 and stores them """
    global counter_the_first
    # print('>>> SQUARE INTEGERS <<<')
    counter_the_first = 1  # minimum range
    set2 = {counter_the_first ** 2}
    while counter_the_first in RANGE:  # maximum range
        set2.add(counter_the_first ** 2)
        counter_the_first += 1
    return set2


def cube_integer():
    """Cubes all Integers between 1 - 100 and stores them """
    # print('>>> CUBE INTEGERS <<<')
    counter_for_math = 1  # minimum range
    set2 = {counter_for_math ** 3}
    while counter_for_math <= 99:  # maximum range
        counter_for_math += 1
        set2.add(counter_for_math ** 3)
    return set2


def return_square_and_cube(user_integer_input):
    """Searches two sets of squared and cubed numbers to determine if the """
    """value provided is contained within. If TRUE, the squared and cubed """
    """values are returned in output """
    input1 = user_integer_input
    ## comparison of user Integer input to squared and cubed sets
    if input1 ** 2 in square_integer() and input1 ** 3 in cube_integer():
        print('Your selection of ', user_integer_input, '\n\tSquared is ',
        user_integer_input ** 2, '\n\t>>AND<<\n\tCubed is ', 
        user_integer_input ** 3)


def math_menu_for_user():  # main function to run the program, provides menu too
    user_selection = int(input(f'\nThe have the following options\n1: Display'
        'the Square and Cube for Integers\n\tRanging from 1 through 100\n2: '
        'Search for a specific Integer range 1 through 100\n\tthen display the'
        'Square and Cube values\n3: Display the UNION of both square and cube'
        'sets\n4: Display the INTERSECTION of both Square and Cube sets\n5: '
        'Display the DIFFERENCE of both Square and Cube sets\n6: EXIT PROGRAM\n'
        '\n\t>>'))
    ## function calls based on user selection of provided menu
    while user_selection != 6:
        if user_selection == 1:
            print(sorted(square_integer()), sorted(cube_integer()))
            math_menu_for_user()
        elif user_selection == 2:
            user_input_to_math = int(input('\nPlease provide an Integer to do'
                ' square and cube upon:\n\t'))  # comparison Integer prompt
            return_square_and_cube(user_input_to_math)
            math_menu_for_user()
        elif user_selection == 3:
            print(sorted(square_integer().union(cube_integer())))
            math_menu_for_user()
        elif user_selection == 4:
            print(sorted(square_integer().intersection(cube_integer())))
            math_menu_for_user()
        elif user_selection == 5:
            print(sorted(square_integer().difference(cube_integer())))
            math_menu_for_user()
    
    print('Thank you for using this awesome and amazing Python program')


math_menu_for_user()  ## runs the module
