from math import *
def num_bombons(d,p):
    '''calcula o maior numero de bombons(que custam p cada)
    que Pedrinho pode comprar com um valor d de dinheiro'''
    return floor(d/p)