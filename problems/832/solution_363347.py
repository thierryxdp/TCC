def eh_quadrada(matriz):
    '''Função que verifica se a matriz dada é quadrada.
    matriz -> list
    return -> bool'''
    
    if matriz == list():
        return True
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False