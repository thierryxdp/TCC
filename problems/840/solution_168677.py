import math
def bolos(A,B,C):
    """Função que determina os bolos que podem ser feitos dados os devidos ingredientes"""
    """A=xícaras de farinha de trigo, B=ovos,C=colheres de sopa de leite"""
    """int,int,int -> int"""
    A = A / 2
    B = B / 3
    C = C / 5
    bolo = (A+B+C)/3
    A >> B >> C
    return math.floor(bolo)