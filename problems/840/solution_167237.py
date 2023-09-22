def bolos (A,B,C):
    """determina a quantidade de bolos máxima que pode ser feita de acordo com a quantidade de ingredientes A, B, C.
    int,int,int -> int"""
    return min(A//2,B//3,C//5)