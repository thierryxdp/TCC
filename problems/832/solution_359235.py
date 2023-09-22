def eh_quadrada(matriz):
    """funcao que define se uma 
    matriz e quadrada.Entrada matriz
    saida string"""
    i=range(len(matriz))
    j=range(len(matriz[]))
    if i!=j:
        return False
    if i==j:
        return True