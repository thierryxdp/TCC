def primo(number):
    '''Function that, given a number as parameter, 
    returns true if it is a prime number, or false, otherwise.
    Int --> Bool'''
    divisor = 1
    divisorsOfNumber = []
    while divisor <= 9:
        if number%divisor == 0:
            divisorsOfNumber = divisorsOfNumber + [divisor]
        divisor = divisor + 1 
    return len(divisorsOfNumber) == 0