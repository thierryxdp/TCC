def repetidos(numeros):
    '''
    '''
    i = 0
    repetidos = ()
    while i < len(numeros):
        if len(list.count(numeros[i],numeros[0:])):
            repetidos = repetidos + len(numeros[i])
        i=i+1
    return repetidos