import math
def bolos (A,B,C):
    """calcula o numero de bolos que joao consegue fazer com os ingredientes disponiveis"""
    return math.ceil min(A/2,B/3,C/5)