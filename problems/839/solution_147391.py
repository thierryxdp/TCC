def carros(p,c=5):
    """calcula o numero de carros necessarios para transportar p pessoas"""
    import math
    return math.ceil(p/c)