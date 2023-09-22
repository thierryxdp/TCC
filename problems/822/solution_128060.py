def repetidos(numeros):
    '''
    '''
    i = 0
    repetidos = ()
    while i < len(numeros):
        if list.count(numeros[i],3) > 1:
            repetidos = numeros[i]
        i=i+1
        return len(repetidos)