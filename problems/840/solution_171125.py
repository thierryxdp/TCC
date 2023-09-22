import math
def bolos(A,B,C):
    """quantidade de bolos que João fará
    int, int, int->int"""
    return int(min((A//2),(B//3),(C//5)))