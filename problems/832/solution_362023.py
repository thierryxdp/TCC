def eh_quadrada(matriz):
    """Define se uma matriz é quadrdada ou não
    list -> bool"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    if colunas == 0:
        return True
    if linhas == colunas:
        return True
    if linhas != colunas:
        return False