def repetidos(lista):
    '''Faça uma função que retorne o número de vezes que um elemento da lista é igual ao elemento anterior, list -> int'''
    x = 0
    iteracao = 0
    while x<len(lista):
        if lista[x] == lista[x]-1:
            iteracao = iteracao + 1
        x = x + 1
    return iteracao