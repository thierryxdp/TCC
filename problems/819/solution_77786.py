def filtraMultiplos(lista, n):
    '''...'''
    lista_divisiveis = []
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            lista1 = lista_divisiveis + (lista[i],)
            i = i + 1
            return list(lista_divisiveis)