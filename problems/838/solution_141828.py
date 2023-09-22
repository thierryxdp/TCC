from math import floor
def num_bombons (d,p):
    '''retorna a quantidade de bombons a um preço p que pedrinho pode comprar com um valor em dinehiro d'''
    a=(d/p)
    return floor(a)