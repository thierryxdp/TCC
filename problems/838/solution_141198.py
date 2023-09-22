from math import floor
def num_bombons(d, p):
    '''função que calcula o maoir número de bombons possível que pedrinho pode comparar dado o dinheiro(d) e o preço do bombom(p).'''
    return floor(d/p)