def bolos(A,B,C):
    """determina a quantidade máxima de bolos que João consegue fazer. float, int, float -> int"""
    return min(int(A/2),int(B/3),int(C/5))