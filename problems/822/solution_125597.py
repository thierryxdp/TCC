def repetidos(lista):
    """retorna quantas vezes um elemento da lista foi igual ao elemento anterior"""
    """list -> int"""
    i = 1
    x = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            x += 1
        i += 1
    return x