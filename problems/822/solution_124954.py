def repetidos (numeros):
    ''' '''
    i=0
    lista2= []
    while i < len(numeros):
        if numeros[i] == numeros[i+1]:
            lista2= lista2+1
        i=i+1  
    return lista2