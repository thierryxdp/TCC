def bolos(A,B,C):
    """ função que determina a quantidade 
    máxima de bolos que João pode fazer"""
    quantidade = [A//2, B//3, C//5]
    return min(quantidade)