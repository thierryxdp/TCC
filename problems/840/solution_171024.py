import math
def farinha(q,p=2):
    """retornar farinha"""
    return math.floor(q/p)
def ovo(q,p=3):
    """retornar ovo"""
    return math.floor(q/p)
def leite(q,p=5):
    """retornar leite"""
    return math.floor(q/p)
def bolos(a,b,c):
    """retornar o n° máximo de bolos que ele pode fazer"""
    return min(farinah(a),ovo(b),leite(c))