def filtraMultiplos(lista, n):
    '''Dado uma lista de números filtra os múltiplos de n;
    list, int -> int'''
    i = 0
    multiplos = []
    while i < len(lista):
        if list[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos