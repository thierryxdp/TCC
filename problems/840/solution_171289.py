import math
def bolos(A,B,C):
    """função que retorna a quantidade de bolos que João consegue fazer com 'A' xicaras de farinha, 'B' ovos e 'C' colheres de sopa de leite. int,int,int->int"""
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))