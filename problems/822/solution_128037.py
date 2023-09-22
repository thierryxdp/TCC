def repetidos(numeros):
    '''
    '''
    i = 0
    repetidos = ()
    while i < len(numeros):
        if lis.count(numeros[i],numeros[0:]):
            repetidos = numeros[i]
        i=i+1
    return repetidos