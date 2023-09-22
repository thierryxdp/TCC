def eh_quadrada(matrizA):
    """Função que identifica se uma matriz é quadrada,lista-->bool"""
    nlinhas=len(matrizA)
    nelementos=len(matrizA[0][1][2][3][4][5][6])
    ncolunas=nelementos/nlinhas
    if nlinhas==ncolunas:
        return True
    else:
        return False