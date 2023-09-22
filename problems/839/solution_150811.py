from math import *
def carros(p,c=5):
    '''calcula a quantidade de veículos de capacidade 5 ou c necessários para levar p pessoas'''
    return ceil(p/c)