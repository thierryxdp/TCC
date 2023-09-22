def eh_quadrada(matriz):
    ''' informa se a matriz dada é quadrada
    list -> bool'''
    i=0
    for x in range(len(matriz)):
        for y in range(len(matriz[i])):
            if x == y:
                i+=1
            else:
                return False
    return True