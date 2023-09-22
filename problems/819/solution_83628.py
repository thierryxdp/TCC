def filtraMultiplos(lista, n):
    """Recebe uma lista e um número inteiro (n) e retorna
    uma outra lista contendo apenas os multiplos de n na lista
    list, int --> list"""
    multiplos = []
    i = 0
    while i < len(lista):
        if ((lista[i] % n) == 0):
            multiplos = multiplos + [lista[i],]
        i = i + 1
    return multiplos