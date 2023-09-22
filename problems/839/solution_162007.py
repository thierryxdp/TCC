def carros (pessoas, capacidade=5):
    '''funcao que calcula e retorna o numero exato de carros necessarios;
    int, int -> int'''
    import math
    return math.ceil (pessoas / capacidade)