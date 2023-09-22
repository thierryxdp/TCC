def faltante(lista):
    ''' '''
    list.sort(lista)
    j = 0
    x = 1
    while j < len(lista):
        if lista[j] == j + 1:
            x = lista[j] + 1
    return x