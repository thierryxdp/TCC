def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = int
    if matriz == []:
        colunas = linhas
        return True
    for i in range(linhas):
        colunas = len(matriz[0])
        if (linhas == colunas):
            return True
    if linhas != colunas:
        return False