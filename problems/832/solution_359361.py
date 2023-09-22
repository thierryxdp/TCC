def eh_quadrada(matriz):
    """funcao que identifica se uma matriz e quadrada.
    Entrada-matriz,saida-boleano"""
    if matriz==[]:
        return True
    j=range(len(matriz[0]))
    i=range(len(matriz))
    if i==j:
        return True
    if i!=j:
        return False