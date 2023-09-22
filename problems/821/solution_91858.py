def fatorial(Number):
    '''Function that, given a number as parameter, returns
    the factorial of that number.
    Int --> Int.'''
    Result = 1
    NumberX = Number #NumberX is referent to the digression of the number until it reaches the value 1.
    while NumberX != 1: 
        Result = Result*NumberX
        NumberX = NumberX - 1
    return Result