import math

def bolos(A,B,C):
    """retorna o numero maximo para se fazer um bolo dados as xicaras de farinha (A), ovos (B) e as colheres de sopa de leite (C)"""
    return math.min(A/2,B/3,C/5)