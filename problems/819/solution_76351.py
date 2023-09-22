def filtraMultiplos(lista,n):
    '''Ao fornecer uma lista e um valor n, retorna os múltiplos de n em uma nova lista.
    list, float -> list'''

    lista_nova = []
    i = 0
    
    while i < len(lista):
        if lista[i] % n == 0:
            list.append (lista_nova,lista[i])
        i = i + 1
    return lista_nova