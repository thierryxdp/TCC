import math
def bolos(a, b, c):
    """ Calcula a quantidade de bolos posiveis de serem feitos dados
    as quantidades de xícaras de farinha de trigo(a), ovos(b) e
    colheres de sopa de leite(c).
    
    int, int, int --> int
    
    a = {2, 4, 6, 8,...}
    b = {3, 6, 9, 12,...}
    c = {5, 10, 15, 20,...}
    
   Casos de teste:
   
    """
    x == a//2
    y == b//3
    z == c//5
    
    if x < 1:
        return 0
    elif y < 1:
        return 0
    elif z < 1:
        return 0
    else:
        return math.floor((a + b + c)/10)