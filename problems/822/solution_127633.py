def repetidos(lista):
    '''Faça uma função que retorne o número de vezes que um elemento da lista é igual ao elemento anterior, list -> int'''
    x = 0
    iteracao = []
    while x<len(lista):
        listanum = lista[x]
        if listanum[x] == listanum[x]:
        iteracao = iteracao + 1
        x = x + 1
    return iteracao