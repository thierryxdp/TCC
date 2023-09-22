def repetidos(numeros):
    '''...'''
    i = 0
    j = 0
    while(i < len(numeros)):
        if numeros[i] == numeros[i-1]:
            j += 1

        if (i == 0):
            j = 0
        i += 1

    return j