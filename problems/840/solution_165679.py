import math
def bolos(A,B,C):
    """dadas as quantidades de ingrediente disponível, calcula quantos bolos podem ser feitos"""
    return min(A//2,B//3,C//5)