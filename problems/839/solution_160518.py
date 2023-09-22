def carros(num_pessoas,limite=5):
    """Calcula a quantidade de carros para transportar um numero inserido de pessoas"""
    import math
    return math.ceil(num_pessoas/limite)