def filtraMultiplos (lista,n):
    '''Dada uma lista, filtre os múltiplos de um número n
    e retorne uma nova lista contendo os elementos da 
    original que forem divisíveis por n;
    list, int -> list'''
    i = 0
    lista2 = []
    
    while i < len(lista):
        if (lista [i] % n) == 0:
            lista2 = lista2 + [lista [i]]
        i = i + 1
    return lista2