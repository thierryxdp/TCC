def bolo(A,B,C):
    """funcao que, dado as medidas de farinha e trigo(a), numero de ovos (b) e numerode colheres de sopa de leite(c),retornara a quantidade maxima de bolo que joao consiguira fazer"""
    return min((a//2),(b//3),(c//5))