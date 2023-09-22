from math import*
def bolos(a,b,c):
    """calcula a quantidade de bolos que João pode fazer com os materiais que tem"""
    return min(floor(a/2),floor(b/3),floor(c/5))