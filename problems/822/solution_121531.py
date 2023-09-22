def repetidos (lista):
    '''retorna aquantidade de vezes que um elemento da lista é igual ao elemento anterior a ele
    list -> int'''
    i = 1
    n = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            n = n + 1
        i = i + 1
    return n