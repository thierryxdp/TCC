def repetidos(numeros):
    '''
    '''
    i = 0
    repetidos = ()
    while i < len(numeros):
        if list.count(numeros[i],numeros[0:]) > 1:
            repetidos = repetidos + len(numeros[i])
        i=i+1
    return repetidos