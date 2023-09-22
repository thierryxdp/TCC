def filtraMultiplos(lista,n):
    """Entra com uma lista de números e um número n qualquer.
    Retorna outra lista contendo todos os elementos da 1ª lista
    que forem divisíveis por n.
    list->list"""
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i]%n == 0:
            multiplos.append(lista[i])
        i = i + 1
    return multiplos