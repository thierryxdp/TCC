import math
def bolos(A,B,C):
    """Calcula o número máximo de bolos que poderá ser feito, dado o número
    dos ingredientes A(xícaras de farinha de trigo), B(ovos) e C(colheres
    de sopa de leite).
    entrada: int,int,int
    saída: int"""
    return min(A//2,B//3,C//5)