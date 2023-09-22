def eh_quadrada(matriz):
    '''funcao que identifica se a matriz dada na entrada é quadrada ou não;
    list->bool'''

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if len(matriz) == len(matriz[l]) or matriz == []:
                return True
            else:
                return False