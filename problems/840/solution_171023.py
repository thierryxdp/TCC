import math
def farinha(q,p=2):
   """Retornar farinha"""
	return math.floor(q/p)
def ovo(q,p=3):
    """Retornar ovo"""
    return math.floor(q/p)
def leite(q,p=5):
    """Retornar leite"""
    return math.floor(q/p) 
def bolo(a,b,c):
    """Retornar o n° máximo de bolos que ele pode fazer"""
    return min(farinha(a),ovo(b),leite(c))