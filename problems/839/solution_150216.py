from math import ceil
def carros(p,c=5):
    '''Calcule o numero necessario de carros dado o numero de pessoas'''
    return ceil(p/c)