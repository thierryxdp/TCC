def carros(num_pessoas,capacidade_v=5):
    """Calcula e retorna quantos carros serão necessários 
    int,int -> int"""
    ca = num_pessoas/capacidade_v
    import math
    carros = math.ceil(ca)
    return carros