def repetidos (lista):
    '''Dada uma lista de números, retorne o número de vezes
    que um elemento da lista é igual ao anterior;
    list -> int'''
    i = 1
    rep = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            rep = rep + 1
        i = i + 1
    return rep