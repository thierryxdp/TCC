def eh_quadrada(matriz):
    if matriz == []:
        return True
    conta_linha = len(m)
    conta_coluna = len(m[0])
    if conta_linha == conta_coluna:
        return True
    else:
        return False