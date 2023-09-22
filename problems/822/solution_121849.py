def repetidos(lista):
    """Retorna o número de vezes que um elemento da lista é igual ao elemento anterior; lista -> int."""
    i = 1
    x = 0
    while i < len(lista):
        if lista[i]== lista[(i-1)]:
            x = x + 1
            i = i + 1
        else:
            i = i + 1
    return x