def eh_quadrada(matriz):
    """Essa função recebe uma lista de listas (uma matriz).
    Se não tiver colunas, seja quadrada (e vazia). Se o nº 
    de colunas for igual o nº de linhas; seja quadrada.
    Se o nº de colunas diferir do nº de linhas, não será
    quadrado."""
    if len(matriz) == 0: return True
    if len(matriz) == len(matriz[0]): return True
    if len(matriz) != len(matriz[0]): return False