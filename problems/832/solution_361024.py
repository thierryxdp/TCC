def eh_quadrada(matriz):
    '''Recebe uma matriz e informa se ela é ou não quadrada (matriz vazia 
    é considerada quadrada); list(list) -> bool'''
    if (matriz == []) or (len(matriz) == len(matriz[0])):
        return True
    else:
        return False