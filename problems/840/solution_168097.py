import math
def bolos(A, B, C):
    """calcula quatos bolos podem ser feitos com os igredientes xicara de farinha 'A', ovo 'B' e colher de sopa de leite 'C'"""
    return math.min(A//2 , B//3, C//5)