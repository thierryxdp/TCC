import math

def bolos(a,b,c):
    """função que calcula o número de bolos que João consegue fazer a partir de um
    mínimo de ingredientes necessários, sendo que João só faz medidas exatas"""
    return min(math.floor(a/2), math.floor(b/3), math.floor(c/5))