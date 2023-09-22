def eh_quadrada(matriz):
    ''' informa se a matriz dada é quadrada
    list -> bool'''
    i=0
    for x in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            i+=1
        else:
            return False
    return True