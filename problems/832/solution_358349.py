def eh_quadrada(matriz):
    if matriz == []:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False