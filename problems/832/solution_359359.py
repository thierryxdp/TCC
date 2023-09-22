def eh_quadrada(matriz):
    """funcao que identifica se uma matriz e quadrada.
    Entrada-matriz,saida-boleano"""
    j=range(len(matriz[]))
    i=range(len(matriz))
    if i==j:
        return True
    if i!=j:
        return False