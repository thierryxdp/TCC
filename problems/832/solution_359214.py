def eh_quadrada(matriz):
    """funcao que define se uma 
    matriz e quadrada.Entrada matriz
    saida string"""
    i=list.range(len(matriz))
    j=list.range(len(matriz[0]))
    if i!=j:
        return False
    if i==j:
        return True