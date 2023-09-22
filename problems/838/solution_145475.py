import math
def num_bombons(dp,vb):
    """Retornar o n° máximo de bombons que ele pode comprar"""
    return math.ceil(dp/vb)