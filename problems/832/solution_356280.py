def eh_quadrada(matriz):
    """Determina se uma matriz é ou não uma matriz quadrada
       lista ~> bool"""
    colunas = 0
    if matriz == []:
        return True
    elif matriz != []:
        linha = range(len(matriz) + 1)
        coluna = range(len(matriz(i) + 1))
        for i in linha:
            linhas = 0
            for j in coluna:
                colunas += 1
            linhas += 1
        if linhas == colunas:
            return True
        else:
            return False