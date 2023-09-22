import math
def carros (p, c=5):
    '''retorna o número de carros necessários para transportar X pessoas
    int->float
    
    p= pessoas 
    c= capacidade'''
    
    return ceil(p/c)