def eh_quadrada(matriz):
    """Define se uma matriz é quadrdada ou não
    list -> bool"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    if (linhas == colunas)or((linhas or colunas)==0):
        return True
    else:
        return False