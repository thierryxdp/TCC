def repetidos(numeros):
    '''Conta quantas vezes um elemento de uma dada
    lista é igual ao anterior;
    list -> int'''
    indice = 1
    contador = 0
    
    while indice < len(numeros):
        if numeros[indice] == numeros[indice-1]:
            contador += 1
        indice += 1
    return contador