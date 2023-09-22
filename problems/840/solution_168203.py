import math
def bolos (a,b,c):
    """retorna a quantidade de bolos que podem ser feitos
    dados os parametros, a (xicaras), b (ovos), c (colheres)"""
    return math.floor(min((a/2),(b/3),(c/5)))