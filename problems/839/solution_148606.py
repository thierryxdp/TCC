def carros(n):
    """Calcula e retorna o número de carros necessários para transportar o n passageiros;
    int->int"""
    import math
    
    return math.ceil(n/5)