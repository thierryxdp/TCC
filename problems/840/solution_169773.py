import math
def bolos (A,B,C):
    """Funcao que calcula a quantidade máxima de bolos que se consegue fazer dado as entradas A,B,C"""
    a=(A//2)
    b=(B//3)
    c=(C//5)
    return (max(a,b,c))