def eh_quadrada(matriz):
    """funcao que identifica se uma matriz e quadrada.
    Entrada-matriz,saida-boleano"""
    i=range(len(matriz))
    if i==0:
        return True
    j=range(len(matriz[0]))
    if i==j:
        return True
    if i!=j:
        return False