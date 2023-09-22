def repetidos (numeros):
    '''recebe uma lista de numeros e retorna o número de vezes em que um número apareceu repetidamente'''
    '''lista->lista'''
    i=0
    lista2= 0
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            lista2+= 1
        i=i+1  
    return lista2