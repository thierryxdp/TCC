def filtraMultiplos(lista,n):
    
    """Essa funcao retorna os multiplos de um numero que estao contidos em uma lista dada como entrada;
    list, int -> list"""

    i = 0
    nova_lista = []

    while  i < len(lista):
        if lista[i] % n == 0:
            list.append(nova_lista, lista[i])
        i = i + 1
    return nova_lista