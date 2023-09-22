import math
def bolos(a,b,c):
    """Calcula quantos bolos podem ser feitos tendo o a numero de xicaras de farinha, b ovos e c colheres de sopa de leite"""
    return math.ceil(a//2, b//3, c//5)