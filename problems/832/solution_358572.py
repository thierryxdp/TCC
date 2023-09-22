def eh_quadrada(matriz):
    '''função que identifica se uma matriz é quadrada
    (matriz)= matriz
    saida = booleano'''
    def quadrado(matriz):
    if len(matriz)==0:
        return True
    else:
        return False
    matrizquadrada = linhas(len(matriz))==colunas(len(matriz[0]))
    return matrizquadrada