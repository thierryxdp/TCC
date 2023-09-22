def eh_quadrada(matriz: list)-> bool:
    """Função que dada uma matriz, retorna 'True' caso a matriz seja quadrada ou
    retorna 'False', caso contrário."""

    linhas_matriz = len(matriz)
    colunas_matriz = len(matriz[0])

    if (linhas_matriz == colunas_matriz):
        return True
    elif (linhas_matriz != colunas_matriz):
        return False
    else:
        return True