def faltante(lista):
    ''' '''
    list.sort(lista)
    i= 0
    iguais=list(range(1,lista[-1]))
    while i < len(lista):
        if lista[i] != i + 1:
            return i + 1
        i += 1
        elif:
            return lista[-1]+1