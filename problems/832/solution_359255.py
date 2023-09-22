def eh_quadrada(matriz):
    """funcao que define se uma 
    matriz e quadrada.Entrada matriz
    saida string"""
    i=range(len(matriz))
    if i==0:
        return True
    j=range(len(matriz[0]))
    if i!=j:
        return False
    if i==j:
        return True