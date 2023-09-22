import math
def bolos(A,B,C):
    """funcao que determina qual a quantidade maxima de bolos que Joao consegue fazer
    	int, int, int -> int"""
    return min((A//2),(B//3),(C//5))