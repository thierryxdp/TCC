from math import*
def bolos(A,B,C):
    """funçao que dada a quantidade de material ele retorna a quantidade maxima de bolos que ele consegue fazer int,int,int->int.
    dados: A,B,C sao respectivamente xicara de farinha de trigo, ovos e colheres de sopa de leite"""
    a= A//2
    b= B//3
    c= C//5
    return min(a,b,c)