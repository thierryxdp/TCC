def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == 0 and colunas == 0:
        return True
    else:
        if linhas == colunas:
            return True
        else:
            return False