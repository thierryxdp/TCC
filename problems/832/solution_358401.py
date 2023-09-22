def eh_quadrada(matriz):
    """função que recebe uma matriz e identifica se ela é
    ou não quadrada.
    list -> bool"""
    if matriz == []:
        return True

    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas == colunas:
        return True
    else:
        return False