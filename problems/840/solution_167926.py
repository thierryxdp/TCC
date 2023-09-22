from math import*
def bolos(A,B,C):
    """Dado o numero de xícaras de trigo A, ovos B e colheres de sopa
    de leite B, a função calcula a quantidade bolos que você poderá 
    fazer e a retorna.
    Parametros de Entrada:int,int,int
    Retorna int"""
    return min(A//2, B//3, C//5)