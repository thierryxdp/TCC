import math
def bolos (a,b,c):
    """retorna a quantidade de bolos que podem ser feitos
    dado a quantidade de xicaras de farinha a, ovos b, e
    colheres de sopa c"""
    if min(a,b,c)==a and c>=5:
        return math.floor(a/2)
    elif min(a,b,c)==b:
        return math.floor(b/3)
    elif min(a,b,c)==c:
        return math.floor(c/5)
    else:
        return 0