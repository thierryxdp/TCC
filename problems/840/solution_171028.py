import math
def farinha(q,p=2):
    """retornar o dado farinha"""
    return math.floor(q/p)
def ovo(q,p=3):
    """retornar o dado ovo"""
    return math.floor(q/p)
def leite(q,p=5):
    """retornar o dado leite"""
    return math.floor(q/p)
def bolos(a,b,c):
    """retornar o n° máximo de bolos que ele pode fazer com os dados"""
    return min(farinha(a),ovo(b),leite(c))