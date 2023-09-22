import math
def bolos(A,B,C):
    """determina a quantidade maxima de bolos que se consegue fazer, dados os materiais;
    int, int-> float"""
    return math.ceil(((A+B+C)/10))