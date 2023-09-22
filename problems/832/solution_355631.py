def eh_quadrada(matriz):
    """A funcao eh_quadrada recebe como entrada uma matriz qualquer, no formato
    de lista de listas, e retorna se esta é quadrada; ou seja, possui o mesmo numero
    de linhas e colunas."""
    if len(matriz)>0 and len(matriz) == len(matriz[0]):
        return True
    if len(matriz)>0 and len(matriz) != len(matriz[0]):
        return False
    if len(matriz) == 0:
        return True