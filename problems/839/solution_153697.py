def carros(p,c=5):
    """Retorna a quantidade de carros necessários para
    transportar um grupo de pessoas"""
    import math
    return math.ceil(p/c)