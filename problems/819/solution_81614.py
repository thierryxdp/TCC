def filtraMultiplos(lista, n):
    """Retorna os elementos de uma lista que são divisíveis por n, dado uma lista de números """
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos