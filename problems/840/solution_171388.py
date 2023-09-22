import math
def bolos (A, B, C):
    """Calcula quantos bolos João pode fazer com quantidade A, B e C de farinha, ovos e leite"""
    return min ( math.floor (A/2), math.floor (B/3), math.floor (C/5))