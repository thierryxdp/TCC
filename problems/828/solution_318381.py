def primo(number):
    '''Function that, given a number as parameter, return
    true, if it`s a prime, or false, if it isn`t.
    Int --> Bool'''
    if number%2 == 0:
        return False
    else: 
        divisor = 3
        divisors = []
        while divisor < number:
            if number%divisor == 0:
                divisors = divisors + [divisor]
                if len(divisors) != 0:
                    return False
        	divisor = divisor + 2
        return True