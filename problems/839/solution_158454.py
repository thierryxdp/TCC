from math import ceil

def carros(pessoas,capacidade=5):
    '''funcao que define o numero de carros necessarios
    
    '''
    return ceil(pessoas/capacidade)