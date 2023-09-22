def carros(num_passageiros, lugares=5):
    """Calcula e retorna quantos carros serão necessários 
    int,int -> int"""
    ca = num_passageiros/lugares
    import math
    carros = math.ceil(ca)
    return carros