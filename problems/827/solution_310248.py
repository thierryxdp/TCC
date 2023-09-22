def qtd_divisores(Number):
    '''Function that, given a number as parameter,
    returns the quantity of divisors it has.
    Int --> Int'''
    divisor = 1
    divisorsOfNumber = []
    while divisor <= Number:
        if Number%divisor == 0:
            divisorsOfNumber = divisorsOfNumber + [divisor]
        divisor = divisor + 1 
    return len(divisorsOfNumber)