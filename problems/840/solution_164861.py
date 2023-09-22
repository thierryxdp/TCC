import math
def bolos(a,b,c):
    '''Calcule a quantidade máxima de bolos que consegue fazer'''
    return max(a/3,b/3,c/5)- min(a,b,c)