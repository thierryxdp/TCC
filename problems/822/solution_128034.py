def repetidos(numeros):
    '''
    '''
    i = 0
    repetidos = ()
    while i < len(numeros):
        if numeros[i] > 1:
            repetidos = len(numeros[i])
        i=i+1
    return repetidos