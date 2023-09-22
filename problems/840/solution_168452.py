import math
def bolos(A,B,C):
    """Funcao que retorna a quantidade maxima de bolos que consegue fazer, a partir
       A xicaras de trigo, B ovos, C colheres de sopa de leite"""
    a=math.floor(A/2)
    b=math.floor(B/3)
    c=math.floor(C/5)
    return min(a,b,c)