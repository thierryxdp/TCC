def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    if matriz == []:
        return True
    elif linhas == colunas:
        return True
    else:
        return False