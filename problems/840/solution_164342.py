def bolos(A,B,C):
    """calcula quantos bolos sao possiveis ser feitos com as quantidades: A xicaras de farinha, B ovos, C colheres de sopa de leite"""
    import math
    return min((math.floor(A/2)),(math.floor(B/3)),(math.floor(C/5)))