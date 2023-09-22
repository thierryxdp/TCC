import math
def bolos(A,B,C):
    """Função que determina a quantidade máxima de bolos que joão
    consegue fazer dado A=xicaras de farinha de trigo,B=ovos,C=colheres de leite"""
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))