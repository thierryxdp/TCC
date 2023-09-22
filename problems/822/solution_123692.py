def repetidos(lista):
    '''dada uma lista de números, retorna o número de vezes que um elemento da lista
    é igual ao elemento anterior;
    list --> int'''
    i = 0
    n = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            n = n + 1
        i = i + 1
    return n