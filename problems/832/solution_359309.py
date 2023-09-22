#Q1
def eh_quadrada(matriz):
    '''identifica se a matriz é quadrada ou não;
    list->bool'''

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if len(matriz) == len(matriz[l]):
                return True
            else:
                return False