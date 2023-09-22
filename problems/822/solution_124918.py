def repetidos(lista):
    """Dada uma lista, retorna o numero de vezes que um elemento é igual ao seu anterior

list -> int"""
    y = 1
    x = 0
    while y < len(lista):
        if lista[y] == lista[y-1]:
            x = x + 1
        else:
            None
        y = y + 1
    return x