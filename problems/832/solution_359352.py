def eh_quadrada(matriz):
    """funcao que identifica se uma matriz e quadrada.
    Entrada-matriz,saida-boleano"""
    i=range(len(matriz))
    j=range(len(matriz[i]))
    if i==j:
        return True
    if i!=j:
        return False