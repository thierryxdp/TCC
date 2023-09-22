def farinha(A):
    """ calcule a quantidade de farinha"""
    import math
    return math.floor(A/2)

def ovos(B):
    """calcule a quantidade de ovos"""
    import math
    return math.floor(B/3)

def leite(C):
    """ calcule quantas colheres de sopa de leite serão necessárias"""
    import math
    return math.floor(C/5)

def bolos(A,B,C):
    """calcule quantos bolos João conseguirá fazer"""
    import math
    return min(farinha(A),ovos(B),leite(C))