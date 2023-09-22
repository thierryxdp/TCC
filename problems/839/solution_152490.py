from math import *
def carros(n,c=5):
    '''calcula a quantidade de carros com capacidade 
    de passageiros c necessaria para transportar 
    n passageiros'''
    return ceil(n/c)