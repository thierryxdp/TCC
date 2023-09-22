def bolos(a,b,c):
    """calcula a quantidade maxima de bolos que podem ser feitos, dada as variaveis (a:xicaras de farinha de trigo) (b:ovos) (c:colheres de sopa de leite)"""
    return min(a//2,b//3,c//5)