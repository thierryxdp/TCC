def bolos (a,b,c,d):
    """funcao que dado as medidas de farinha de trigo(a), numero de ovos (b) e numero  de colheres de sopa de leite (c), retornara a quantidade maxima de bolo que joao consiguira fazer.
    int, int,int -> int"""
    return min((a//2),(b//3),(c//5))