def repetidos(lista):
    '''Recebe como entrada uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior.'''
    '''list->int'''
    numeros = 0
    proximo = 0
    while proximo<len(lista):
        if lista[proximo - 1] == lista[proximo]:
            numeros = numeros + 1
        proximo = proximo + 1
    return numeros