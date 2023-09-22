def eh_quadrada(matriz):
    '''Retorna se a lista de entrada e quadrada(mesmo numero
    de linhas e colunas) ou nao
    list -> bool'''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False