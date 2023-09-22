def carro_viajem(p,carros=5):
    '''retorna a quantidade minima de carros necessaria para a viajem
    dado o numero de pessoas (p)
    caso o carro tenha capacidade diferente de 5 e necessario a entrada de sua capacidade'''
    import math
    return math.floor(p/carros)