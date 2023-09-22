def carros(n,q=5):
    '''
    Calcula quantos carros serão necessários dado o número de pessoas e a capacidade máxima permitida em cada carro.
    
    Parametros
    ----------
    n : número de pessoas
    q : capacidade máxima
    '''
    from math import ceil
    return ceil(n/q)