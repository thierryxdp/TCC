from math import ceil
def bolos (A,B,C):
    """funcao que determina a quantidade maxima de bolos que Joao pode fazer;
    int,int,int -> int"""
    return math.ceil(min(A/2,B/3,C/5))