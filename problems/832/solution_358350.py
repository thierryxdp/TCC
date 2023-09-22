def eh_quadrada(matriz):
    """ a função retorna se a matriz dada é quadrática ou não"""
    if matriz == []:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False