import math
def bolos(a,b,c):
    """Calculao número de bolos que João conseguirá fazer dados a xícaras de farinha, b ovos e c colheres de sopa de leite"""
    return min(a//2,b//3,c//5)