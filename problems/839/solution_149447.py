def carros (p,c=5):
    ''' Funcao que calcula e retorna o numero aproximado de carros 
    necessarios dado o número de pessoas (p) e a capacidade do veiculo 
    (c) '''
    import math
    return math.ceil (p/c)