def primo(number):
    '''Function that, given a number as parameter, 
    returns true if it is a prime number, or false, otherwise.
    Int --> Bool'''
    if number%2 == 0:
        return False
    else:
        divisor = 1
    	divisorsOfNumber = []
    	while divisor <= number:
        	if number%divisor == 0:
            	divisorsOfNumber = divisorsOfNumber + [divisor]
        	divisor = divisor + 2
    	return len(divisorsOfNumber) == 0