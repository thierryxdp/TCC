def eh_quadrada(matriz):
    '''função que identifica se uma matriz é quadrada
    (matriz)= matriz
    saida = booleano'''
    if len(matriz)==0:
        return True
    matrizquadrada = linhas(len(matriz))==colunas(len(matriz[0]))
    return matrizquadrada