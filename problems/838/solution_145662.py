import math
def farinha(q,p=2):
    """retornar o dado farinha; int, int => float"""
    return math.floor(q/p)
def ovo(q,p=3):
    """retornar o dado ovo; int, int => float"""
    return math.floor(q/p)
def leite(q,p=5):
    """retornar o dado leite; int, int => float"""
    return math.floor(q/p)
def bolos(a,b,c):
    """retornar o n° máximo de bolos que ele pode fazer com os dados; int, int => int"""
    return min(farinha(a),ovo(b),leite(c))#Escreva sua função aqui. Pode apagar essa linha.