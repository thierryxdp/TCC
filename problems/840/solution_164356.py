import math
def bolos(a,b,c):
    """calcula e retorna o maximo de bolos que podem ser feitos, sendo
    a o numero de xicaras de farinha, b o numero de ovos e c o numero de
    colheres de sopa; a=int, b=int, c=int -> int"""
    return math.floor (min (a/2, b/3,c/5))