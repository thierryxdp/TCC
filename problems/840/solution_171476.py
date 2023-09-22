from math import*
def bolos(A,B,C):
    """ Calcula qual o máximo de bolos que João pode fazer com A xícaras, B ovos e C colheres, int,int,int -> int"""
    N = min((A//2),(B//3),(C//5))
    return N