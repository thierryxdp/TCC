def bolos (A, B, C):
    """funcao que dado o numero de ingedientes resulta na quantidade de bolos
    máxima que João consegue fazer; int,int,int -> int"""
    return min(A//2, B//3, C//5)