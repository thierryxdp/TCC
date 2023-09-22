import math
def bolos(a,b,c):
    """Funcao que, dado os numeros de xicaras de farinha, o numero de ovos e o numero de colheres de sopa de leite, retorna a quantidade maxima de bolos que ele consegue fazer. int,int,int->int"""
    return min(math.floor(a/2),math.floor(b/3),math.floor(c/5))