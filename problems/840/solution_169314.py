import math
def bolos (a,b,c):
    '''Ajudar o João a determinar a quantidade máxima de bolos que ele consegue fazer'''
    trigo(a//2)
    ovos (b//3)
    leite (c//5)
    return min(trigo,ovos,leite)