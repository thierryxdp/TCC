def filtraMultiplos(lista_de_numeros, n):
    '''Função que recebe uma lista de números e um número n e retorna uma lista contendo todos os elementos da lista original que forem divisíveis por n.'''
    '''list, int/float -> list'''
    numeros = []
    i = 0
    while i < len(lista_de_numeros):
        if lista_de_numeros[i] % n == 0:
            numeros += [lista_de_numeros[i]]
        i += 1
    return numeros