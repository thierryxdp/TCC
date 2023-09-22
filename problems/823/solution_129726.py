def faltante(lista):
    ''' '''
    list.sort(lista)
    i= 0
    while i < len(lista):
        if lista[i] != i + 1:
            return i + 1
        i += 1
        if lista==list(range(1,len(lista)):
            return lista[-1]+1