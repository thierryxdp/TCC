import math
def bolos(A,B,C):
    """calcula e retorna a quantidade maxima de bolos que é possivel fazer
    usando como referencia uma receita que leva 2 xicaras de farinha, 3 ovos
    e 5 colheres de sopa de leite;

    Entradas:
            A,B,C: int
            quantidades de farinha, ovo e leite respectivamente
    Saida:
            int
            um numero representando a quantidade maxima de bolos
    """
    a = math.floor(A/2)
    b = math.floor(B/3)
    c = math.floor(C/5)

    return min(a,b,c)