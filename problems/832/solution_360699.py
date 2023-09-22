def eh_quadrada(matriz):
    '''recebe uma matriz e retorna se a matriz é quadrada
    ou nao.
    entrada: list
    saida: booleano'''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False