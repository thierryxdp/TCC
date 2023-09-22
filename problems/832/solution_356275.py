def eh_quadrada(matriz):
    """Determina se uma matriz é ou não uma matriz quadrada
       lista ~> bool"""
    colunas = 0
    if matriz == []:
        return True
    elif matriz != []:
        for i in range(len(matriz) + 1):
            linhas = 0
            for j in range(len(matriz(0) + 1)):
                colunas += 1
            linhas += 1
        if linhas == colunas:
            return True
        else:
            return False