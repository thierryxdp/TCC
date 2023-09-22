def repetidos(numeros):
    '''Dado uma lista retorna a quantidade de vezes que o elemento anterior'''
    
    numeros_repetidos = 0
    i = 0
    
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            numeros_repetidos+= 1
        i += 1
    return numeros_repetidos