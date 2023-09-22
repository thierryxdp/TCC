import math
def xicara(a):
   """quantas xicaras de farinha precisam"""
    return a//2
def ovos(b):
    """quantos ovos precisam"""
    return b//3
def leite(c):
   """quanto de leite precisa"""
    return c//5
def bolos(a,b,c):
    """quantida de bolos possiveis"""
    return min(xicara(a),ovos(b),leite(c))