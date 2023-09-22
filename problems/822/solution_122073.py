def repetidos(listaNum):
    '''Retorna o número de vezes que um elemento de uma lista é igual ao
    elemento anterior dada uma lista de números'''
    i = 1
    total = 0
    while (i < len(listaNum)):
        if (listaNum[i] = listaNum[i-1]):
            total = total + 1
        i = i + 1
    return total