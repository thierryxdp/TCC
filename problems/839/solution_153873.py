def carros(pessoas,capacidade=5):
    """calcula a quantidade de veículos necessária para transportar uma determinada quantidade de pessoas. Se o valor da capacidade não for definida, retorna para capacidade de 5 pessoas"""
    int,int,int -> int 
    import math
    return math.ceil(pessoas/capacidade)