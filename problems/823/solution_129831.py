def faltante(lista):
    '''função'''
    list.sort(lista)
    i = 0
    while i < len(lista):
        if lista[i] == i+1:
            n = lista[i] = 1
        i += 1
    return n