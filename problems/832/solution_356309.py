def eh_quadrada(matriz):
    '''A função que dada uma matriz de entrada identifica se ela se a matriz é quadrada contando o número de linhas e colunas
    retornando o booleano True caso a condição se satisfaça ou False caso contrário. list->bool'''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False