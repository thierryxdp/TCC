def repetidos(numeros):
    '''
    '''
    i = 0
    repetidos = ()
    while i < len(numeros):
        if list.count(numeros[i],1) > 1:
            repetidos = len(repetidos)
        i=i+1
    return repetidos