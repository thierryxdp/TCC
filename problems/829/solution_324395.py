def soma_h(N):
    '''Function that calculates the value of the somatory
    H = 1 + 1/2 + 1/3 ... 1/N, given the last term N (a positive
    interger) as parameter.
    Int --> Float'''
    term = 1
    somatory = 0
    while term <= N:
        somatory = somatory + 1/term
        term = term + 1
    return round(somatory, 2)