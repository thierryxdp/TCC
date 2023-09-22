def eh_quadrada(matriz):
    linhas = len(matriz)
    if matriz == Null:
        return True
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False