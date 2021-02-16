# Richard Brown
# March 28, 2020
# SDEV 300 - Lab #2
# This program generates an x value, then runs the value through a set of math
# functions - (cosine, sine, square root, and log10).  The x value is then
# incremented and run again through the math functions.  Incrementation and
# range differ based on the math function.  

from math import cos, sin, sqrt, log10, pi


def cosine_generator():
    """increments through cosine function, (range (-2 * pi) - (2 * pi)"""
    cos_generator_counter = (-2 * pi) # minimum range
    print('\n\t\t\t\t >>>>>>>>>>  COSINE OUTPUT  <<<<<<<<<<\n')
    while cos_generator_counter <= (2 * pi): # maximum range
        ## output x and f(x) values
        print('x = ', cos_generator_counter, '\n\tf(x) = ', 
              cos(cos_generator_counter))
        ## incremental value
        cos_generator_counter += (pi / 64)

# 
def sine_generator():
    """increments through sine function, (range (-2 * pi) - (2 * pi)"""
    sin_generator_counter = (-2 * pi) # minimum range
    print('\n\t\t\t\t >>>>>>>>>>  SINE OUTPUT  <<<<<<<<<<\n')
    while sin_generator_counter <= (2 * pi): # maximum range
        ## output x and f(x) values
        print('x = ', sin_generator_counter, '\n\tf(x) = ', 
              sin(sin_generator_counter))
        ## incremental value
        sin_generator_counter += (pi / 64)


def sqrt_generator():
    """increments through square root function, (range 0-200)"""
    sqrt_generator_counter = 0 # minimum range
    print('\n\t\t\t\t >>>>>>>>>>  SQRT OUTPUT  <<<<<<<<<<\n')
    while sqrt_generator_counter <= 200: # maximum range
        ## output x and f(x) values
        print('x = ', sqrt_generator_counter, '\n\tf(x) = ', 
              sqrt(sqrt_generator_counter))
        ## incremental value
        sqrt_generator_counter += 0.5


def log10_generator():
    """increments through log10 function, (range 0-200)"""
    log10_generator_counter = 0 # minimum range
    print('\n\t\t\t\t >>>>>>>>>>  LOG10 OUTPUT  <<<<<<<<<<\n')
    while log10_generator_counter <= 200: # maximum range
        ## output x and f(x) values
        print('x = ', log10_generator_counter, '\n\tf(x) = ', 
              log10(log10_generator_counter))
        ## incremental value
        log10_generator_counter += 0.5


"""each function call executes a math function. Caution: each math function
generates more than 250 lines of output and should be run individually"""
cosine_generator()
sqrt_generator()
log10_generator()
sine_generator()
