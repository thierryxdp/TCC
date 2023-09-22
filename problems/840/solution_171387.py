import math
def bolos (A, B, C):
    """Calcula quantos bolos João pode fazer com quantidade A, B e C de farinha, ovos e leite"""
    return min ( math.ceil (A/2, B/3, C/5))